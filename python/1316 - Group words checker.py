n = int(input())

group_words = 0
for _ in range(n):
    word = input()
    err = 0
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            new = word[i + 1:]
            if new.count(word[i]) > 0:
                err += 1
    if err == 0:
        group_words += 1
print(group_words)
