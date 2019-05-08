while True:
   print("Menu\t\t..")
   print("Expression\t1")
   print("Data Entry\t2")
   choice = input("Enter choice(../1/2):")
   if choice == '1':
      while True:
         expr = input()
         if expr == "..":
            break
         print(eval(expr))
   if choice == '2':
      sum = 0
      while True:
         expr = input()
         if expr != "..":
            result = eval(expr)
            print("\t"+str(result))
            sum += result 
         else:
            print("Sum:\t"+str(sum))
            break
         
