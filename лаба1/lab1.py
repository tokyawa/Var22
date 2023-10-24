import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = float(sys.argv[index])
    except:
        while(True):
            try:
                print(prompt)
                coef_str = float(input())
            except:
                continue
            break
    coef = float(coef_str)
    return coef

def append(root, result):
    if root >= 0:
        root = math.sqrt(root)
        if root == 0:
            result.append(root)
        else:
            result.append(root)
            result.append(-root)

def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        append(root1, result)
        append(root2, result)
        
    return result

def main():
    a = get_coef(1, 'Введите коэффициент перед a:')
    b = get_coef(2, 'Введите коэффициент перед b:')
    c = get_coef(3, 'Введите коэффициент перед c:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('1 корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('2 корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('3 корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('4 корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()
