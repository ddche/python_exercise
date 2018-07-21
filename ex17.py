from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("copying from {} to {}".format(from_file,to_file))

in_file = open(from_file)
indata = in_file.read()
indata1 = open(from_file).read()

print("the input file is {} bytes long".format(len(indata)))
print("does the output file exist? {}".format(exists(to_file)))
print("ready,hit return to continue, ctrl-c to abort.")
input()

out_file = open(to_file,"w")
out_file.write(indata1)

print("alright,all done.")

out_file.close()
in_file.close()

