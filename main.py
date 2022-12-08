
holder = open('mbox.txt')

count = {}
for line in holder:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) +1
print(count.keys())

bigcount = None
bigword = None
for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
