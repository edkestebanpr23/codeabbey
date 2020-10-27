import math

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7']

# Encode functions


def encode(text):
    adjust = adjustIn5(text)
    octal = decToOct(adjust)
    binary = octToBin(octal)
    longBinary = ''.join(binary)
    chunk5 = divideEveryFive(longBinary)
    int26 = binToInt(chunk5)
    encodeText = base32(int26)
    return encodeText


def adjustIn5(text):
    s = 5 - (len(text) % 5)
    aux = str(s)
    while s > 0:
        text += aux
        s -= 1
    return text


def decToOct(text):
    return [ord(i) for i in text]


def octToBin(octal):
    binArray = []
    for o in octal:
        short = "{0:b}".format(o)
        while len(short) < 8:
            short = '0' + short
        binArray.append(short)
    return binArray


def divideEveryFive(binary):
    return [binary[i: i + 5] for i in range(0, len(binary), 5)]


def binToInt(binary):
    return [int(i, 2) for i in binary]


def base32(int26):
    return ''.join([letters[i] for i in int26])

# Decode functions


def decode(text):
    index = [letters.index(i) for i in text]
    bins = ['{0:05b}'.format(i) for i in index]
    longBinary = ''.join(bins)
    bins8 = [longBinary[i: i + 8] for i in range(0, len(longBinary), 8)]
    octal = [int(i, 2) for i in bins8]
    txt = [chr(i) for i in octal]
    return ''.join(txt[:-int(txt[-1])])


lines = int(input())
txt = [encode(input()) if i % 2 == 0 else decode(input())
       for i in range(lines)]
print(' '.join(txt))
