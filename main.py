import time
import pyautogui
import cv2

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
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

    # print('Commands in Pyautogui form to operate')
    # command = input('Command to input: ')
    print('5 seconds to click command prompt to bruteforce')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('0')
    windowName = pyautogui.getActiveWindowTitle()

    while cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
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

        pyautogui.write(word)
        pyautogui.press('enter')
        pyautogui.press('enter')
