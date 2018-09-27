Python 3.4.3 (default, Nov 28 2017, 16:41:13) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> Num=[1,2,3,4,5,6,7,8,9,10]
>>> for numb in num:
	if numb == 5:
		continue
	else:
		print(num)

		
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    for numb in num:
NameError: name 'num' is not defined
>>> numb=[1,2,3,4,5,6,7,8,9,10]
>>> for num in numb:
	if num == 5:
		continue
	else:
		print(num)

		
1
2
3
4
6
7
8
9
10
>>> 
