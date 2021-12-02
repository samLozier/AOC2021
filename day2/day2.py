from pathlib import Path
from dataclasses import dataclass
FILE_DIR = Path(__file__).parent

@dataclass
class Direction:
    input_dir: str = ""
    input_value: int = ""
    x: int = 0
    y: int = 0

    def __post_init__(self):
        if self.input_dir == "down":
            self.y = self.input_value
        if self.input_dir == "up":
            self.y = -self.input_value
        if self.input_dir == "forward":
            self.x = self.input_value


def load_data(filename:str)->list[Direction]:
    data = (FILE_DIR / filename).read_text().strip()
    data = [Direction(d.split()[0], int(d.split()[1])) for d in data.split('\n')]
    return data

def calc_final(parsed_input:list[Direction])->int:
    X = sum([d.x for d in parsed_input])
    Y = sum([d.y for d in parsed_input])
    return X*Y


class CalcB:
    def __init__(self,
                 parsed_input: list[Direction]):
        self.aim = 0
        self.X = 0
        self.Y = 0
        self.parsed_input = parsed_input

    def calc_final(self)->int:
        for dir in self.parsed_input:
            if dir.y !=0:
                self.aim += dir.y
            if dir.x !=0:
                self.X += dir.x
                self.Y = self.Y+(dir.x * self.aim)
        return self.X* self.Y

if __name__ == "__main__":
    data = load_data(filename='day2_input.txt')
    final_a = calc_final(data)
    print(final_a)
    final_b = CalcB(parsed_input=data).calc_final()
    print(final_b)