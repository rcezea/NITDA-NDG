#eXAMOLE 2

tup1 = ("Adamu", "NDG Developer", 1000, 2000)
print("Tuple 1: ", tup1)

tup2 =(1,2,3,4,5,6,76,5)
print("Tuple 2: ", tup2[3:])

del tup2

print("After delete")
try:
    print("Tuple 2: ", tup2[0:])
except NameError:
    print("Variabe deleted successfully")