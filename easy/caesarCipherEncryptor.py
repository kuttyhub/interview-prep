def caesarCipherEncryptor(string, key):
    res = ""
    key = key%26
    for i in string:
        letterCode = ord(i)+key
        if letterCode<=122:
            res += chr(letterCode)
        else:
            res+= chr(96+ letterCode % 122)
    return res
string = "xyz"
key = 2
print(caesarCipherEncryptor(string,key))
