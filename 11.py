# import os #for deleting

letter = 65
for i in range(26):
    file =  open(chr(letter) + ".txt", "x")
    print(chr(letter) + ".txt created" )
    file.close()
    # os.remove(chr(letter) + ".txt") #for deleting
    letter += 1