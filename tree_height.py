# python3

import sys
import threading
import numpy as np
def compute_height(n, parents):
    depth_arr = np.zeros(n)
    check_arr = np.zeros(n)
    max_height = 0
    for i in range(n):
       height = 1
       number = parents[i-1]
       while number != -1:
        height += 1
        number = parents[number]
       if height > max_height:
           max_height = height
    # Write this function
    # Your code here
    return max_height

def main():
    text = input()
    if "I" in text:
       n = int(input("input number of nodes: "))
       values = input("input parents of nodes: ")
       stringlist = values.split()
       parents = [int(x) for x in stringlist]
       print(compute_height(n, parents))
    elif "F" in text:
       nosaukums = input()
       if "a" in nosaukums:
        print("faila nosaukums nedrīkst saturēt a burtu")
       else:
           fails = open("./test/"+nosaukums)
           n = fails.readline()
           n = int(n)
           values = fails.readline()
           stringlist = values.split()
           parents = [int(x) for x in stringlist]
           print(compute_height(n, parents))
           fails.close
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))
