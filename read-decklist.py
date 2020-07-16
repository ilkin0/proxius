from decouple import config

file = open(config("DECKLIST"), "r")


def readDecklist(file):
    if file.mode == "r":
        contents = file.read()
        print(contents)


readDecklist(file)
