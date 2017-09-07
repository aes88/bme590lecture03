def sumfunction(a,b):
	if((type(a) == str) or (type(b)==str)):
		print('error')
		return 'error';
	else:
		sum=a+b
		if(sum>0):
			print(sum)
			return sum;
		else:
			print(0)
			return 0;
