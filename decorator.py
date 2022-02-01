import time
'''to calculate performance I write the code like the following'''
def calc_square(numbers):
    start=time.time()
    result = []
    for num in numbers:
        result.append(num*num)
    end=time.time()
    print("calculate square took "+ str(end-start))
    return result

def calc_cube(numbers):
    start=time.time() #repeating 
    result = []
    for num in numbers:
        result.append(num*num*num)
    end=time.time() #repeating 
    print("calculate square took "+ str(end-start)) #repeating
    return result

array= range(1,100000)
out_square=calc_square(array)
out_cub= calc_cube(array)

'''If there were 200 functions, for each of them
 the start time ,end time and print statements 
would repeat 200 times. Here's where the decorator 
comes into picture''' #not a good coding practice

print("Using a decorator instead")

def time_it(func):
    def wrapper(*args,**kwargs):
        start= time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__+" took "+ str((end-start))+" secs")
        return result
    return wrapper
@time_it
def sq_num(numbers):
    res=[]
    for num in numbers:
        res.append(num*num)
    return res

@time_it
def cube_num(numbers):
    res=[]
    for num in numbers:
        res.append(num*num*num)
    return res

array= range(1,100000)
out_square=sq_num(array)
out_cub= cube_num(array)

'''Functions are like first class objects in Python which means
they can be used like variables and can be passed as args
to other functions'''