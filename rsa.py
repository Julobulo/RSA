import subprocess
# from StringToDigits import StringToDigits

Digits = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        #   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        #   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '&', 'é', ' ', '~', '"', '#', "'",
          '{', '(', '[', "-", "|", "è", "`", "_", "\\", "ç", "^", "à", "@",
          ")", "°", "]", "+", "=", "}", "¨", "$", "£", "¤", "%", "ù", "µ",
          "*", "<", ">", ",", "?", ".", ";", ":", "/", "!", "§"]

def StringToDigits(string):
    num = 0
    # check wether a the character is a letter or a digit
    def check(string):
        # return isinstance(string, int)
        try:
            float(string)
            return True
        except ValueError:
            return False
    
    # do this for all characters in the sentence to turn into digits
    for i in string:
        # if it is a digit then turn it into int because else it will be considered a letter
        if (check(i) == True): 
            i = int(i)
        # calculate the number to add using the position in the list + 10 to avoid numbers under 10
        toAdd = str(Digits.index(i.lower()) + 10)
        # if (len(toAdd) < 2):
        #     toAdd = str(0) + toAdd
        # add the toAdd val to the end of the number
        num = int(str(num) + toAdd)
    # return a number
    return num

def DigitsToString(val):
    # from list_string_digits import Digits
    num = str(val)
    # final string
    string = ""
    toAdd = 0
    for i in range (0, int(len(num) / 2)):
        # this line gets the position of the character using the two digits; -10 because at the encoding there was a +10
        toAdd = int(str(num[i*2]) + str(num[i*2+1])) - 10
        # add the value to the final string
        string = str(string) + str(Digits[toAdd])
    # return a string value
    return string


def encrypt():
    message = input("\nWhat do you want to encrypt? ")
    # turn the message into a number
    m = int(StringToDigits(message))
    print("Message to encrypt:", m)
    # Encrypt data
    print("\nPlease enter your public keys:")
    # get the public keys from the user
    e = int(input("Please enter e:")) # small number
    n = int(input("Please enter n:")) # big pseudo prime number
    # encrypt the data
    c = pow(m, e, n)
    print("\nEncrypted message:", str(c))

def decrypt():
    # get the number to decrypt from the user
    toDecrypt = int(input('What do you want to decrypt? '))
    print("\nPlease enter your private keys:")
    # get the private keys from the user
    d = int(input("Please enter d (private key): ")) # big pseudo prime number
    n = int(input("Please enter n (public key): ")) # big pseudo prime number
    # decrypt the number using the private keys
    decrypted = pow(toDecrypt, d, n)

    # print the decrypted number
    print("\nDecrypted value:", decrypted)
    # from StringToDigits import DigitsToString
    # turn the decrypted number into a string
    result = DigitsToString(decrypted)
    print("\nFinal value:", result)


print("\nDon't forget, you need public keys only to encrypt, and private keys only to decrypt!")
EncryptOrDecrypt = input("\nWhat do you want to do, encrypt or decrypt? (e/d)")

while(EncryptOrDecrypt != 'e' and EncryptOrDecrypt != 'd'):
    print("\nPlease enter a valid input!")
    EncryptOrDecrypt = input("\nWhat do you want to do, encrypt or decrypt? (e/d)")

if (EncryptOrDecrypt == 'e'):
    encrypt()
elif(EncryptOrDecrypt == 'd'):
    decrypt()