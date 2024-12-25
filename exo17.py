numbers= []
shoe_sizes= []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

shoe_sizes.append(8)
shoe_sizes.append(9)
shoe_sizes.append(10)
shoe_sizes.append(11)
shoe_sizes.append(12)
    
print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)

numbers.append(3) 
print("\nNumbers List with Duplicate Added:", numbers)

numbers = list(set(numbers))  
numbers.sort() 
print("Numbers List after Removing Duplicates:", numbers)

combined_list = numbers + shoe_sizes
print("\nCombined List (Numbers + Shoe Sizes):", combined_list)