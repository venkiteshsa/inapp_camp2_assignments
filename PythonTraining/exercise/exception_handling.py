"""
#  A simple demonstration of exception handling in python
#using the try, except, finally blocks (clause)

from importlib.machinery import PathFinder


try:
    div = 4//0
except Exception as e:
    print('You are trying to divide a number by 0')
    print(f'{type(e).__name__} was occured. More details below:')
    print(e) # print the entire details of the exception
else:
    print('Division completed and result is', div)
finally:
    print('I will run whatever happens')
"""

try:
    f = open('nonexistingfile.txt')
    try:
        f.write('Hello world')
    except:
        print('Some problem with writing to the file')
    finally:
        f.close()
except:
    print('Some problem with opening the file')
