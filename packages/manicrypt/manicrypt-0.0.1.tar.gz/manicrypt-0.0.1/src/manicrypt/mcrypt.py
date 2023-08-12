def mencrypt(string,key):
    enc = ''
    for letter in string:
        encletter = chr(ord(letter)+int(key))
        enc += encletter
    return enc

def mdecrypt(string,key):
    enc = ''
    for letter in string:
        encletter = chr(ord(letter)-int(key))
        enc += encletter
    return enc


