import itertools as it

dic=None
with open("./words.txt",'r') as dicfile:
	L=map(lambda s: s[:-1].lower(),dicfile.readlines())
	dic=set(L)


while True:
	s=input("Lettres : ")
	n=int(input("longueur du mot : "))

	combis=it.combinations(s,n)
	
	for i in combis:
		mot=''.join(i)
		
		if mot in dic:
			print(mot)

