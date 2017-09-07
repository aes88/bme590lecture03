import sumfunction

def test_basicsum():
	assert sumfunction.sumfunction(2,-1)==1
	assert sumfunction.sumfunction(2,1)==3

def test_negsum():
	assert sumfunction.sumfunction(2,-3)==0
	assert sumfunction.sumfunction(3,-8)==0
	assert sumfunction.sumfunction(2,-2)==0

def test_nonnumber():
	#assert sumfunction.sumfunction(2,"2")=="error"
	assert sumfunction.sumfunction(2,"teststring")=="error"

