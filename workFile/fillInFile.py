from random import randint, uniform

def fill_in_file(name_file: str, count_line: int) -> None:
    name_file += '.txt'
    with open(name_file, 'a', encoding='utf-8') as file:
        for _ in range(count_line):
            file.write(f"{randint(-1000, 1000)} | {uniform(-1000, 1000)} \n")