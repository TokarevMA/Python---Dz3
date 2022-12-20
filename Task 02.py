import random
n = int(input())
some_list1 = [random.randint(-n, n) for _ in range(n)]
print(some_list1, end = '')
print(' => ',[some_list1[i] * some_list1[-1 * (1 + i)] for i in range(0, (n + 1) //2)])