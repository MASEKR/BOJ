"""
https://www.acmicpc.net/problem/10987
"""


def is_vowel():
    vowels = ["a", "e", "i", "o", "u"]
    strings = str(input()).lower()
    cnt = 0

    for i in strings:
        if i in vowels:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(is_vowel())
