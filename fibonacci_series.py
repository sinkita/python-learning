def fibinacci_series(n):
   f1 = 0
   f2 = 1
   print(f1)
   print(f2)
   for _ in range(n):
       f3 = f1 + f2
       f1=f2
       f2=f3
       print(f3)

fibinacci_series(10)