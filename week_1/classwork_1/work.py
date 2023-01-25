## Example to open a normal file in python
ccfile = open("file.txt", "r")

# data = ccfile.read()


for aline in ccfile:
    values = aline.split()

    print("In", values[0], "the average temp was", values[1] )


ccfile.close()


## Example to open file with "with"

with open('mydata.txt') as md:
    print(md)
    for line in md:
        print(line)

print(md)
