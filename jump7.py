for a in range(1,101):
    b=a%7
    c=a%10
    if b==0 or c==7 or (70<=a<80):
        continue
    print(a)
