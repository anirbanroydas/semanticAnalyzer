#!/usr/bin/env python
# encoding: utf-8
"""
SemanticModel.py

Created by nick on 2013-04-04.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from prolog import convert,execute


D = [  
 		"RiverName",
	    "PlaceName",
	 	"StateName",
		"CountryName",
		"StateAbbrev",
		"CityName",
    	"cityid",	    
    	"countryid",               
		"placeid",	                
    	"riverid",     	                
		"stateid",	                        
		"capital",	           
		"city",                    
		"lake",	           
		"major",        
		"mountain",	          
		"place",           
		"river",          
		"state",          
		"area_1",	           
		"capital_1",          
		"capital_2",          
		"density_1",       
		"elevation_1",	
		"high_point_1",
		"high_point_2",
		"higher_2",      
		"loc_1",    
		"loc_2",    
		"longer",	   
		"lower_2",	   
		"len",	         
		"next_to_1",	
		"next_to_2",	
		"population_1",	
		"size",	         
		"traverse_1",
		"traverse_2",
		"answer",			
		"largest",			
		"largest_one",	
		"smallest",		
		"smallest_one",	
		"highest",	
		"lowest",	
		"longest",	
		"shortest",	
		"count",	
		"most",	
		"fewest"
	]
	
Lexicon = {}								#  
											#  eg :-  (1)  Lexicon["next_to"]  =  [ "borders", "next", "adjacent" ]
											#         (2)  Lexicon["CityName"]  =  [ "california", "newyorkcity", "washington d.c.", ... ]
											#         (3)  Lexicon["RiverName"]  =  [ "Mississippi", "Rio Grande", ... ]
											#

Lexicon["RiverName"]  	 =  [ ]
Lexicon["PlaceName"]  	 =  [ ]
Lexicon["StateName"]  	 =  [ ]
Lexicon["CountryName"]   =  [ ]
Lexicon["StateAbbrev"]   =  [ ]
Lexicon["CityName"]  	 =  [ ]
Lexicon["cityid"]  		 =  [ ]	    
Lexicon["countryid"]  	 =  [ ]               
Lexicon["placeid"]  	 =  [ ]                
Lexicon["riverid"]  	 =  [ ]     	                
Lexicon["stateid"]  	 =  [ ]	                        
Lexicon["capital"]  	 =  [ ]	           
Lexicon["city"]  		 =  [ ]                 
Lexicon["lake"]  		 =  [ ]	           
Lexicon["major"]  		 =  [ ]        
Lexicon["mountain"]  	 =  [ ]	          
Lexicon["place"]   		 =  [ ]        
Lexicon["river"]  		 =  [ ]          
Lexicon["state"]  	 	 =  [ ]          
Lexicon["area_1"]  		 =  [ ]	           
Lexicon["capital_1"]  	 =  [ ]         
Lexicon["capital_2"]  	 =  [ ]          
Lexicon["density_1"]     =  [ ]       
Lexicon["elevation_1"]   =  [ ]	
Lexicon["high_point_1"]  =  [ ]
Lexicon["high_point_2"]  =  [ ]
Lexicon["higher_2"]  	 =  [ ]  
Lexicon["loc_1"]  		 =  [ ] 
Lexicon["loc_2"]  		 =  [ ]    
Lexicon["longer"]  		 =  [ ]	   
Lexicon["lower_2"]  	 =  [ ]	   
Lexicon["len"]  		 =  [ ]       
Lexicon["next_to_1"]  	 =  [ ]	
Lexicon["next_to_2"]  	 =  [ ]	
Lexicon["population_1"]  =  [ ]	
Lexicon["size"]  		 =  [ ]  
Lexicon["traverse_1"]  	 =  [ ]
Lexicon["traverse_2"]  	 =  [ ]
Lexicon["answer"]  		 =  [ ]		
Lexicon["largest"]  	 =  [ ]			
Lexicon["largest_one"]   =  [ ]	        	
Lexicon["smallest"]  	 =  [ ]	
Lexicon["smallest_one"]  =  [ ]	
Lexicon["highest"]  	 =  [ ]
Lexicon["lowest"]  	 	 =  [ ]	
Lexicon["longest"]  	 =  [ ]	
Lexicon["shortest"]  	 =  [ ]	
Lexicon["count"]  		 =  [ ]	
Lexicon["most"]  		 =  [ ]
Lexicon["fewest"]  		 =  [ ]	


LC = []	





def  compute_word_span(x):   #  computes word spans of sentence x and returns a list of (constituents, grammer_symbol) pairs
	
	x=x.strip()
	depTree = dependency_Tree(x)
	x=compute_word_grammer(depTree)
	return x
	

def  dependency_Tree(x):	
	#
	#	computed the dependency tree which is the 
	#	grammer parse tree using certain predefined 
	#	grammer rules and lexicon values.
	#   
	#   It returns the complete tree with its root node
	#   as the return node from which we can access the
	#	entire dependency tree.
	#
	return tree
	
	
def  compute_word_grammer(depTree):
	#
	#	it traverses the tree (depTree) using BFS or DFS 
	#	to reach the leaves which are the
	#	constituents of sentence x whose
	#	dependency tree is depTree, and fine their parents
	#	which are the constituent's grammer symbols
	#
	#	it creates a list of (constituent, associated_grammerSymbol) pairs
	#	and return the list.
	#	let the list be l
	#
	return l
	


def  find_Log_Comp():        #  finds the logical compostion of 
	#
	#  
	#	Use W (Weight Vector) to modify the list
	#	called LC (logical compostion) everytime 
	#	by adding pairs (s,t) where s and t are 
	#	elements of D and s(t) , i.e. s is a function
	#	and t is a symbol or a function itself with its own
	# 	symbol which is defined recursively.
	#	
	#	This is can done by going throught W's (the weight vector's)
	#	z values.
	#
	#   Modifies LC
	#
	#

	
	

def  Feature1(x,c,s):		#   determines whether constituent c of sentence x has a symbol s associated with it or not.
	""" Takes input x(sentence), c (a (constituent,associted_grammerSymbol) pair) 
	and s (element of D)
	"""
	if c[1]=="preposition":
		x=x.split(' ')
		l=len(x)
		for i in range(l):
			if x[i]==c[1]:
				if i>0:
					left=x[i-1]
					right=x[i+1]
				else:
					left=''
					right=x[i+1]
				constituent=left+c[i]+right
				break
	else:
		constituent=c[0]
	
	if constituent in Lexicon[s]:
		return 1
	else:
		return 0



def  Feature2(x,c,s,d,t,dt):		#	determines whether constituents c and d are assoctiated with symbols or function s and t respectively and whether s(t) is valid or not.
	""" Takes input x(sentence), c and d ( two (constituent, associated_grammerSymbol) pairs ), 
	s and t ( two elements of D) and root node of dependency tree , dt
	"""
	norm_d= normalized_dist(c,d,dt)
	g= general_compos(s,t)
	v= feature_Learner(norm_d, g)
    return v


def  normalized_dist(node1,node2,depTree):		#	finds the normalized distance between two constituents in the dependency tree formed by the sentence x
	
	dist= calculate(depTree,node1,node2)
	if dist>0:
		return 1
	else:
		return 0


def  calculate(root, node1, node2):
	#
	#	traverses the dependency tree starting from root (root node of tree)
	#	of the dependency tree and calculates
	# 	the distance between node1 and node2 
	# 	normalized by either node1 is comes before or
	#	after node2 and by looking at their grammer symbols
	#	and considering their positions in the sentence x.
	#
	#	it returns the normalized distance
	#
	return d


def  general_compos(elem1, elem2):			#	determines how elem1 and elem2 are assciated with each other i.e. elem1(elem2) or elem2(elem1)
	
	if (elem1,elem2) in LC:
		return 1
	else:
		return 0


def  feature_Learner(norm_dist, gen_compos):
	#
	#	decides whether Feature2(x,c,s,d,t) is (+ve) or
	#	(-ve) abstractly by using W (Weight Vector) , i.e. 
	#	W's y and z values and taking into account
	#	norm_dist (i.e. the normalized distance between c and d in the dependency tree of x)
	#   and gen_compos	(i.e. the general composition of s and t ,the elements of D)
	#
	#	It returns either 1 or 0 accordingly.
	#



def  F_w(x):		#	Function to return the y(associations of x and z) and z ( the logical form or the meaningful representation of x)

	alpha={}
	beta={}
	y=[]
	z=[]
	depTree=dependency_Tree(x)
	C=compute_word_span(x)
	done_C=[]
	done_D=[]
	i=1
	for c in C:
		if c not in done_C:
			for s in D:
				if s not in done_D:
					v=Feature1(x,c,s)
					if v==1:
						alpha[i]=(c,s)
						i=i+1
						done_C.append(c)
						done_D.append(s)
	C1=alpha.values()
	i=1	
	for cs in C1:
		for dt in C1:
			if cs!=dt:
				v=Feature2(x,cs[0],cs[1],dt[0],dt[1],depTree)
				if v==1:
					beta[i]=(cs[1],dt[1])
					if beta[i] not in LC:
						LC.append(beta[i])
					i=i+1
	for k in alpha.keys():
		c=alpha[k][0][0]
		s=alpha[k][1]
		y.append((c,s))
	p=[]
	D1=[]
	for k in alpha.keys():
		D1.append(alpha[k][1])
	D1=set(D1)
	for k in beta.keys():
		p.append(beta[k][0])
	p=set(p)
	t=D1-p
	t=list(t)
	z=''
	next=''
	for k in beta.keys():
		if t==beta[k][1]:
			z=t
			next=beta[k][0]
			del beta[k]
			break
	while(1):
		for k in beta.keys():
			if next==beta[k][1]:
				z=next+"("+z+")"
				next=beta[k][0]
				del beta[k]
				break
		if beta=={}:
			break
	
	return arg_max(x,y,z)
	


def  arg_max(x,y,z):  		# 	Inference Problem solved by ILP (Integer Linear Programming)
	#	
	#	it takes as input the sentence x,
	#	the assosciation y and the logical
	#	form or the meaningful representation z.
	#	
	#	It returns a new (y,z) pair combining the 
	#	feature function's (y,z) and weight vector W
	#
	return  (y,z)
	
	

def  Feedback(x,z):			#  returns feedback regarding whether  z is a valid and appropriated meaningful representation or logical form of sentence x
	 z=convert(z)
     result=execute(z)
	 if result==response[x]:
		return 1
	else:
		return 0
		

#def  importResponse250():			#	Function to read the Response250 data
			
