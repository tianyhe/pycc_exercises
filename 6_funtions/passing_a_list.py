# 8.9 - Messages
def show_messages(text_messages):
    """print all the text messages in the list"""
    for msg in text_messages:
        print(msg)

name_list = ['Rico', 'Liz', 'Batu', 'Chasel', 'Shawn']
show_messages(name_list)

print('\n')

# 8.10 - Sending Messages
def send_messages(unsent_messages, sent_messages):
    """
    Stimulate printing each messages, until none are left
    Move each messages to sent_messages after sending
    """
    while unsent_messages:
        current_messages = unsent_messages.pop()
        print(f"Sending messages: {current_messages}")
        sent_messages.append(current_messages)
    
unsent = ['I love Python', 'I love Computer Science', 'I love Programming']
sent = []

send_messages(unsent, sent)
print('Unsent Messages:', unsent)
print('Sent Messages:', sent)

print('\n')

# 8.11 - Archived Messages
unsent = ['I love Python', 'I love Computer Science', 'I love Programming']
sent = []
    # Call the function send_messasges() with a copy of the list of messages
send_messages(unsent[:], sent)
print('Archived Messages:', unsent)
print('Sent Messages:', sent)