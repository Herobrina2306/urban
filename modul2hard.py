from random import randint
n = randint(3, 21)

# n: int = 20


primes = [3, 5, 7, 11, 13, 17, 19]

password = []
print(f'n = {n}')

def opn(passw):
    p = ''
    for i in range(len(passw)):
        for j in range(2):
            p += str(passw[i][j])
    return p


if n in primes:
    for i in range(1, n // 2 + 1):
        password.append([i, n - i])
    print(f'Пароль: {opn(password)}')
else:
    if n == 4: print('Пароль: 13')
    else:
        deli = []
        for j in range(3, n):
            if n % j == 0:
                deli.append(j)
        for k in range(1, n // 2 + 1):
            for m in deli:
                if k < m - k:
                    password.append([k, m - k])
            if k < n-k:
                password.append([k, n - k])
        print(f'Пароль: {opn(password)}')

