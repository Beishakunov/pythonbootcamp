a = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
 
even = 0
odd = 0
 
for i in a:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
 
print("Even: %d, odd: %d" % (even, odd)) 
