alph = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ'
word = alph[0]
alphPos, wordLen = 0, 0


def CheckZ(point):
    while alph.index(word[point]) == len(alph) - 1:
        point -= 1
        if point == -1:
            return True
    return False


def ZSpot(point):
    while alph.index(word[point]) == len(alph) - 1:
        point -= 1
    return point


if __name__ == "__main__":
    user = input('1. Run\n2. Use custom alphabet\n> ')
    if user == '2':
        alph = input("Custom Alphabet: ")
    while 1:
        # Current spot increase
        word = word[:wordLen] + alph[alphPos] + word[wordLen + 1:]

        alphPos += 1

        # Checks if spot is z
        if alphPos == len(alph):
            # Reset the letter to work with
            alphPos = 0

            # Makes all z to increase onto next letter
            if CheckZ(wordLen):
                word = ''
                wordLen += 1
                for p in range(wordLen + 1):
                    word += alph[0]
            # Makes a more than 1 back increase
            elif alph.index(word[wordLen - 1]) == len(alph) - 1:
                spot = ZSpot(wordLen)
                word = word[:spot] + alph[alph.index(word[spot]) + 1] + word[spot + 1:]
                while spot != wordLen:
                    spot += 1
                    word = word[:spot] + alph[0] + word[spot + 1:]
            # Increases the last letter
            else:
                word = word[:wordLen - 1] + alph[alph.index(word[wordLen - 1]) + 1] + word[wordLen:]

        print(word)
