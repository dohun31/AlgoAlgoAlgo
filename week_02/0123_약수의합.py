def solution(n):
    return sum([i + n // i if i != n // i else i for i in range(1, int(n ** 0.5) + 1) if n % i == 0])

print(solution(1))