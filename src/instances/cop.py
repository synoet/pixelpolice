from typing import List, Any, Dict
from instances.property import CSSProperty
from instances.file import File

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

