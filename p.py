def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
def radiationExposure(start,stop,step):
    add=0
    while start<stop:
        add+=f(start)*step
        start+=1
    print(str(add))
    
    