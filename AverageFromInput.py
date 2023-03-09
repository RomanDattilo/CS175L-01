def value_file(filename):
    total = 0.0
    count = 0
    with open(filename, "r") as file:
        for line_num, line in enumerate(file, start=1):
            try:
                number = float(line.strip())
                total += number
                count += 1
                print(f"I read in {count} number(s) Current number is: {number:8.2f} Total is: {total:8.2f}")
            except ValueError:
                print(f"Non-numeric data found in line {line_num} of file {filename}. Skipping...")

    return total, count

def file_average(total, count):
    average = total / count if count > 0 else 0.0
    print(f"Average: {average:8.1f}")

def main():
    filename = input("Enter the name of the input file: ")
    try:
        total, count = value_file(filename)
        file_average(total, count)
    except IOError:
        print(f"An error occurred trying to read the file {filename}.")
    except ValueError:
        print('Non-numeric data found in the file.')

if __name__ == '__main__':
    main()





        







        

