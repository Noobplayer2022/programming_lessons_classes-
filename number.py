import random

def generate_numbers():
    try:

        with open('numbers.txt', 'w') as file:
            for _ in range(1000):
                number = random.randint(1, 1000)  
                file.write(str(number) + '\n')
        print("1000")
    except:
        print("erro")

def calculate_average():
    
    try:

        with open('numbers.txt', 'r') as file:
            numbers = []
            for line in file:
                if line.strip():  
                    numbers.append(float(line.strip()))
        

        if numbers:
            total = sum(numbers)
            count = len(numbers)
            average = total / count
            print("count", count)
            print("average", average)
        else:
            print("file is empty")
    except:
        print("error invalid")


generate_numbers()
calculate_average()