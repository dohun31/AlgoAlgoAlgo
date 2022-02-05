def solution(n):
    return len(check_prime(n))

def check_prime(n):
    is_prime = [True] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    
    return [prime for prime in range(2, n + 1) if is_prime[prime]]

print(solution(21))