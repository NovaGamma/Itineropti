number = [i for i in range(20)]
text = ''
for n in number:
    text += str(n) + "|"
print(text)
print(text[:-1])
