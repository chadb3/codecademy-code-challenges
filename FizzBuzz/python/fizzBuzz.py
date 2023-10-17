def fizzbuzz(limit):
  # Write your code here
  retArr=[]
  for i in range(1,limit+1):
   if i%15==0:
    retArr.append("FizzBuzz")
   elif i%3==0:
    retArr.append("Fizz")
   elif i%5==0:
    retArr.append("Buzz")
   else:
    retArr.append(i)
  return retArr
print(fizzbuzz(16))
