sum = 0

for c in range(1, 5):
    for a in range(1, 5):
        if c != a:
            for b in range(1, 5):
                if b != a and b != c:
                    print(b+10*a+100*c)
