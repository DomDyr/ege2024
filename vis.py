for n in range(511, 10000):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    sum_one = 0
    sum_zero = 0
    for i in range(len(s)):
        if i % 2 != 0 and s[i] == "1":
            sum_one += 1
        elif i % 2 == 0 and s[i] == "0":
            sum_zero += 1
    if abs(sum_one - sum_zero) == 5:
        print(n)
        break