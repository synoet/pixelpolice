from typing import List


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
