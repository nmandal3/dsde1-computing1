import resistor

def parallel_pair(r1, r2):
    sum = (r1.value())**(-1) + (r2.value())**(-1)
    total = 1/sum
    return total
    

#my_resistor1 = resistor.Resistor('red', 'red', 'brown', 'gold')
#my_resistor2 = resistor.Resistor('yellow', 'orange', 'black', 'silver')
#total_resistance = parallel_pair(my_resistor1, my_resistor2)
#print (total_resistance)