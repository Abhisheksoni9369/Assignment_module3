import random

def read_random_line(filename):
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    num_lines = len(lines)
    
    random_line_num = random.randint(0, num_lines - 1)
    
    
    return lines[random_line_num].strip()


filename = 'sample.txt'  

try:
    random_line = read_random_line(filename)
    print("Random line from", filename + ":", random_line)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print("Error:", e)
