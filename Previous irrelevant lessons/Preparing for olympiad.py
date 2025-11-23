#ex1
# lst = []
# for i in range(4):
#     i = input()
#     lst.append(int(i))
# for i in lst:
#     if i <= 1 or i >= 100 or ((lst[0] + lst[1] + lst[2]) - lst[3]) < 0:
#         i = int(input("Число не повинне бути менше 1 або більше 100 або  в Аліси входить від'ємна кількість гривень. введіть коректне число ", lst[1], ': '))
# print((lst[0] + lst[1] + lst[2]) - lst[3])
# #5 2 3 4
#
from _ast import While

#ex2
# example below, replace it with your solution
# pas = [int(i) for i in input('Enter 3 natural values: ').split()]
# ave = 0
# a = 0
# for i in pas:
#     if i > 100:
#         pas.append(int(input('Enter a new value')))
#     ave += int(i)
# ave = float((ave/len(pas)))
# print()
# if ave is not int:
#     print('IMPOSSIBLE')
#
# while pas[0] != pas[1] != pas[2]:
#     while pas[0] == pas[1] or pas[1] == pas[2] or pas[0] == pas[2]:
#         for i in pas:
#             if i == max(pas):
#                 i += 1
#             elif i == min(pas):
#                 i -= 1
#             else:
#                 continue
#     for i in pas:
#         if i == max(pas):
#             i -= 2
#         else:
#             i += 1
#     a += 1
# print(a)
# n = input()
# pas = [int(i) for i in n.split()]
# for i in pas:
#     if i > 100:
#         i = int(input('Enter a new value'))
# if sum(pas) % len(pas) != 0:
#     print('IMPOSSIBLE')
# else:
#     print(max(pas) - (sum(pas) // len(pas)))

# #ex3
# n, m = input().split()
# n = int(n)
# m = int(m)
# ai = [int(i) for i in input().split()]
# bi = [int(i) for i in input().split()]
# a = 0
# while (1 > n or n > 1000) and (1 > m or m > 1000) and (10 > sum(ai) or sum(ai) > 10000) and (10 > sum(bi) or sum(bi) > 10000):
#     if 1 > n or n > 1000:
#         n = int(input('Enter a new value of n: '))
#     elif 1 > m or m > 1000:
#         m = int(input('Enter a new value of m: '))
#     elif 10 > sum(ai) or sum(ai) > 10000:
#         for i in ai:
#             if 1 > i or i > 1000:
#                 i = int(input('Enter a new value of ai: '))
#     elif 10 > sum(bi) or sum(bi) > 10000:
#         for i in bi:
#             if 1 > i or i > 1000:
#                 i = int(input('Enter a new value of ai: '))
# while True:
#     if min(bi) >= min(ai):
#         bi.remove(min(bi))
#         ai.remove(min(ai))
#         a += 1
#     else:
#         bi.remove(min(bi))
#         print(a)
#         break

#ex4
# a, b, x, y = input().split()
# a = float(a)
# b = float(b)
# x = float(x)
# y = float(y)
# z = (100 / (a + 2 * b))
# res = z * ((a - x) + 2 * (b - y))
# if res > 51:
#     print('YES')
# else:
#     print('NO')

#ex5
# n, m = input().split()
# print(int(n) + int(m) - 2)

#ex6
# n = int(input())
# m, k = map(int, input().split())
# if (n >= 18 and m >= 2) or (n <= 18 and k >= 2):
#     print(' Yes ')
# else:
#     print( 'No ')

#ex7
# k = int(input())
# a = map(int, input().split())
# c = 0
# for i in a:
#     k -= i
#     if k >= 0:
#         c += 1
# print(c)

#ex8
# n, g, y, r = map(int, input().split())
# k = 2 * (g + y) + r
# P = ((n - 1) % k) + 1
# if P <= g:
#     print("G")
#     exit()
# P -= g
# if P <= y:
#     print("Y")
#     exit()
# P -= y
# if P <= r:
#     print("R")
#     exit()
# P -= r
# if P <= y:
#     print("Y")
#     exit()
# print("G")

#ex9
# n = int(input())
# b = [int(i) for i in input().split()]
# a = 0
# a += b[0]
# a += b[n-1]
# for i in range(n-1):
#     a += min(b[i], b[i+1])
# print(a)

#ex10
# n = int(input())
# arr_x = []
# arr_y = []
# lst_x = []
# lst_y = []
# ans = 0
# for i in range(n):
#     x, y = map(int, input().split())
#     if x not in arr_x:
#         lst_x += [x]
#     if y not in arr_y:
#         lst_y += [y]
#     arr_x += [x]
#     arr_y += [y]
# for i in lst_x:
#     if arr_x.count(i) == 3:
#         ans += 1
# for i in lst_y:
#     if arr_y.count(i) == 3:
#         ans += 1
# print(ans)

#ex11
# n, m = map(int, input().split())
# lst = [0 for i in range(n)]
# for i in range(m):
#     k, c = map(int, input().split())
#
#     z = 0
#     for j in lst:
#         if z >= k:
#             break
#         if j == 0 or lst.count(0) == 0:
#             lst[lst.index(j)] = c
#             z += 1
#         elif lst.count(0) != 0:
#             lst[lst.index(0)] = c
#             z += 1
# print(sum(lst))

#ex12
n, m, k = map(int, input().split())
obs = set()
min_obsx = n + 1
min_obsy = m + 1
if k == 0:
    print(n * m - 1)
    exit()
for i in range(k):
    x, y = map(int, input().split())
    obs.add((x, y))
    if x == 1 and y != 1:
        min_obsy = min(min_obsy, y)
    if y == 1 and x != 1:
        min_obsx = min(min_obsx, x)
max_y1 = min_obsy - 2
max_x1 = min_obsx - 2
h1 = max_y1 + max_x1
available_rows = set(range(1, max_x1 + 1))
available_cols = set(range(1, max_y1 + 1))
obs_by_row = {}
obs_by_col = {}
for x, y in obs:
        if x > 1:
            obs_by_row[x] = min(obs_by_row.get(x, m + 1), y)
        if y > 1:
            obs_by_col[y] = min(obs_by_col.get(y, n + 1), x)
h2 = set()
for x in available_rows:
    max_reachable_y = obs_by_row.get(x, m + 1) - 1
    for y in range(1, max_reachable_y + 1):
            cell = (x, y)
            if cell != (1, 1) and cell not in obs:
                if x > 1 and y > 1:
                    h2.add(cell)
for y in available_cols:
    max_reachable_x = obs_by_col.get(y, n + 1) - 1
    for x in range(1, max_reachable_x + 1):
        cell = (x, y)
        if cell != (1, 1) and cell not in obs:
            if x > 1 and y > 1:
                h2.add(cell)
h2_count = len(h2)
print(h2_count + h1)