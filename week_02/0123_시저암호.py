# 옛날에 풀었던 코드
def solution1(s, n):
    UPPER, LOWER, ALPHA = 65, 97, 26
    answer = ''
    for c in s:
        if c.isalpha():
            nowv = LOWER
            if c == c.upper(): nowv = UPPER
            c = chr((ord(c) + n - nowv) % ALPHA + nowv)
        answer += c
    return answer


# 한 줄
def solution2(s, n):
    return " ".join(map(lambda x: "".join([chr(((ord(a) + n) - ord('A')) % 26 + ord('A')) if a.isupper() else chr(((ord(a) + n) - ord('a')) % 26 + ord('a')) for a in x]), s.split(" ")))


# 한 줄 22
def solution3(s, n):
    return " ".join(map(lambda x: "".join([chr(((ord(a) + n) - ord('A' if a.isupper() else 'a')) % 26 + ord('A' if a.isupper() else 'a')) for a in x]), s.split(" ")))


# 중복 조건 lambda식
def solution3(s, n):
    check = lambda x: 'A' if x.isupper() else 'a'
    return " ".join(map(lambda x: "".join([chr(((ord(a) + n) - ord(check(a))) % 26 + ord(check(a))) for a in x]), s.split(" ")))


# lambda식 사용 22
def solution4(s, n):
    nowa = lambda x: ord('A') if x.isupper() else ord('a')
    convert = lambda x: chr(((ord(x) + n - nowa(x))) % 26 + nowa(x))
    return " ".join(map(lambda x: "".join([convert(a) for a in x]), s.split(" ")))


print(solution3("a   z A", 1))


