# 10.1 - Learning Python
file_name = 'learning_python.txt'
file_path = f"/Users/tianyaohe/GitHub/python_learning/pycc/8_files_and_exceptions/txt/{file_name}"
with open(file_path) as file_object:
    content = file_object.read()

print("---Reading the Entire File---")
print(content)

with open(file_path) as file_object:
    lines = file_object.readlines()

print("---Looping Over the File Object---")
for line in lines:
    print(line.strip())

print("---Storing the line in a List---")
file_string = ''
for line in lines:
    file_string += line.strip()
print(file_string)

# 10.2 - Learning C
print("---Replace 'Python' with 'C'---")
for line in lines:
    print(line.replace('Python', 'C').strip())
