#### (p1.py) Create a function f(word) that, for a given word, returns a string of characters in which the subsequent letters of the word form the so-called Mexican Wave. Initially, the first letter of the word is capitalized and the remaining letters are lowercase. Then, the second letter of the word is capitalized and the remaining letters are lowercase, etc. Separate words with a minus sign. 
 Example:\
 f("book") returns "Book-bOok-boOk-booK"\
 f("water") returns "Water-wAter-waTer-watEr-wateR"\
 f("ok") returns "Ok-oK"\
 f("a") returns "A"\
 f("") returns ""

#### (p2.py) Create a function f(x,y,digit) that returns how many times the given digit appears in numbers in the range from x to y. 
 Example:\
 f(10,15,1) returns 7\
 f(28,32,2) returns 3\
 f(100,105,6) returns 0\
 f(100,101,0) returns 3

#### (p3.py) The uid array contains user IDs in one of the popular websites. Identifiers should be unique. Create a function f(uid) that returns true if all ids are unique. Otherwise, the function returns false. 
 Example:\
 f(["john5","ann123","JOHN5","xxx","abc333","a10"]) returns True\
 f(["abc123","ann","abc123","a10"]) returns False\
 f(["bob2","bob2"]) returns False\
 f(["bob2","BOB2"]) returns True

#### (p4.py) The prods array contains the names of the products in stock. Create a function f(fnc,prods) that maps product names to their IDs, according to the fnc function. The f function returns a comma-separated list of product IDs, with no spaces. 
 Example:\
 prods = ["water","cheese","tomato"] \
 fnc1 = lambda x: "id:"+x[:2] \
 f(fnc1,prods) returns " id:wa,id:ch,id:to"\
 fnc2 = lambda x: (x[0]+x[-1]).upper() \
 f(fnc2,prods) returns "WR,CE,TO"

#### (p5.py) A counter allows you to count any elements. Define a class C to create counters. The initial value of the counter is assigned when the object is created. The class contains the following methods:
 •	m1() - returns the counter value\
 •	m2() - increases the counter value by 1\
 •	m3() - decreases the counter value by 1\
 •	m4(n) - increases/decreases the counter value by n\
 •	\_\_str__- returns a string representation of the counter value\
   Example:\
   c=C(5)\
   c.m1() returns 5\
   c.m2()\
   c.m1() returns 6\
   c.m4(-8)\
   c.m1() returns -2\
   c.m3()\
   c.m1() returns -3\
   c.m4(10)\
   c.m1() returns 7\
   c.\_\_str__() returns "7"

#### (p6.py) Assume that a valid variable name in a computer program consists of one to five characters. The first character of a variable name must be a lowercase or uppercase letter or an underscore. The remaining characters in the variable name can be uppercase or lowercase letters, digits or the underscore character. Create a function f(vname) that returns true if the variable name vname is valid. Otherwise, the function returns false. 
 Example:\
 f("abc") returns True\
 f("Abc") returns True\
 f("aBC") returns True\
 f("_ab_c") returns True\
 f("abcdef") returns False\
 f("8abc") returns False\
 f("_aB8_") returns True\
 f("_4x") returns True

#### (p7.py) Create a function f(arr2D) that returns true when the sum of the values in at least two columns is the same. Otherwise, the function returns false. 
 Example:\
 arr = [[3,4,2],[2,2,2,0],[5,0,0,5],[4,7,0,2],[0,2,0,0]]\
 f([[3,4,2],[5,1,6]]) returns True\
 f([[3,4,2],[5,1,7]]) returns False\
 f([[3,4],[5,1],[4,7]]) returns True\
 f([[3,4],[5,9],[4,7]]) returns False

#### (p8.py) Create a function f(n) that returns the difference between the largest and smallest odd digit contained in the number n. When the number n does not contain odd digits, the function returns -1. 
 Example:\
 f(10852) returns 4\
 f(7235973) returns 6\
 f(4388) returns 0\
 f(846206) returns -1

#### (p9.py) Create a function f(x,y,d) that returns true when the string of digits d appears in any number between x and y. Otherwise, the function returns false. 
 Example:\
 f(10,15,"14") returns True\
 f(100,120,"11") returns True\
 f(205,210,"04") returns False

#### (p10.py) Flight numbers along with the number of passengers are stored in a dictionary d. Define a function f(d) that returns the number of flights in which the number of passengers is greater than the average number of passengers on all flights. 
 Example:\
 f({"LO231":150,"BA787":120,"NZ15":30}) returns 2\
 f({"LO231":150,"BA787":20,"NZ15":30}) returns 1

#### (p11.py) The res array contains test results, i.e. the number of points between 0 and 100. Create a function f(fnc,res) that filters the test results according to the criteria contained in the fnc function. The f function returns the difference between the highest and lowest test result. 
 Example:\
 res = [95,90,20,50,70]\
 fnc1 = lambda x: x>50\
 f(fnc1,res) returns 25\
 fnc2 = lambda x: x>30 and x<90\
 f(fnc2,res) returns 20

#### (p12.py) Class C describes a point (x,y) in the plane. The point coordinates are given when creating (initializing) the object. The class contains the m1() method that returns the number of the quadrant of the Cartesian system in which the point (x,y) is located ( https://en.wikipedia.org/wiki/Quadrant_(plane_geometry) ). The m1() method returns 0 if the point (x,y) is located on the X-axis or Y-axis. The class contains the m2(a,b) method that returns true when the point (x,y) is in the same quadrant of the Cartesian system as the point with coordinates a,b. Otherwise, the method returns false. The class contains the m3(a,b) method that returns true when the distance between points (x,y) and (a,b) is greater than 5. Otherwise, the method returns false. 
 Example:\
 p = C(2,3)\
 p.m1() returns 1\
 p.m2(7,4) returns True\
 p.m2(-3,1) returns False\
 p.m3(8,5) returns True\
 p.m3(4,7) returns False\
 p1 = C(0,5)\
 p1.m1() returns 0\
 p1.m2(4,7) returns False\
 p1.m2(-7,0) returns True

#### (p13.py) A valid number on the planet Metis consists of digits 1 to 7 and lowercase or uppercase letters a to d. A plus (+) or minus (-) sign may also appear at the beginning of the number. The mnumbers array contains sample numbers. Create a function f(mnumbers) that returns how many numbers in the array that are valid in the planet Metis. 
 Example:\
 f(["A15","-31","7abC","+D1","-gH"]) returns 5\
 f(["A05","-3+1","7ab8C","+D1","-22k"]) returns 1

#### (p14.py) A computer system registers all entries into the car park ("in") and exits from the car park ("out"). Define a function f(d) that for the registered data d returns an array containing the registration numbers of vehicles that remain in the car park, in alphabetical order. 
 Example:\
 cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]\
 f(cars) returns ["BA111","GX444","KR234"]\
 cars1 = [["KR234","in"],["KR234","out"]]\
 f(cars1) returns [ ]

