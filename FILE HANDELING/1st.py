with open("hi.txt","w") as file:
    file.write("Hello\n")
    file.writelines(["hello\n","how r you"])


with open("hi.txt","r") as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())


with open("hi.txt","w+") as file:
    file.write("Hello\n")
    file.writelines(["hello\n","how r you"])
    print(file.read())