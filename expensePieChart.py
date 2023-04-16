import matplotlib.pyplot as plt

def read_expenses(file_name):
    expenses = {}
    with open(file_name) as file:
        for line in file:
            label, value = line.strip().split('\t')
            try:
                expenses[label] = int(value)
            except ValueError:
                print(f"Skipping invalid value '{value}' for '{label}'")
    return expenses

def create_pie_chart(expenses):
    labels = expenses.keys()
    values = expenses.values()
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.title("Monthly expenses")
    plt.show()

def main():
    try:
        expenses = read_expenses('expenses.txt')
        create_pie_chart(expenses)
    except IOError:
        print("Error: Could not open file 'expenses.txt'")
    except ValueError as e:
        print(f"Error: Invalid data in file - {e}")

main()
