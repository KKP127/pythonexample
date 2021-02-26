from sys import argv
script, filename=argv

print("We are going to delete {filename}")
print("If you dont want to do that,CTL-C(^C).")
print("if you do want that hit Return")

input("?")
print("openining the file")

target = open(filename,'w')

print("Truncatinf the file.Goodbye")

target.truncate()

print("Now I am going to ask you for 3 files:")

line1=input("line 1:")
line2=input("line 2:")
line3=input("line 3:")

print("I am going to write this to file:")

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print("and finally we close it")
target.close()
