from decouple import config

file = open(config("DECKLIST"), "r")
dList = []


def read_deck(file):
    if file.mode == "r":
        lines = (line.rstrip() for line in file)
        lines = (line for line in lines if line)
        for line in lines:
            if not line.startswith('#'):
                line = line.rstrip()
                dList.append(line)
        # print(dList)


# read_deck(file)
