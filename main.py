from typing import Dict, Any, List
import sys

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
        if "'" in self.unparsed_value:
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

    def is_suspect(self, line):
        return True if ':' in line and '{' not in line else False

    def is_legall(self, prop: CSSProperty):
        required = self.rules["property_requires"].get(prop.name)

        if not required: return True

        if len(prop.values) > 1:
            for value in prop.values:
                if required not in value:
                    return False
        else:
            if required not in prop.values[0]:
                return False

        return True

    def translate(self, line) -> List[str]:
        return [line[0:line.find(':')].strip(' '), line[line.find(':') + 2: len(line) - 1]]
    
    def reformat(self, culprit: int , name: str, values: str) -> None:
        og = self.file.lines[culprit -1]
        comp = ''
        if len(values) > 1:
            for value in values:
                comp = comp + value + ' ' 
        
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

    
if __name__ == "__main__":
    file_path = sys.argv[1]
    option = sys.argv[2]
    file = File(get_lines(file_path))
    cop = Cop(file, {"property_requires": {
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
    if option == '--culprits':
        print(cop.culprits)
    elif option == '--count-culprits':
        print(len(cop.culprits))
    elif option == '--reform':
        cop.investigate()
        cop.reform()




# def is_line_faulty(line):
#     return True if ':' in line and line[0:line.find(':')].strip(' ') in target_classes and 'theme.spacing' not in line else False


# def corrector(line, counter):
#     instances = []
#     ip= [pos for pos, char in enumerate(line) if char == "'"]
#     if ip:
#         instances = line[ip[0] + 1 :ip[1]].split(' ')
#         for instance in instances:
#             if 'rem' in instance:
#                 value = instance[0:instance.find('rem')]
#                 spacing_value = (float(value) * 2)
#                 print(line)
#                 print(f"line {counter} : {instance} changed to -> theme.spacing({spacing_value})")



# def investigator():
#     """
#         Finds and returns a list of line numbers that are faulty
#     """

#     return [pos for pos, line in enumerate(get_lines('./tests/one.styles.ts'), 1) if is_line_faulty(line)]


# def pixeler():
#     faulty_lines = investigator()
#     print(faulty_lines)
