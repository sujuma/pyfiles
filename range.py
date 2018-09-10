Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> len([])
0
>>> len("Apple")
5
>>> len([1,2,5,4,3])
5
>>> len("Apple",[23,43,2])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    len("Apple",[23,43,2])
TypeError: len() takes exactly one argument (2 given)
>>> len("A",1,2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    len("A",1,2)
TypeError: len() takes exactly one argument (3 given)
>>> len(a,2,2)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    len(a,2,2)
NameError: name 'a' is not defined
>>> 1 in [1,2,3,4]
True
>>> 7 in [2,1,2]
False
>>> S in "Sujuma"
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    S in "Sujuma"
NameError: name 'S' is not defined
>>> 'S' in 'Sujuma'
True
>>> 'u' in 'Sujuma'
True
>>> 'j' in 'Sujuma'
True
>>> 'u' in 'Sujuma'
True
>>> 'Apple' in ['Banana','mango','grapes']
False
>>> 'Apple' in ['Apple','Mango','Grapes']
True
>>> 'g' in ['gr','g','h']
True
>>> name = input("What is your name")
What is your namejohn
>>> name = input("WHat is your name")
WHat is your nameJohn
>>> name = input("What is your name ")
What is your name John
>>> print("Welcome ",name)
Welcome  John
>>> name = print("your name " name)
SyntaxError: invalid syntax
>>> name = print("Your name", name)
Your name John
>>> if A>2:
	    print("Hello")

	    
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    if A>2:
NameError: name 'A' is not defined
>>> A=4:
	
SyntaxError: invalid syntax
>>> A=4
>>> if A>2:
	    print("A is greater")

	    
A is greater
>>> A=4
>>> B=2
>>> if A>B:
	print(A," is greater than ,B)
	      
SyntaxError: EOL while scanning string literal
>>> if A>B:
	          print(A," is greater than ",B)

	      
4  is greater than  2
>>> if A>B:
	          print(A,A" is greater than B",B)
	      
SyntaxError: invalid syntax
>>> if A>B:
	          print(A,"A is greater than B",B)

	      
4 A is greater than B 2
>>> if A>B:
	      print(A," is greater than ",B)
	      elif B>A:
	      
SyntaxError: invalid syntax
>>> if A>B:
	      print(A," is greater than ",B)
    elif B>A:
	      
SyntaxError: unindent does not match any outer indentation level
>>> if A>B:
	      print(A," is greater than ",B)
    elif B>A:
	      
SyntaxError: unindent does not match any outer indentation level
>>> 
================== RESTART: C:/Users/ACER/Desktop/phy/if.py ==================
B is greater
>>> 
============== RESTART: C:/Users/ACER/Desktop/phy/palindrome.py ==============
Please enter a worddad
>>> 
============== RESTART: C:/Users/ACER/Desktop/phy/palindrome.py ==============
Please enter a worddad
Its palindrome
>>> 
============== RESTART: C:/Users/ACER/Desktop/phy/palindrome.py ==============
Please enter a wordmog
It is not
>>> 
============== RESTART: C:/Users/ACER/Desktop/phy/palindrome.py ==============
Please enter a word madam
Its palindrome
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/bool.py =================
Traceback (most recent call last):
  File "C:/Users/ACER/Desktop/phy/bool.py", line 4, in <module>
    bool(0,0)
TypeError: bool expected at most 1 arguments, got 2
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/bool.py =================
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/bool.py =================
False
False
False
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/bool.py =================
False
False
False
False
False
False
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/data.py =================
There is no data
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/try.py =================
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/try.py =================
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/try.py =================
range(0, 3)
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/try.py =================
range(5, 10)
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/try.py =================
range(2, 12, 3)
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/try.py =================
0
1
2
3
4
>>> 
================= RESTART: C:/Users/ACER/Desktop/phy/try.py =================
-1
-3
-5
-7
-9
-11
-13
>>> 
