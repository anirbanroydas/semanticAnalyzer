#!/usr/bin/env python
# encoding: utf-8
"""
SemanticModel.py

Created by nick on 2013-04-04.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os





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

# C = []


def  compute_word_span(x):   #  computes word spans of sentence x
	
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
	#	Use W (Weight Vector) to create a new list
	#	called LC (logical compostion) everytime 
	#	by adding pairs (s,t) where s and t are 
	#	elements of D and s(t) , i.e. s is a function
	#	and t is a symbol or a function itself with its own
	# 	symbol which is defined recursively.
	#	
	#	This is can done by going throught W's (the weight vector's)
	#	z values.
	#
	#   Builds LC
	#
	#
	return LC
	
	

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



def  Feature2(x,c,s,d,t):		#	determines whether constituents c and d are assoctiated with symbols or function s and t respectively and whether s(t) is valid or not.
	""" Takes input x(sentence), c and d ( two (constituent, associated_grammerSymbol) pairs ), 
	s and t ( two elements of D)
	"""
	norm_d= normalized_dist(x,c,d)
	g= general_compos(s,t)
	v= feature_Learner(norm_d, g)
    return v


def  normalized_dist(x,node1,node2):		#	finds the normalized distance between two constituents in the dependency tree formed by the sentence x
	
	dt= dependency_Tree(x)
	dist= calculate(dt,node1,node2)
	if dist>0:
		return 1
	else:
		return 0


def  calculate(root, node1, node2):
	#
	#	traverses the tree starting from the node root
	#	of the dependency tree and calculates
	# 	the distance between node1 and node2 
	# 	normalized by either node1 is a descendent or
	#	an ancester of node2.
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
	


