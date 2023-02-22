def readfile(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

print(readfile("doc1.txt"))

