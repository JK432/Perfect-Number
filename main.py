# Write a Python Program to check whether a given number is a perfect number or not using functions. 
def perfect(n):
  Sum = 0
  for i in range(1, n):
    if(n % i == 0):
        Sum = Sum + i
  if (Sum == n):
    return(print("perfect"))
  else:
   return(print("NOT perfect")) 


Number = int(input())
perfect(Number)


