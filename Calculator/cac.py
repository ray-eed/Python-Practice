count = int(input ("Enter how many number you want to calculate with: "))
exp = input ("What unit you want to work with?\nPress 1 for (+)\nPress 2 for (-)\nPress 3 for (*)\nPress 4 for (/)\nChoose: ")
total = 0
while True:
    if exp in ["1", "2", "3", "4"]:
        break
    else:
        print("Invalid input. Please try again.")
        exp = input ("What unit you want to work with?\nPress 1 for (+)\nPress 2 for (-)\nPress 3 for (*)\nPress 4 for (/)\nChoose: ")
for i in range(count):
    a = float(input(f"Enter number {i+1}: "))
    if i == 0:
        total = a
    else:
        total = total + a if exp == "1" else total - a if exp == "2" else total * a if exp == "3" else total / a if exp == "4" else total
print(f"Result: {total}")