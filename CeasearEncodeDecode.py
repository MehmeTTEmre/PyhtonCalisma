def ceasear(text,n):
    newText = ""
    for i in text:
        newChr = chr(ord(i) + n)
        newText += newChr
        
    return newText


text = input("enter a text: ")
n = int(input("enter a number: "))

encodedText = ceasear(text,n)
print(encodedText)
decodedText = ceasear(encodedText,n*-1)
print(decodedText)
