with open('flag.txt', 'rb') as f1:
    with open('code.txt', 'rb') as f2:
        with open('enc.txt', 'wb') as f3:
            a = bytearray(f1.read())
            b = bytearray(f2.read())
            print(len(a), len(b))
            for i in range(len(a)):
                a[i] = a[i] ^ b[i]
            f3.write(a)
