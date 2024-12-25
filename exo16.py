numbers = [1, 2, 3, 4, 5]

while True:
    try:
        index = int(input("Enter index (-1 to quit): "))
        if index == -1:
            break
        if index < 0 or index >= len(numbers):
            print("Invalid index. Please enter a number between 0 and", len(numbers) - 1)
            continue
        new_value = int(input("Enter new value: "))
        numbers[index] = new_value
        print(numbers)
    
    except ValueError:

        print("Please enter an integer.")

print("end")
