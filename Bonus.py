def gcd(a,b):
    print(f"a{a} -- b{b}")
    if b==0:
        print(f"a{a} -- b{b}")
        return a
    else:
        print(f"a{a} -- b{b}-- a%b{a%b}")
        return gcd(b,a%b)
