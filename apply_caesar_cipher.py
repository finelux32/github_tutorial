CHAR_LOWER_A_INDEX = 97
CHAR_UPPER_A_INDEX = 65


def applyCaesarCipher(message, shift):
    resultMessage = ""
    for alphabet in message:
        if alphabet.isspace():
            resultMessage += ' '
        else:
            resultMessage += applyCaesarCipherInternal(alphabet, shift)
    print("actual = ", resultMessage)
    return resultMessage


# sub problem of applyCaesarCipher
def applyCaesarCipherInternal(alphabet, shift):
    # upper case
    if alphabet.isupper():
        # 65 - 90 => circular => mod operator
        print(ord(alphabet))
        asciiVal = ord(alphabet) - CHAR_UPPER_A_INDEX
        resultAsciiVal = ((asciiVal + shift) % 26) + CHAR_UPPER_A_INDEX
    # lower case
    else:
        asciiVal = ord(alphabet) - CHAR_LOWER_A_INDEX
        resultAsciiVal = ((asciiVal + shift) % 26) + CHAR_LOWER_A_INDEX
    return chr(resultAsciiVal)


if __name__ == '__main__':
    assert (applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert (applyCaesarCipher("zodiac", -2) == "xmbgya")
