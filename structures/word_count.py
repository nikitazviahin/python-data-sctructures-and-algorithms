with open('poem.txt', 'r') as f:
    for line in f:
        print(line)

word_count = {}
with open('poem.txt', 'r') as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n','')
            if token in word_count:
                word_count[token]+=1
            else:
                word_count[token]=1

print(word_count)