# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import treelib
from game import Directions


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def pathToGoal(tree,goalState):
    pathToLeaves = tree.paths_to_leaves()
    pathToGoal = None
    for i in range(len(pathToLeaves)):
        if goalState in pathToLeaves[i]:
            pathToGoal = pathToLeaves[i]

    pathToGoal = pathToGoal[1:len(pathToGoal)]
    pathToGoalNodes = []
    for i in range(len(pathToGoal)):
        pathToGoalNodes.append(tree.get_node(pathToGoal[i]))
    return pathToGoalNodes


def depthFirstSearch(problem):
    lifoStack=util.Stack()
    visitedStates=set()
    tree=treelib.Tree()
    reachedGoal = False
    goalState = None
    currentState = problem.getStartState()
    lifoStack.push(currentState)
    tree.create_node(currentState,currentState,parent=None,data=currentState)
    visitedStates.add(currentState)

    while not reachedGoal:
     currentState=lifoStack.pop()
     print()
     successorStates=problem.getSuccessors(currentState)
     for i in range(len(successorStates)):
         state=successorStates[i][0]
         action=successorStates[i][1]
         print()
         if  state in visitedStates:
             print()
             continue
         else:
             if problem.isGoalState(state):
                 reachedGoal=tree
                 goalState=state
             lifoStack.push(state)
             tree.create_node(state,state,currentState,action)
             visitedStates.add(state)
             print()

    pathToGoalNodes=pathToGoal(tree,goalState)
    actions=[]
    for i in range(len(pathToGoalNodes)):
     actions.append(pathToGoalNodes[i].data)

    return actions

    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """


def breadthFirstSearch(problem):
    lifoStack=util.Queue()
    visitedStates=set()
    tree=treelib.Tree()
    reachedGoal = False
    goalState = None

    currentState = problem.getStartState()
    lifoStack.push(currentState)
    tree.create_node(currentState,currentState,parent=None,data=currentState)
    visitedStates.add(currentState)

    while not reachedGoal:
     currentState=lifoStack.pop()
     print()
     successorStates=problem.getSuccessors(currentState)
     for i in range(len(successorStates)):
         state=successorStates[i][0]
         action=successorStates[i][1]
         print()
         if  state in visitedStates:
             print()
             continue
         else:
             if problem.isGoalState(state):
                 reachedGoal=tree
                 goalState=state
             lifoStack.push(state)
             tree.create_node(state,state,currentState,action)
             visitedStates.add(state)
             print()

    pathToGoalNodes = pathToGoal(tree, goalState)
    actions=[]
    for i in range(len(pathToGoalNodes)):
     actions.append(pathToGoalNodes[i].data)

    return actions


def uniformCostSearch(problem):

    lifoStack=util.PriorityQueue()
    visitedStates=set()
    tree=treelib.Tree()
    reachedGoal = False
    goalState = None

    currentState = problem.getStartState()
    lifoStack.push(currentState,-1)
    tree.create_node(currentState,currentState,parent=None,data=currentState)
    visitedStates.add(currentState)

    while not reachedGoal:
     currentState=lifoStack.pop()
     print()
     successorStates=problem.getSuccessors(currentState)
     for i in range(len(successorStates)):
         state=successorStates[i][0]
         action=successorStates[i][1]
         cost=successorStates[i][2]
         print()
         if  state in visitedStates:
             print()
             continue
         else:
             if problem.isGoalState(state):
                 reachedGoal=tree
                 goalState=state
             lifoStack.push(state,cost)
             tree.create_node(state,state,currentState,action)
             visitedStates.add(state)
             print()

    pathToGoalNodes = pathToGoal(tree, goalState)
    actions=[]
    for i in range(len(pathToGoalNodes)):
     actions.append(pathToGoalNodes[i].data)

    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
