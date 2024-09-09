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


def listOfDict(dict):
    list_of_char = []
    for i,v in dict.items():
        list_of_char.append({"char":i,"num":v})
    return list_of_char


def main():
    file_location = "books/frankenstein.txt"
    file_contents = getFileContent(file_location)
    number_of_strings = strCount(file_contents)
    number_of_characters = charCount(file_contents)
    sorted_list_of_chars = sorted(listOfDict(number_of_characters),key=lambda x: x["num"], reverse=True)

    print(f"--- Beging report of {file_location} ---")
    print(f"{number_of_strings} words found in the document \n")
    for i in sorted_list_of_chars:
        char = i["char"]
        num = i["num"]
        if char.isalpha():
            print(f"The {char} character was found {num} times")
    print(f"--- End report ---")


if __name__ == "__main__":
    main()