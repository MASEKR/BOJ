def postfix_eval(n, word, num_lst):
    stack = []

    for i in word:
        if 'A' <= i <= 'Z':
            stack.append(num_lst[ord(i) - ord('A')])
        else:
            str2 = stack.pop()
            str1 = stack.pop()

            if i == '+':
                stack.append(str1 + str2)
            elif i == '-':
                stack.append(str1 - str2)
            elif i == '*':
                stack.append(str1 * str2)
            elif i == '/':
                stack.append(str1 / str2)

    return stack[0]

if __name__ == "__main__":
    n = int(input())
    word = input()
    num_lst = [int(input()) for _ in range(n)]

    res = postfix_eval(n, word, num_lst)
    print('%.2f' % res)
