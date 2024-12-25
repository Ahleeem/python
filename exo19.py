
unique_words = set()
total_word_count = 0 

print("Unique Word Counter")
print("Enter words one by one. The program stops when you enter a duplicate word.")

while True:
    word = input("Enter a word: ").strip() 
    total_word_count += 1

    if word in unique_words:
        print(f"\nYou typed in {len(unique_words)} unique words.")
        print(f"Total words : {total_word_count}")
        print("Unique words :", sorted(unique_words))
        # Save unique words to a file
        save = input("Would you like to save unique words to a file? (yes/no): ").strip().lower()
        if save == "yes":
            try:
                with open("unique_words.txt", "w") as file:
                    file.write("\n".join(sorted(unique_words)))
                print("Unique words saved to 'unique_words.txt'.")
            except Exception as e:
                print(f"Error saving to file: {e}")
        break
    else:
        unique_words.add(word)
       
   
