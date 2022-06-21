import re
import time

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


    
    '''
    gcd_list = []
    for num in range(1, n):
        gcd_list.append((num, gcd_dic[num])) 
    gcd_list.append((n, n))
    '''

def square_dic_i(n):
    square_dic = {}
    for remainder in range(n):
        square_dic[remainder] = 0
    return square_dic

def sum_g(a, b, n):
    sum_tmp = 0
    dic_tmp = square_dic_i(b**2)
    if a+b**2 > n+1:
        for index in range(a, n+1):
            dic_tmp[index % b**2] = gcd(index, b**2)
        # print(dic_tmp)
        return sum(dic_tmp.values())
    for index in range(a, a+b**2):
        dic_tmp[index % b**2] = gcd(index, b**2)
    q_a, r_a, q_n, r_n = a//b**2, a%b**2, n//b**2, n%b**2
    if r_a >= r_n : 
        sum_tmp = sum(dic_tmp.values()) * (q_n - q_a + 1)
        for index in range(r_n+1, r_a):
            sum_tmp -= dic_tmp[index]
    else :
        sum_tmp = sum(dic_tmp.values()) * (q_n - q_a)
        for index in range(r_a + 1, r_n + 1):
            sum_tmp += dic_tmp[index]
    # print(dic_tmp)
    return sum_tmp

def gcd_sum_from_i_to_n(m, n):
    #column
    sum = 0
    for i in range(m, n+1):
        sum += sum_g(i, i, n)
    return sum
    

def G(n):
    sum = 0
    for i in range(1, n+1):
        print(i)
        sum += (-1)**i * gcd_sum_from_i_to_n(i, n)
    return sum


if __name__ == '__main__':
    time_start = time.time()
    print(G(1234))
    time_end = time.time()
    print(f'time = {time_end - time_start}s')