#!/bin/bash

clear
echo "Secure Overwrite Engine!"
echo ""

echo "#Documentation:" >> Secure\ Overwrite\ Engine.py
echo "#https://www.geeksforgeeks.org/how-to-open-and-close-a-file-in-python/" >> Secure\ Overwrite\ Engine.py
echo "#https://www.askpython.com/python/examples/rename-a-file-directory-python" >> Secure\ Overwrite\ Engine.py
echo "" >> Secure\ Overwrite\ Engine.py
echo "import os" >> Secure\ Overwrite\ Engine.py
echo "" >> Secure\ Overwrite\ Engine.py
echo "def secure_overwrite_engine():" >> Secure\ Overwrite\ Engine.py
echo "        #os.system(\"clear\")" >> Secure\ Overwrite\ Engine.py
echo "" >> Secure\ Overwrite\ Engine.py
echo "        #print(\"Secure Overwrite Engine\")" >> Secure\ Overwrite\ Engine.py
echo "" >> Secure\ Overwrite\ Engine.py
echo "        file = open(\"abc.abc\", \"w+\")" >> Secure\ Overwrite\ Engine.py
echo "" >> Secure\ Overwrite\ Engine.py
echo "        while True:" >> Secure\ Overwrite\ Engine.py
echo "                file.write(str(\"abc\"))" >> Secure\ Overwrite\ Engine.py
echo "" >> Secure\ Overwrite\ Engine.py
echo "        file.close()" >> Secure\ Overwrite\ Engine.py
echo "" >> Secure\ Overwrite\ Engine.py
echo "secure_overwrite_engine()" >> Secure\ Overwrite\ Engine.py

for number in {1..35}
do

clear
echo "Secure Overwrite Engine!"
echo ""

echo "Pass $number!"

python3 Secure\ Overwrite\ Engine.py

rm abc.abc

done

echo ""
echo "Done!"
