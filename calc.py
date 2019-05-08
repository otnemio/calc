while True:
   print("Select operation.")
   print("1.Expression")
   print("2.Data Entry")
   print("3.Multiply")
   print("4.Divide")
   choice = input("Enter choice(1/2/3/4):")
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
         sum += int(eval(input()))
         if expr == "..":
            print(sum)
            break
         
