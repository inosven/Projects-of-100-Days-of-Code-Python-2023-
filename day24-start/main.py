# with open("/Users/sunqu/Desktop/my_file.txt", mode="r") as file:
with open("../../Desktop/my_file.txt", mode="r") as file:

    contents = file.read()
    print(contents)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nThis is the new text.")

# with open("new_file.txt", mode="a") as file:
#     file.write("\nThis is the new file.")