from typing import Dict, Any, List
from utils.logger import print_banner, print_running_message, print_clean_message, print_dirty_message, erease_last_line
import sys
from glob import glob
import os
import time
from colorama import Fore, Back, Style

class CSSProperty():
    def __init__(self, name, value):
        self.name = name
        self.unparsed_value = value
        self.values = self.parse_values()

    def __str__(self) -> str:
        return f"CSS Property: {self.name}, Value: {self.unparsed_value}"

    def strip(self, value: str,  strip_of: str) -> str:
        return value[0:value.find(strip_of)] 

    def to_theme(self) -> List:
        new_values = [] 
        for pos in range(len(self.values)):
            if 'rem' in self.values[pos]:
                new_values.append(f"theme.spacing({str(float(self.strip(self.values[pos], 'rem')) * 2)})")
        return [self.name, new_values]

    def parse_values(self) -> List[str]:
        paren = [pos for pos, char in enumerate(self.unparsed_value) if char == "'"]

        if "'" in self.unparsed_value and len(paren) > 1:
            start_quote, end_quote = [pos for pos, char in enumerate(self.unparsed_value) if char == "'"]

            return self.unparsed_value[start_quote + 1 : end_quote].split(' ')
        else:
            return [self.unparsed_value]


class File():
    def __init__(self, lines):
        self.lines = lines

    def replace_line(self, line_content: str, line_number: int) -> None:
        self.lines[line_number] = line_content


class Cop():
    def __init__(self, file: File,  rules: Dict[str, Any]):
        self.file = file
        self.rules = rules
        self.culprits = []
        self.violations = []

    def is_suspect(self, line):
        return True if ':' in line and '{' not in line else False

    def get_violation(self, line):
       print(line) 

    def is_legall(self, prop: CSSProperty):
        required = self.rules["property_requires"].get(prop.name)

        if not required: return True

        if len(prop.values) > 1:
            for value in prop.values:
                if required not in value:
                    self.violations.append(f"{prop.name} requires {required}")
                    return False
        else:
            if required not in prop.values[0]:
                self.violations.append(f"{prop.name}-requires-{required}")
                return False

        return True

    def translate(self, line) -> List[str]:
        return [line[0:line.find(':')].strip(' '), line[line.find(':') + 2: len(line) - 1]]
    
    def reformat(self, culprit: int , name: str, values: str) -> None:
        og = self.file.lines[culprit -1]
        comp = ''
        if len(values) > 1:
            for value in values:
                comp = comp + "${" + value + '}px ' 
        comp = f"`{comp}`"
        
        new_line = f"{og[0:og.find(name)]}{name}: {comp[0:-1]}, \n"
        print(self.file.lines[culprit - 1])
        print(new_line)


    def investigate(self) -> None:
        self.culprits = [pos for pos, line in enumerate(self.file.lines, 1) if self.is_suspect(line) and not self.is_legall(CSSProperty(self.translate(line)[0], self.translate(line)[1]))]


    def reform(self) -> None:
        if not self.culprits: 
            print('Pixel Cop: There are no culprits in the file specified! Please try again ... ')
            return None

        for culprit in self.culprits:
            name, value = self.translate(self.file.lines[culprit - 1])
            css = CSSProperty(name, value)
            name, new_values = css.to_theme()
            self.reformat(culprit, name, new_values)

def get_lines(file_path):
    return open(file_path, 'r').readlines()


def search_files(root):
    files = glob(root + '/**/*.styles.ts', recursive=True)
    return files

if __name__ == "__main__":
    start_time = time.time()
    print_banner()
    files_ran = 0
    files_dirty = 0
    files_clean = 0
    lines_dirty = 0
    lines_clean = 0
    lines_ran = 0
    for file in search_files('/home/nysteo/dev/cox/dri-frontend/packages/consumer-checkout/src'):
        print_running_message(file[len('/home/nysteo/dev/cox/dri-frontend/packages/consumer-checkout/src'): len(file)])
        files_ran += 1
        file_ins = File(get_lines(file))
        lines_ran += len(file_ins.lines)
        cop = Cop(file_ins, {"property_requires": {
            "margin": "theme.spacing",
            "marginLeft": "theme.spacing",
            "marginRight": "theme.spacing",
            "marginBottom": "theme.spacing",
            "padding": "theme.spacing",
            "paddingRight": "theme.spacing",
            "paddingBottom": "theme.spacing",
            "paddingLeft": "theme.spacing",
        }})
        cop.investigate()
        if len(cop.culprits) == 0:
            print_clean_message(file[len('/home/nysteo/dev/cox/dri-frontend/packages/consumer-checkout/src'): len(file)])
            print("\n", end="")
            lines_clean += len(file_ins.lines)
            files_clean += 1
        else:
            print_dirty_message(file[len('/home/nysteo/dev/cox/dri-frontend/packages/consumer-checkout/src'): len(file)])
            files_dirty += 1 
            output = ""

            counter = 0
            for culprit in cop.culprits:
                counter += 1 
                lines_dirty += 1
                output += f"{culprit}  "
            lines_clean += len(file_ins.lines) - counter

            for idx in range(len(cop.culprits) - 1):
                print(f"  {Fore.RED}violation:{Fore.WHITE}{Style.NORMAL} line {cop.culprits[idx]} violates rule: {Style.BRIGHT}{cop.violations[idx]}{Style.RESET_ALL}")
            print("\n", end=" ")


    print("\n")
    print(f"\033[1m{Fore.WHITE}Files: {Fore.RED}{files_dirty} dirty, {Fore.GREEN}{files_clean} clean{Fore.WHITE}{Style.DIM} of {files_ran} files{Style.RESET_ALL}")
    print(f"\033[1m{Fore.WHITE}Lines: {Fore.RED}{lines_dirty} dirty, {Fore.GREEN}{lines_clean} clean{Fore.WHITE}{Style.DIM} of {lines_ran} lines{Style.RESET_ALL}")
    print(f"\033[1m{Fore.WHITE}Time: {round(time.time() - start_time, 2)} seconds")

    

                

