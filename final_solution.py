"""
Решение задачи о сравнении gcd(a1, a2, ..., an)! и gcd(a1!, a2!, ..., an!)

Ключевое наблюдение: 
- Для факториалов справедливо: если x ≤ y, то gcd(x!, y!) = x!
- Поэтому gcd(a1!, a2!, ..., an!) = min(a1, a2, ..., an)!
- Условие выполняется ⟺ gcd(a1, a2, ..., an) = min(a1, a2, ..., an)
"""

import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Находим НОД всех элементов массива
    gcd_all = a[0]
    for i in range(1, n):
        gcd_all = math.gcd(gcd_all, a[i])
    
    # Находим минимальный элемент массива
    min_element = min(a)
    
    # Проверяем условие: gcd(a1, a2, ..., an) = min(a1, a2, ..., an)
    if gcd_all == min_element:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()