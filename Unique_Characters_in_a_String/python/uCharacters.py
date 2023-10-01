def unique_characters(string_in):
	cc=""
	count=0;
	if(len(string_in)>0):
	 for x in string_in:
	  for i in range(0,len(string_in)):
	   if(x==string_in[i]):
	    count+=1;
	   if(count>=2 or string_in==""):
	    return False
	  count=0
	 return True
	else:
	 return "ERROR"

print(unique_characters("apple"))
print(unique_characters("Thanks"))
print(unique_characters(""))
