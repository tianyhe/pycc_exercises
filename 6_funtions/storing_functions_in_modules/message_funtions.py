def show_messages(text_messages):
    """print all the text messages in the list"""
    for msg in text_messages:
        print(msg)


def send_messages(unsent_messages, sent_messages):
    """
    Stimulate printing each messages, until none are left
    Move each messages to sent_messages after sending
    """
    while unsent_messages:
        current_messages = unsent_messages.pop()
        print(f"Sending messages: {current_messages}")
        sent_messages.append(current_messages)


