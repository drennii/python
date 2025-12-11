# file_path="example.txt"
# file=open(file_path,"r")
#
# content=file.read()
# print(content)
#
# file.close()
# import os

# with open("example.txt","wrd") as file:
#      file.write('Hello World')
#
# with open("example.txt","r") as file:
#      content=file.read()
#      line=file.readline()
#      lines=file.readlines()
#
# lines=['Hello World\n',"Welcome to Python\n"]
# with open("example.txt","w") as file:
#     file.writelines(lines)
#
# with open("example.txt",'r') as file:
#     file.seek(0)
#     data=file.read()
#     print(data)

# if os.path.exists("example.txt"):
#     print("File exist")
#
#
#
#
# with open("example.txt","a") as file:
#     file.write("New data append")

with open("example.txt","r") as file:
    for line in file:
        cleaned_line=line.strip()
        print(cleaned_line)

with open("example.txt","r") as file:
    for line in file:
        words=line.strip().split()
        print(words)

name="Alice"
age=30

with open("example.txt","w") as file:
    file.write("Name:"+name+'\n')
    file.write("Age:"+ str(age) +'\n')

with open("example.txt","w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age:{age}")

