# functions for simple char shift encription
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

# function for simple message attach to the image
def imgwrite(img, msg):
    with open(img, 'ab') as f:
        encoded_msg = msg.encode('utf-8')
        data = b" " + encoded_msg
        f.write(data)

def imgread(img):
    with open(img, 'rb') as f:
        print(f.read())

