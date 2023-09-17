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
# import treelib
from enum import Enum
from game import Directions
from dataclasses import dataclass
from typing import Any
from copy import deepcopy,copy

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
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def path_to_node(edge_dict, node):
    """this function finds a path to a node. Because of the way we have implemented the search algorithms,
    there is only one path to each unique node """
    # temp_edge_dict=deepcopy(edge_dict)
    temp_edge_dict = copy(edge_dict)
    current_node=node
    edges=[]
    while current_node in temp_edge_dict.keys():
        #temp_edge=deepcopy(temp_edge_dict[current_node])
        temp_edge = copy(temp_edge_dict[current_node])
        edges.append(temp_edge)
        parent=temp_edge.parent
        del temp_edge_dict[current_node]
        current_node=parent
    edges.reverse()
    return edges

def costToNode(edge_dict,node):
    "calculates the cost from start node or state to the current state"
    pathToNode=path_to_node(edge_dict,node)
    return sum([pathToNode[i].cost for i in range(len(pathToNode))])

class Search_alg_mode(Enum):

    dfs = 'depthFirstSearch'

    bfs = 'breadthFirstSearch'

    cs = 'costSearch'

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

@dataclass
class Edge:
    """Each edge basically acts as the transition between states"""
    parent: Any
    child: Any
    action: str
    cost: int =0

def general_search_alg(problem: SearchProblem,mode: Search_alg_mode,heuristic=nullHeuristic):
    """here we implement the general search algorithm, where it's selected mode determines if either depthFirstSearch
    ,breadthFirstSearch or uniformCostSearch is going to be performed"""
    queue=None
    """Select the type of queue based on the strategy of the algorithm to manage fringe/frontier"""
    if mode==Search_alg_mode.dfs:
        queue = util.Stack()
    elif mode==Search_alg_mode.bfs:
        queue = util.Queue()
    elif mode == Search_alg_mode.cs:
        queue = util.PriorityQueue()
    "For storing transition between different states and also not expanding on already expanded states"
    edge_dict=dict()
    goalState = None
    """Our start node"""
    current_state = problem.getStartState()
    if mode == Search_alg_mode.cs:
        queue.push(Edge(parent=None,child=current_state,action=''),0)
    else:queue.push(Edge(parent=None,child=current_state,action=''))
    
    while not queue.isEmpty():
     pass
     current_edge= queue.pop()
     current_state=current_edge.child
     if current_state in edge_dict.keys():
         """we have already expanded on this node, therefore we don't expand on it again"""
         continue
     else:
         edge_dict[current_state]=current_edge
         
     if problem.isGoalState(current_state):
         goalState = current_state
         """we have reached the goal state, therefore we break the while loop."""
         break
     successorStates = problem.getSuccessors(current_state)
     pass
     for i in range(len(successorStates)):
         state, action = successorStates[i][0], successorStates[i][1]
         if state in edge_dict.keys():
             """we have already expanded on this state"""
             continue
         else:
             edge = Edge(parent=current_state, child=state, action=action)
             if mode == Search_alg_mode.cs:
                 """the cost between transition from parent state to successor state"""
                 edgeCost = successorStates[i][2]
                 backwardsCost = costToNode(edge_dict, current_state) + edgeCost
                 heu=heuristic(state, problem)
                 pass
                 f = heu + backwardsCost
                 edge.cost=edgeCost
                 queue.push(edge, f)
             else:queue.push(edge)
    path_to_nodeNodes = path_to_node(edge_dict, goalState)
    pass
    actions=[path_to_nodeNodes[i].action for i in range(len(path_to_nodeNodes))]
    if actions:actions.remove('')
    return actions


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being ed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    return general_search_alg(problem=problem,mode=Search_alg_mode.dfs)

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    return general_search_alg(problem=problem, mode=Search_alg_mode.bfs)

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    return general_search_alg(problem=problem, mode=Search_alg_mode.cs)

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    return general_search_alg(problem=problem, mode=Search_alg_mode.cs,heuristic=heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
