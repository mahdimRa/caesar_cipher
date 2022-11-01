from socket import AI_NUMERICHOST
import string
from unicodedata import mirrored

num_abc = {}
abc_num = {}
c = 0
for i in string.ascii_lowercase:
    c += 1
    abc_num[i] = c
    num_abc[c] = i


def betwea_0_26(numi):
    if 0 <= numi <= 26:
        return numi
    if numi > 26:
        return betwea_0_26(numi - 26)
    if numi < 0:
        return betwea_0_26(numi + 26)


def encrypt(message, shifted):
    encrypt_message = []
    for i in message:
        if i in string.ascii_lowercase:
            encrypt_message.append(num_abc[betwea_0_26(abc_num[i] + shifted)])
        else:
            encrypt_message.append(i)
    return "".join(encrypt_message)


def decript(enmessage, unshifted):
    decript_message = []
    for i in enmessage:
        if i in string.ascii_lowercase:
            decript_message.append(num_abc[betwea_0_26(abc_num[i] - unshifted)])
        else:
            decript_message.append(i)

    return "".join(decript_message)


msg = input("\n Please enter your message to encryp: ")
shifi = input("\n Please enter your shift key to encryp: ")
en = encrypt(msg, int(shifi))
print("\n Message Encrypted -->> \n \n", f"***   {en}  ***")
response = input("\n If you want to decrypt your message please type y or n: ")

if response == "y":
    print("\n Orginal message:\n", decript(en, int(shifi)))
if response == "n":
    print(";)")
