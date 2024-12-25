
numbers = [1, 2, 3, 4, 5]


def display_menu():
    print("\nMenu:")
    print("1. Append ")
    print("2. Insert ")
    print("3. Pop")
    print("4. Remove ")
    
    print("5. Sort ")
    print("6. Reverse ")
    print("7. Search ")
    print("8. Save ")
    print("9. Load ")
    
    print("10. Quit")

while True:

    print("\nCurrent List:", numbers)
    display_menu()

    try:
 
        choice = int(input("Choose an option: "))

        if choice == 1:  # Append
            value = int(input("Enter value to append: "))
            numbers.append(value)
            print("Updated List:", numbers)

        elif choice == 2:  # Insert
            value = int(input("Enter value to insert: "))
            index = int(input(f"Enter index (0 to {len(numbers)}): "))
            if 0 <= index <= len(numbers):
                numbers.insert(index, value)
                print("Updated List:", numbers)
            else:
                print("Error: Index out of range.")

        elif choice == 3:  # Pop
            if numbers:
                index = int(input(f"Enter index to pop (0 to {len(numbers) - 1}): "))
                if 0 <= index < len(numbers):
                    removed_value = numbers.pop(index)
                    print(f"Popped value: {removed_value}")
                    print("Updated List:", numbers)
                else:
                    print("Error: Index out of range.")
            else:
                print("Error: List is empty.")

        elif choice == 4:  # Remove
            value = int(input("Enter value to remove: "))
            if value in numbers:
                numbers.remove(value)
                print("Updated List:", numbers)
            else:
                print("Error: Value not found in the list.")

        elif choice == 5:  # Sort
            numbers.sort()
            print("Sorted List:", numbers)

        elif choice == 6:  # Reverse
            numbers.reverse()
            print("Reversed List:", numbers)

        elif choice == 7:  # Search
            value = int(input("Enter value to search for: "))
            if value in numbers:
                print(f"Value {value} found at index {numbers.index(value)}.")
            else:
                print("Value not found.")

        elif choice == 8:  # Save to file
            filename = input("Enter filename to save the list: ")
            with open(filename, "w") as file:
                file.write(" ".join(map(str, numbers)))
            print(f"List saved to {filename}.")

        elif choice == 9:  # Load from file
            filename = input("Enter filename to load the list: ")
            try:
                with open(filename, "r") as file:
                    numbers = list(map(int, file.read().split()))
                print(f"List loaded from {filename}: {numbers}")
            except FileNotFoundError:
                print("Error: File not found.")
            except ValueError:
                print("Error: File contains invalid data.")

        elif choice == 10:  # Quit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
