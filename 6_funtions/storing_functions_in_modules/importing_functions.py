# 1 - import message_funtions
    # call: message_function.show_messages(unsent)
# 2 - from message_funtions import show_messages, send_messages
    # call: show_messages(unsent)
# 3 - from message_funtions import show_messages as show, send_messages as send
    # call: show(unsent)
# 4 - from message_funtions import *
    # call: show_message(unsent)

import message_funtions as mf

unsent = ['I love Python', 'I love Computer Science', 'I love Programming']
sent = []

mf.show_messages(unsent)
mf.send_messages(unsent, sent)
print('Unsent Messages:', unsent)
print('Sent Messages:', sent)
