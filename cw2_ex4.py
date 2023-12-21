viginere = """
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
"""
def generate_vigenere_square():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vigenere_square = []

    for i in range(26):
        row = list(alphabet[i:] + alphabet[:i])
        vigenere_square.append(row)

    return vigenere_square
def convert_to_list_of_strings(string):
    string = string.replace(' ', '|')
    lista = ' '.join(string)
    final = []
    for i in lista:
        if i != " ":
            final.append(str(i))
    return(final)

def key_creator(message_final, keyword_final):
    key = []
    k = 0
    for i in message_final:
        key.append(keyword_final[k])
        k+=1
        if k == len(keyword_final):
            k = 0
    return key
"""
def create_viginere_list(viginere):
    # Preparing the Viginere list:
    splitted = viginere.split("\n")
    spl = []
    for s in splitted:
        spl.append(s.split(","))
    spl.pop(0)
    spl.pop(-1)
    lista = []

    for j in range(len(spl)):
        test = ' '.join(spl[j])
        for i in test:
            if i != " ":
                lista.append(str(i))

    vig_list = [[] for _ in range(26)]

    for i in range(26):
        for j in range(26):
            letter = chr((i + j) % 26 + ord('A'))
            vig_list[i].append(letter)

    return vig_list
"""
def code_algorithm(keyword, message):
    # pre steps
    keyword_final = (convert_to_list_of_strings(keyword))
    message_final = convert_to_list_of_strings(message)
    key = (key_creator(message_final, keyword_final))
    print(key)

    # algorithm
    # change the message_final for indexes
    for letter in range(len(message_final)):
        message_final[letter] = message_final[letter].upper()

    for letter in range(len(key)):
        key[letter] = key[letter].upper()

    message_numbers = [ord(letter) - ord('A') + 1 for letter in message_final if letter]
    key_numbers = [ord(letter) - ord('A') + 1 for letter in key if letter]

    p = 0
    q = 0
    crip = []
    for letter in range(len(message_final)):
        if message_final[letter].isalpha():
            crip.append(generate_vigenere_square()[key_numbers[p]-1][message_numbers[q]-1])
            p += 1
            q += 1
        else:
            crip.append(message_final[letter])
            p += 1
            q += 1

    for letter in range(len(crip)):
        if crip[letter] == '|':
            crip[letter] = crip[letter].replace('|', ' ')

    result = ' '.join(crip)

    return(result)


keyword = "lemon"
#LXFOPVEFRNHR
message = "Attack at dawn !!"
print(code_algorithm(keyword, message))


#SFB'K RAZTKI HU TQEB EDLF TOPQ!
#UIYSXNIEQ LUJ KOCL NM BTIM UIEMXCUXEHKU.

#PROGRAMMING
keyword2 = "lemon"
encripted_message = "lxfopv mh oeib !!"

def decode_algorithm(keyword_final,encrypted_message_final):
    # create decode algorithm
    keyword_final = (convert_to_list_of_strings(keyword2))
    encrypted_message_final = convert_to_list_of_strings(encripted_message)
    key = (key_creator(encrypted_message_final, keyword_final))

    for letter in range(len(encrypted_message_final)):
        encrypted_message_final[letter] = encrypted_message_final[letter].upper()

    for letter in range(len(key)):
        key[letter] = key[letter].upper()

    message_numbers = [ord(letter) - ord('A') + 1 for letter in encrypted_message_final if letter]
    key_numbers = [ord(letter) - ord('A') + 1 for letter in key if letter]
    print(message_numbers)
    print(key_numbers)
    res = []
    final=[]
    for number in range(len(message_numbers)):
        res.append((message_numbers[number]-key_numbers[number])+1)
        if res[number] < 0:
            res[number] = res[number] + 26
        final.append(chr(res[number] + 64))

    decrip = []
    p=0

    for letter in range(len(encrypted_message_final)):
        if encrypted_message_final[letter].isalpha():
            decrip.append(final[p])
            p+=1
        else:
            decrip.append(encrypted_message_final[letter])
            p+=1


    for letter in range(len(decrip)):
        if decrip[letter] == '|':
            decrip[letter] = decrip[letter].replace('|', ' ')

    result = ' '.join(decrip)
    return(result)

print(decode_algorithm(keyword2, encripted_message))
