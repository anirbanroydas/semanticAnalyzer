import SemanticModel
import sys
import os

W=[]
response={}
feature_vector=()
S={}

def  import_TrainingData():		# it imports the Response250.txt (training data file) and reads it line by line ans store it in a list
	try:
		f=open("Response250(training).txt","r")
	except e:
		print "\nunable to open file\n"
		sys.exit(1)
	line=f.readline()
	while (line):
		if line[0]=="\n":
			n=f.readline()
			q=f.readline()
			r=f.readline()
			n=int(n)
			q=q[:-1]
			r=r[:-1]
			response[n]=(q,r)


def  initialize_weight_vector():		
	#
	#	 it initializes the weight vector with some 
	#	 initial values of (x,y,z)
	#
	return W


def initialize_working_set_S():		# initialized the B's
	for k in response.keys():
		S[k]=[]


def  structured_learner(S): 		# 	Structural Classifier
	#	
	#	It takes as input the
	#	working set of training examples (i.e S having training examples for each sentence, S is a dictionary)
	#	for all the senetences
	#   and modifies the  weight vector W.
	#
	#	It the returns the weight vecotr W
	#
	return W
	

def main():				# Main Function - Execution starts here.
	import_TrainingData()
	initialize_weight_vector()
	initialize_working_set_B()
	while True:
		stopLoop=True
		find_Log_Comp()
		for k in response.keys():
			x=response[k][1]
			y,z=F_w(x)
			f=Feedback(x,z)
			if f==1:
				feature_vector=(x,y,z)
				v=feature_vector
				temp=B[k]
				if v not in temp:
					temp.append(v)
					S[k]=temp
					stopLoop=False
		W=structured_learner(S)
		if stopLoop==True:
			break
	return W



if __name__ == '__main__':
	main() 
	


