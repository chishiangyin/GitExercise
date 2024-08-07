nums=list(range(2,100000))
zhi=[]
for num in nums:
    flag=0
    temps=list(range(2,num))
    for temp in temps:
        if num%temp==0:
            flag=1
    if flag==0:
        zhi.append(num)
print(zhi)
