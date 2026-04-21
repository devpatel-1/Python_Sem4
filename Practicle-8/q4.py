# Create class Hospital having attributes patient_no, patient_name and disease_name and an instance p1. Show use of methods getattr(), setattr(), delattr(), and hasattr() for p1. Display values of attributes __dict__, __doc__, __name__, __module__, __bases__ with respect to class Hospital. Delete instance p1 in the end.


class Hospital:
    """ This is Hospital Class """

    def __init__(self, patient_no, patient_name, disease_name):
        self.patient_no = patient_no
        self.patient_name = patient_name
        self.disease_name = disease_name
    
p1 = Hospital(101, "Preet Lullo", "Fever")

print("Patient Name Using getattr(): ", getattr(p1, "patient_name"))

setattr(p1, "diesease_name", "Cold")
print("Updated Diesease: ", p1.disease_name)

print("Has attribute 'patient_no'?", hasattr(p1, "patient_no"))

delattr(p1, "patient_no")
print("After deleting patient_no: ", hasattr(p1, "patient_no"))

print("\nClass Attributes: ")
print("Class __dict__: ", Hospital.__dict__)
print("Class __doc__: ", Hospital.__doc__)
print("Class __name__: ", Hospital.__name__)
print("Class __module__: ", Hospital.__module__)
print("Class __bases__: ", Hospital.__bases__)

del p1
print("\nObject p1 deleted.")