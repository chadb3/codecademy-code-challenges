def fizzbuzz(limit):
  # Write your code here
  for i in range(1,limit+1):
   if i%15==0:
    print("fizzbuzz")
   elif i%3==0:
    print("buzz")
   elif i%5==0:
    print("fizz")
   else:
    print(i)
   
print(fizzbuzz(16))
