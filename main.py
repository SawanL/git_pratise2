def fib(x):
    l=[0,1]
    for i in range(2,x):
        z = l[i-1]+ l[i-2]
        l.append(z)
    return l

z=fib(10)
print(z)

def gen_fib(x):
    a=0
    b=1
    for i in range(x):
        yield a
        a=b
        b=a+b
    

for i in gen_fib(25):
    print(i)