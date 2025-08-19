"""
Решение задачи о сравнении gcd(a1, a2, ..., an)! и gcd(a1!, a2!, ..., an!)
с использованием циклов для всех операций

Ключевое наблюдение: 
- Для факториалов справедливо: если x ≤ y, то gcd(x!, y!) = x!
- Поэтому gcd(a1!, a2!, ..., an!) = min(a1, a2, ..., an)!
- Условие выполняется ⟺ gcd(a1, a2, ..., an) = min(a1, a2, ..., an)
"""

def gcd(a, b):
    """Вычисление НОД двух чисел с помощью алгоритма Евклида"""
    while b:
        a, b = b, a % b
    return a

def solve():
    n = int(input())
    a = []
    
    # Считываем массив с помощью цикла
    line = input().split()
    for i in range(n):
        a.append(int(line[i]))
    
    # Находим НОД всех элементов массива с помощью цикла
    gcd_all = a[0]
    for i in range(1, n):
        gcd_all = gcd(gcd_all, a[i])
    
    # Находим минимальный элемент массива с помощью цикла
    min_element = a[0]
    for i in range(1, n):
        if a[i] < min_element:
            min_element = a[i]
    
    # Проверяем условие: gcd(a1, a2, ..., an) = min(a1, a2, ..., an)
    if gcd_all == min_element:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()