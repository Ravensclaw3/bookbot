def getFileContent(location):
    with open(location) as f:
        return f.read()

def strCount(input):
    words = input.split()
    return len(words)

def charCount(input):
    characters = dict()
    lowered_input = input.lower()
    for i in lowered_input:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters

def main():
    file_location = "books/frankenstein.txt"
    file_contents = getFileContent(file_location)

    print(strCount(file_contents))

    print (charCount(file_contents))


if __name__ == "__main__":
    main()