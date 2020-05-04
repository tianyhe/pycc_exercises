# 10.6 & 10.7 - Addition & Addition Calculator
print("Give me two number, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break

    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("Invalid Input. You must enter numeric value for both input")
        pass
    else:
        result = first_number + second_number
        print(f"Result: {result}")

# 10.8 & 10.9 - Cats and Dogs & Silent Cats and Dogs
def read_files(path, file_name):
    """Read a file and print the content of the file"""
    file_path = path + file_name
    try:
        with open(file_path) as fhand:
            lines = fhand.readlines()
    except FileNotFoundError:
        print(f"\nWe can't locate the file under the following path: {file_path}")
        #pass
    else:
        print(f"\n---{file_path}---")
        for line in lines:
            print(line.strip())

path = '8_files_and_exceptions/txt/'

read_files(path, 'cats.txt')
read_files(path, 'dogs.txt')

# 10.10 - Common Words
def count_words(path, file_name, word=None):
    """Count the approximate number of words in given path file."""
    file_path = path + file_name
    try:
        with open(file_path) as fhand:
            contents = fhand.read()
    except FileNotFoundError:
        print(f"\nWe can't locate the file under the following path: {file_path}")
    else:
        words = contents.split()
        if word is None:        
            num_words = len(words)
            print(f"The file has about {num_words} words.")
        
        else:
            # words = [word.lower() for word in words]
            # num_words = words.count(word)
            num_words = contents.count(word)
            print(f"The word '{word}' appears {num_words} times in the txt.")

path = '8_files_and_exceptions/txt/'

count_words(path, 'moby_dick.txt')
count_words(path, 'moby_dick.txt', 'the')
count_words(path, 'moby_dick.txt', 'the ')
