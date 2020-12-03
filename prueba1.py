import math
pi = math.pi
x=2
z=[2]

while x<=1000:
    k = len(z)
    k1 = 0
    y1 = 1
    while k1<k:
        y2 = math.sin((pi*x)/z[k1])
        y1 = y1*y2
        k1+=1
    y = y1
    y = abs(y)
    if y>=0.00000000001:
        z.append(x)
    x+=1

print("z =")
print(z)





