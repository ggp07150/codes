import time

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def gcd_func(n):
    gcd_dic = {}
    for num in range(1, n//2+1):
        gcd_dic[num] = gcd(n, num**2)
    for num_reverse in range(1, n//2+1):
        gcd_dic[n-num_reverse] = gcd_dic[num_reverse]
    gcd_list = []
    for num in range(1, n):
        gcd_list.append((num, gcd_dic[num])) 
    gcd_list.append((n, n))
    return gcd_list

def g(n):
    sum = 0
    for i in range(1, n+1):
        sum += (-1)**i * gcd_func(n)[i-1][1]
    return sum

def G(n):
    sum = 0
    for i in range(1, n+1):
        sum += g(n)
    return sum


if __name__ == '__main__':
    time_start = time.time()
    print(G(1234))
    time_end = time.time()
    print(f'time = {time_end - time_start}s')