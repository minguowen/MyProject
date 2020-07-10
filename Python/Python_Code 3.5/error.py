x = 'abc'

def fetcher(obj, index):  
    return obj[index]

def catcher():  
    try:  
        print(fetcher(x, 2))  
    except(TypeError, IndexError):  
        print("got exception")
        
    else:  
        print("not exception" )
    finally:  
        print('after fecth') 
        

catcher()
