import re

def trimchar(s):
	rems = ['&lt;','&gt;','&quot;']
	for st in rems:
		s=s.replace(st,' ')
	return s

def contract(s):
	cons = {"&#039;":"'", "n't":' not', "'re":' are', "'m":' am', "'ll":' will', "'ve":" have"}
	for con in cons:
		s=s.replace(con,cons[con])
	return s

def remspace(s):
	n = len(s)
	s=s.replace('  ',' ')
	if len(s) == n: 
		return s
	return remspace(s)

def remHTML(s):
	s = trimchar(s)
	left = 0
	inds=[]
	for i in range(len(s)):
		if s[i]=="<":
			left+=1
			if left == 1:
				li = i
		
		if s[i]==">":
			left -=1
			if left == 0:
				ri = i
				inds.append((li,ri))

	for l,r in reversed(inds):
		s = s[:l]+' '+s[r+1:]
	
	s = s.lower()
	s = contract(s)
	s = re.sub("http[^ ]+ "," ",s)
	s = re.sub("www[^ ]+ "," ",s)
	s = re.sub("[^a-z ]"," ",s)
	s = re.sub(' [bcdefghjklmnopqrstvwxyz] ',' ',s)
	s = remspace(s).strip()

	return s