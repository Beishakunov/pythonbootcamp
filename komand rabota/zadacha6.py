a = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
b = []
for i in a:
    if i > 0:
        b.append(1)
    elif i < 0:
        b.append(-1)
    else:
        b.append(0)

print(a)
print(b)
