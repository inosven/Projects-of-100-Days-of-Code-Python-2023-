# # with open("a_file.txt") as file:
# #     file.read()
#
# # FileNotFound Error
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exsit.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise KeyError("This is an error I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("You are too high!")
bmi = weight / height**2

print(bmi)