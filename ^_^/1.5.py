def areMetaStrings(s1, s2) : 
	
	s1 = list(s1)
	s2 = list(s2)

	sim = 0

	for i in range(len(s1)):
		try:
			if s1[i] == s2[i]:
				sim += 1
		except:
			pass

	return (len(s1) + len(s2) - 2*sim) < 2

	
str1 = "pales"
str2 = "palet"
if ( areMetaStrings(str1,str2) ) : 
	print "Yes"
else: 
	print "No"