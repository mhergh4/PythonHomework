import random
import time

def generate_random_numbers():
    return " ".join(str(random.randint(1, 100)) for _ in range(20))

with open("data.txt", "w") as file:
    for _ in range(100):
        file.write(generate_random_numbers() + "\n")

def process_file(filename):
    def filter_numbers(line):
        return list(filter(lambda x: x > 40, map(int, line.split())))

    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()

        for line in lines:
            filtered_numbers = filter_numbers(line)
            file.write(" ".join(map(str, filtered_numbers)) + "\n")

def read_file_generator(filename):
    with open(filename, "r") as file:
        for line in file:
            yield list(map(int, line.split()))

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f} seconds")
        return result
    return wrapper

@measure_execution_time
def main():
    process_file("data.txt")
    generator = read_file_generator("data.txt")
    for i, line in enumerate(generator):
        print(f"Line {i + 1}: {line}")

if __name__ == "__main__":
    main()
