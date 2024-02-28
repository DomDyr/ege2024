for n in range(2, 2000):
    n2 = f'{n:b}'
    x = [n2[i] for i in range(len(n2)) if i % 2 == 1 and n2[i] == '1']
    y = [n2[i] for i in range(len(n2)) if i % 2 == 0 and n2[i] == '0']
    r = abs(len(x) - len(y))
    if r == 5:
        print(n)
        print(n2)
        # break
print(f'{511:b}')