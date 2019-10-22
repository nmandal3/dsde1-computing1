import math
length = float(input("Pendulum length: "))
g = 9.81

def period(L, g) :
    T = 2*(math.pi)*((L/g)**0.5)
    print ("inside function")
    return T

def function1() :
    a = period(length, g)
    print (a)
    return

if __name__ == "__main__" :
    function1()