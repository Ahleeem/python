#with bonus
import statistics

user_list = []

print("Enter numbers to build your list. Enter 0 to stop.")

while True:
    try:
 
        num = int(input("Enter a number: "))
        
        if num == 0:
            break  
   
        user_list.append(num)
    
        print("Current List:", user_list)
        print("Sorted List:", sorted(user_list))
        
    except ValueError:
        print("Please enter a valid integer.")


if len(user_list) > 0:

    mean_value = statistics.mean(user_list)
    median_value = statistics.median(user_list)
    
    print(f"\nList Statistics:")
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
else:
    print("\nNo numbers entered.")
    

desc_order = input("Would you like to view the list in descending order? (yes/no): ").strip().lower()
if desc_order == "yes":
    print("Sorted Descending Order:", sorted(user_list, reverse=True))


save_to_file = input("Would you like to save the list to a file? (yes/no): ").strip().lower()
if save_to_file == "yes":
    try:
        with open("user_list.txt", "w") as file:
            file.write("\n".join(map(str, user_list)))
        print("List saved to 'user_list.txt'.")
    except Exception as e:
        print(f"Error saving the list: {e}")


load_from_file = input("Would you like to load list from a file and append it? (yes/no): ").strip().lower()
if load_from_file == "yes":
    try:
        with open("user_list.txt", "r") as file:
            loaded_list = [int(line.strip()) for line in file.readlines()]
        user_list.extend(loaded_list)
        print("Loaded list from file and appended to current list.")
        print("Updated List:", user_list)
    except Exception as e:
        print(f"Error loading the list: {e}")
