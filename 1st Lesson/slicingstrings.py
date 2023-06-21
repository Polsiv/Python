name = "Paulsiv"

first = name[0:3]
#slices 0 is the index where it beggins and 3 is the last idx it takes. [:3] works the same

lastname = name[4:]
#slices 4 is the index where it beggins then takes the last idx. [4:3] works the same

funkyname = name[0:7:2]
#2 is the numbers of steps it takes

reversename = name[::-1]
#it's just that simple

print(first + "\n" + lastname + "\n" + funkyname + "\n" + reversename)

website = "http://google.com"

sliceobj = slice(7, -4, )
#same parameters as the above, the -4 points at the last index -n jumps.

print(website[sliceobj])