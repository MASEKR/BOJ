"""
https://www.acmicpc.net/problem/1157
"""


def solution():
    strings = input().upper()
    unique_strings = list(set(strings))
    ans = [strings.count(i) for i in unique_strings]
    print(unique_strings)
    print(ans)
    if ans.count(max(ans)) > 1:
        print("?")
    else:
        print(unique_strings[ans.index(max(ans))])


if __name__ == "__main__":
    solution()