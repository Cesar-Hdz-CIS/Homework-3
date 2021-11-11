# Cesar Hernandez
# PSID 1835494

list = input()
text = list.split()

for word in text:
        freq = text.count(word)
        print(word, freq)