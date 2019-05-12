while True:
   print("Menu\t\t[..]")
   print("Expression\t[ 1]")
   print("Data Entry\t[ 2]")
   choice = input("Enter choice\t")
   if choice == '1':
      print("Enter Expression")
      while True:
         expr = input()
         if expr == "..":
            break
         print(eval(expr))
   if choice == '2':
      print("Enter Data")
      sum = 0
      while True:
         expr = input()
         if expr != "..":
            result = eval(expr)
            print("{:20.2f}".format(result))
            sum += result 
         else:
            print("--------------------")
            print("Total:"+"{:14.2f}".format(sum))
            print("--------------------")
            break