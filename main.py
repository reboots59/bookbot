def word_count(contents):
    words = len(contents.split())
    return words

def character_counts(contents):
    character_list = {}
    lowered_book = contents.lower()
    for letter in lowered_book:
        if letter not in character_list:
            character_list[letter] = 1
        else:
            character_list[letter] += 1
    return character_list

def book_report(contents):
    print("--- Begin report of books/frankenstein.txt ---")

    # Call your word count function
    words = word_count(contents)
    print(f"{words} words found in the document\n")

    char_counts = character_counts(contents)

    char_list = []
    for char, count in char_counts.items():  # Changed from character_counts to char_counts
        if char.isalpha():  # We only want alphabetic characters
            char_list.append({"char": char, "count": count})

    # Now we sort the list
    char_list.sort(key=lambda x: x["count"], reverse=True)

    # Print the sorted character counts
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")



def main():
    with open('books/frankenstein.txt', 'r') as file:
        contents = file.read()
       
        book_report(contents)

if __name__ == "__main__":
    main()

