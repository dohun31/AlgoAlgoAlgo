def solution(s):
    alpha_cnt = 0
    answer = ''
    for i in range(len(s)):
        if s[i] == " ":
            answer += ' '
            alpha_cnt = 0
        else:
            answer += s[i].upper() if alpha_cnt % 2 == 0 else s[i].lower()
            alpha_cnt += 1
    return answer