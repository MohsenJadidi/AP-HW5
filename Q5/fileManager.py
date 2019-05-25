import os


def create_dir(name, address):
    print("> Create Directory")
    try:
        # If the file does not exist, then it would throw an IOError
        os.chdir(address)
        os.mkdir(name)
        print("Created new Directory: ", os.path.join(os.getcwd(), name))
    except IOError:
        print("Problem: Directory existed!")


def create_file(name, address):
    print("> Create File")
    try:
        # If the file does not exist, then it would throw an IOError
        os.chdir(address)
        f = open(name, "x")  # Character Meaning : 'x' create a new file and open it for writing
        f.close()
        print("Created File: ", os.path.join(os.getcwd(), name))
    except IOError:
        print("Problem: File existed!")


def delete(name, address):
    print("> Delete Directory")
    try:
        # If the file does not exist, then it would throw an IOError
        os.chdir(address)
        os.remove(name)
        print("Remove File: ", os.path.join(os.getcwd(), name))
    except IOError:
        print("Problem: File not existed!")


def find(name, address):
    print("> Find File")
    result = []
    for root, dirs, files in os.walk(address):
        if name in files:
            result.append(os.path.join(root, name))
    # Print
    for i in range(len(result)):
        print(f'Address {i}: ', result[i])

    if len(result) == 0:
        print("Problem: File not existed!")
