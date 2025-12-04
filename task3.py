"""
Алгоритм вычисления значения функции F(n) и G(n), где n - целое число, задан следующими соотношениями:
F(n) = 2 * (G(n - 3) + 8);
G(n) = 2 * n, если n < 10;
G(n) = G(n - 2) + 1, если n >= 10.
Чему равно значение выражения F(15548)?

Формат вывода: программа должна печатать только одно число - ответ на задачу.
"""
import sys
sys.setrecursionlimit(10000000)
F_cache = {}
G_c = {}


def G(n):
    if n in G_c:
        return G_c[n]

    if n < 10:
        result = 2 * n
    else:
        result = G(n - 2) + 1

    G_c[n] = result
    return result


def F(n):
    if n in F_cache:
        return F_cache[n]

    result = 2 * (G(n - 3) + 8)
    F_cache[n] = result
    return result

print(F(15548))
