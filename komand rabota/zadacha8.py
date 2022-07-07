a = [1,0,-2,4,3,6,6,3,5,8,4,2]
c= []
for i in range(len(a) - 1):
    n = a[i]
    i += 1
    m = a[i]
    if m > n:
        c.append(m)
print(f'numbers{a}', f'результат {c}') 
