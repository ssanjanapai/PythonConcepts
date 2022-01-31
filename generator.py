'''A generator is an easy way to create an iterator'''
from re import A


def remote_control():
    yield "CNN"
    yield "ESPN"
#yeild is different from return as yield preserves state 
'''anything that has to be remembered has to be "returned using yield" .'''
itr= remote_control()
next(itr)
next(itr)
for c in remote_control():
    print(c)

print("let's work on a fibonacci sequence using generator")
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for f in fib():
    if f > 100:
        break
    print(f)

'''yield generates iterators hence no use of iter() method'''
        
    