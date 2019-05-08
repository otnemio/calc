while True:
   print("Select operation.")
   print("1.Expression")
   print("2.Data Entry")
   choice = input("Enter choice(1/2):")
   if choice == '1':
      while True:
         expr = input()
         if expr == "..":
            break
         print(eval(expr))
   if choice == '2':
      sum=0
      while True:
         expr = input()
         if expr != "..":
            sum += int(eval(expr))
         else:
            print(sum)
            break
