with open('enc.txt', 'rb') as f1:
    with open('code.txt', 'rb') as f2:
        a = bytearray(f1.read())
        b = bytearray(f2.read())
        print(len(a), len(b))
        for i in range(len(a)):
            a[i] = a[i] ^ b[i]
        print(a)
