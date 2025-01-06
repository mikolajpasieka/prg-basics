import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   brackets = queue.LifoQueue()
   for x  in expression:
      if x == "[" or x == "(" or x == "{":
         brackets.put(x)
      elif x == "]" or x == ")" or x == "}":
         y = brackets.get(x) + x 
         if y == "()"  or y == "[]" or y == "{}":
            continue
         else:
            brackets.put(x)    
   return brackets.empty()#True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
   print("brackets ok")
else:
   print("brackets not correct")

if brackets_ok(expression2):
  print("brackets ok")
else:
   print("brackets not correct")


if brackets_ok(expression3):
  print("brackets ok")
else:
   print("brackets not correct")