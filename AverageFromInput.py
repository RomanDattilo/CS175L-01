filename = input("Enter the name of the input file: ")

total = 0.0
count = 0

with open(filename, "r") as file:
    for line_num, line in enumerate(file, start=1):
        number = float(line.strip())
        total += number
        count += 1
        print(f"I read in {count} number(s) Current number is: {number:8.2f} Total is: {total:8.2f}")
        
average = total / count if count > 0 else 0.0
print(f"Average: {average:8.1f}")
