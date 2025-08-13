#Append to an existing  file called john.txt it should contain data about John wife

f = open("john.txt", "a")

f.write("\n His wife is called Jane")

f.close()