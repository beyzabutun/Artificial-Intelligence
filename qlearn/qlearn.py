
import random
from qlearnexamples import *

# The Q-Learning Algorithm

# EXERCISE ASSIGNMENT:
# Implement the Q-learning algorithm for MDPs.
#   The Q-values are represented as a Python dictionary Q[s,a],
# which is a mapping from the state indices s=0..stateMax to
# and actions a to the Q-values.
#
# Choice of actions can be completely random, or, if you are interested,
# you could implement some scheme that prefers better actions, e.g.
# based on Multi-arm Bandit problems (find more about these in the literature:
# this is an optional addition to the programming assignment.)

# OPTIONAL FUNCTIONS:
# You can implement and use the auxiliary functions bestActionFor and execute
# if you want, as auxiliary functions for Qlearning and makePolicy and makeValues.

# bestActionFor chooses the best action for 'state', given Q values

def bestActionFor(mdp,state,Q):

  lst = mdp.applicableActions(state)
  
  if lst==[]:
  	return -1
 
  #print(Q)
  bestAction=lst[0]
  val=Q[state,bestAction]
  for i in lst:
  	if val < Q[state,i]:
  		bestAction=i
  		val=Q[state,i]
  
  return bestAction

# valueOfBestAction gives the value of best action for 'state'

def valueOfBestAction(mdp,state,Q):

    best = bestActionFor(mdp,state,Q)
    if  best == -1:
    	return 0

    return Q[state, best]
# 'execute' randomly chooses a successor state for state s w.r.t. action a.
# The probability with which is given successor is chosen must respect
# to the probability given by mdp.successors(s,a).
# It returns a tuple (s2,r), where s2 is the successor state and r is
# the reward that was obtained.

def execute(mdp,s,a):

	succs=mdp.successors(s,a)
	randSuccArray = []
	randProbArray = []
	randRewArray = []
	myArray=[]
	
	for s in succs:
		randSuccArray.append(s[0])
		randProbArray.append(s[1])
		randRewArray.append(s[2])
	
	sizeA=len(randSuccArray)
	for s in range(sizeA):
		x=int(100*randProbArray[s])
		for n in range(x):
			myArray.append(randSuccArray[s])
	
	s2=random.choice(myArray)
	for i in range(sizeA):
		if randSuccArray[i]==s2:
			return (s2,randRewArray[i])
	
	#print((s2,randRewArray[i]))
	
# OBLIGATORY FUNCTION:
# Qlearning returns the Q-value function after performing the given
#   number of iterations i.e. Q-value updates.

def Qlearning(mdp,gamma,lambd,iterations):
  # The Q-values are a real-valued dictionary Q[s,a] where s is a state and a is an action.
  Q = dict()
  for s in range(mdp.stateMax+1):
  	acts = mdp.applicableActions(s)
  	for a in acts:
  		Q[s,a]=0
  s=0
  for i in range(iterations):
  	if a==-1:
  		break

  	a=random.choice(mdp.applicableActions(s))
  	sAndr = execute(mdp,s,a)
  	s2=sAndr[0]
  	r2=sAndr[1]
  	Q[s,a] = (1-lambd)*Q[s,a]+lambd*(r2 + gamma*valueOfBestAction(mdp,s2,Q))
  	s=s2
  	



  return Q

# OBLIGATORY FUNCTION:
# makePolicy constructs a policy, i.e. a mapping from state to actions,
#   given a Q-value function as produced by Qlearning.

def makePolicy(mdp,Q):
  # A policy is an action-valued dictionary P[s] where s is a state
  P = dict()
  states = [ x for x in range(0,mdp.stateMax+1)]
 
  for s in states:
    P[s] = bestActionFor(mdp,s,Q)
  
  return P


# OBLIGATORY FUNCTION:
# makeValues constructs the value function, i.e. a mapping from states to values,
#   given a Q-value function as produced by Qlearning.

def makeValues(mdp,Q):
  # A value function is a real-valued dictionary V[s] where s is a state
  V = dict()
  states = [ x for x in range(0,mdp.stateMax+1)]
  
  for s in states:
  	V[s] = valueOfBestAction(mdp,s,Q)
  
  return V
