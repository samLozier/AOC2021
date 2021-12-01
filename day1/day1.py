from pathlib import Path

FILE_DIR = Path(__file__).parent

def load_data(filename:str)->list[int]:
    data = (FILE_DIR / filename).read_text().strip()
    data = [int(d) for d in data.split()]
    return data

def count_growth(data: list[int])->int:
    reference =data[0]
    count = 0
    for i in data:
        if i > reference:
            count += 1
        reference = i

    return count

def update_lists(data, index, step):

    A = data[index:index+step]
    B = data[index+1:index+1+step]
    return A, B

def part_b(data: list[int], step: int)->int:
    index = 0
    counter = 0

    A, B = update_lists(data, index, step)
    while len(A) == step and len(B) == step:
        if sum(B) > sum(A):
            counter +=1
        index += 1
        A, B = update_lists(data, index, step)
    return counter



if __name__ == "__main__":
    data = load_data("day1_input.txt")
    print(count_growth(data))

    print(part_b(data, 3))
