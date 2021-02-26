'''Now let’s do a few more things with files.
We’ll write a Python script to copy one file to another.
It’ll be very short but will give you ideas about other things you can do with files.'''

from sys import argv
from os.path import exists
'''We import another handy command named exists. This returns True if a file exists,
 based on its name in a string as an argument. It returns False if not'''

script, from_file, to_file=argv

print(f"copying from {from_file} to {to_file} file:")

# we could do this in 1 line
in_file=open(from_file)
indata=in_file.read()

print(f"the input file is {len(indata)} bytes long")
print(f"Does the output file exist:? {exists(to_file)}")
print("Hit RETURN to Continue,CTRL-C to abort ")
input()

out_file=open(to_file,'w')
out_file.write(indata)
print("Allright,All Done")

out_file.close()
in_file.close()
