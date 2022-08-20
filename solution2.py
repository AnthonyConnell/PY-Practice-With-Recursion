def natural_numbers(x,y):
    if x>y:
        return
    else:
        print(x)
        natural_numbers(x+1,y)

natural_numbers(1,8)