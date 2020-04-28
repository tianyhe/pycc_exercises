# 10.3 - Guest
guest_file_path = "/Users/tianyaohe/GitHub/python_learning/pycc/8_files_and_exceptions/guest.txt"
with open(guest_file_path, 'w') as guest_file:
    name = input('What is your name?\n')
    guest_file.write(name)

# 10.4 - Guest Book
guestbook_file_path = "/Users/tianyaohe/GitHub/python_learning/pycc/8_files_and_exceptions/guest_book.txt"
with open(guestbook_file_path, 'a') as guestbook_file:
    while True:
        name = input("What is your name? (enter 'q' to quit)\n")
        if name == 'q':
            break    
        guestbook_file.write(f"{name.title()}\n")
        print(f"Hi {name.title()}, welcome to my hotel!")

# 10.5 - Programming Poll
polling_file_path = "/Users/tianyaohe/GitHub/python_learning/pycc/8_files_and_exceptions/polling_results.txt"
with open(polling_file_path, 'a') as polling_results_file:
    while True:
        response = input("Why you like programming? (enter 'q' to quit)\n")
        if response == 'q':
            break
        polling_results_file.write(f"{response}\n")
        