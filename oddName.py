def main():
    name = str(input("Please input your name"))
    while len(name) == 0:
        name = str(input("Incorrect length!! \n Please input your name:"))
    for i in range(0, len(name), 2):
        print(name[i])