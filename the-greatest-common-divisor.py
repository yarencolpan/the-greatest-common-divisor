def functioon(a, b):
    x = []
    for i in range(1, a+1):
        if a % i == 0:
            x.append(i)
            for z in x:
                n = []
                if b >= z and b % z == 0:
                    n.append(z)
                    v = 1
                    for d in n:
                        v *= d
    return v


while True:
    print("Press 'w' two times to exit")
    k = input("Enter the first number:")
    q = input("Enter the second number:")
    if k != "w" and q != "w":
        k = int(k)
        q = int(q)
        print("the greatest common divisors is :", functioon(k, q))
    elif k == "w" and q == "w":
        break
        
