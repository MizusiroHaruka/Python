# -*- coding: utf-8 -*-
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    if aTup==():
        return ()
    else:
        return (aTup[0],)+oddTuples(aTup[2:])
        
x=()
print(oddTuples(x))


#空元组为()，而不是''单元素元组为（*,）逗号是必须的逗必