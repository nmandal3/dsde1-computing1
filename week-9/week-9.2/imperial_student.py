
class ImperialStudent():
    def __init__(self, name, cid):
        self.name = name
        self.cid = cid
    
    def library_check_out(self, book_availability):
        if book_availability == False:
            raise TypeError('book is not available')
        else:
            return 'book is available for loan'

student1 = ImperialStudent('Alice Gast', '12345678')

class DEStudent(ImperialStudent):
    faculty = 'Dyson School of Design Engineering'
    
    def __init__(self, name, cid, workshop_induction = False):
        self.wi = workshop_induction
    
    def ace_workshop(self, workshop_availability):
        if workshop_availability == False:
            raise TypeError('No availability at current')
        elif self.wi == False:
            raise TypeError('Student has not passed induction')
        else:
            return 'Workshop is available'

student2 = DEStudent('Misty Ayu', '01757775', True)

#print (student2.ace_workshop(True))
#print (student1.ace_workshop(True))

print (student1.library_check_out)
#print (student2.library_check_out)