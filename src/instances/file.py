class File():
    def __init__(self, lines):
        self.lines = lines

    def replace_line(self, line_content: str, line_number: int) -> None:
        self.lines[line_number] = line_content

