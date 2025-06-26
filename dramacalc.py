import time
# imports necessary modules
import sys

# takes user input for the first digit
a = float(input("enter first digit: "))
print("Saving Data...")

time.sleep(2)
b = float(input("enter second: "))
print("Saving Data...")

time.sleep(1)
c = float(input("enter third: "))
print("Saving Data...")

# not neccesarily needed, just for dramatic effect cuz im bored
time.sleep(2)
print("Calculating...")
time.sleep(1.5)
print("1%")
time.sleep(1.5)
print("2%")
time.sleep(1.5)
print("3%")

# more drama
print("FATAL_SYS_CRASH 0xc0u00D6f")
f = input("Reset? Y/N?: ")

if f == 'Y':
	print("reset done")
	
if f == 'N':
	print("err_unresolved")
	sys.exit()
	
time.sleep(1.5)
print("97%")
time.sleep(1.5)
print("98%")
time.sleep(1.5)
print("99%")
time.sleep(3)
print("100%")

time.sleep(0.5)
print("done!")
time.sleep(0.75)
print(a+b+c)
