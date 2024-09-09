def getFileContent(location):
    with open(location) as f:
        return f.read()

def strCount(input):
    words = input.split()
    return len(words)

def main():
    filelocation = "books/frankenstein.txt"
    file_contents = getFileContent(filelocation)

    print(strCount(file_contents))


if __name__ == "__main__":
    main()