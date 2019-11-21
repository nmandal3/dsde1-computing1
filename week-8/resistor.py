'''
Resistor Class

A simple class to demonstrate how to interact with attributes and methods.


attributes: colour bands

methods: target value, min value, max value

'''

class Resistor:
    '''Resistor class representing 4 or 5 band resistors.'''
    def __init__(self, band1, band2, band3, band4, band5=None):
        self.b1 = band1.lower()
        self.b2 = band2.lower()
        self.b3 = band3.lower()
        # 4 band resistor 
        if band5 is None:
            self.tolerance = band4.lower()
            self.num_bands = 4
        # 5 band resistor
        else:
            self.b4 = band4.lower()
            self.tolerance = band5.lower()
            self.num_bands = 5


    def value(self):
        '''Returns the calculated value of the resistor in Ohms.'''
        colours = {'black': 0,
                   'brown': 1,
                   'red': 2,
                   'orange': 3,
                   'yellow': 4,
                   'green': 5,
                   'blue': 6,
                   'violet': 7,
                   'grey': 8,
                   'white': 9, 
                   'silver': 0.1,
                   'gold':0.01}
        
        # 4-band value = <band1 band2> (each a digit) x 10^band3
        if self.num_bands == 4:
            value = (colours[self.b1] * 10 + colours[self.b2]) * 10**colours[self.b3]
        
        # 5-band value = <band1 band2 band3> (each a digit) x 10^band4
        if self.num_bands == 5:
            value = (colours[self.b1] * 100 + colours[self.b2] * 10 + colours[self.b3]) * 10**colours[self.b4]
        print (value)
        return value


    def min_value(self):
        '''Return the minimum value within the tolerance of the resistor value.'''
        tol_colours = {'brown': 0.01,
                       'red': 0.02,
                       'green': 0.005,
                       'blue': 0.0025,
                       'violet': 0.001,
                       'grey': 0.0005,
                       'silver': 0.05,
                       'gold': 0.1}
        return tol_colours
    
    def max_value(self):
        '''Return the maximium value within the tolerance of the resistor value.'''
        tol_colours = {'brown': 0.01,
                       'red': 0.02,
                       'green': 0.005,
                       'blue': 0.0025,
                       'violet': 0.001,
                       'grey': 0.0005,
                       'silver': 0.05,
                       'gold': 0.1}
        return tol_colours


resistor1 = Resistor('brown', 'black', 'red', 'silver')
resistor2 = Resistor('red', 'red', 'red', 'brown', 'gold')
resistor1.value()
resistor2.value()