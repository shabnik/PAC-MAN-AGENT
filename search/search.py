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

from heapq import heappush, heappop

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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

def depthFirstSearch(problem):
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
    "*** YOUR CODE HERE ***"

    fring = util.Stack()
    visited_list = []

    #pushes the state onto the stack
    fring.push( (problem.getStartState(), []) )
    visited_list.append( problem.getStartState() )

    #goes through the fring while its not empty visiting the nodes not visited looking for goal
    #visited_list gets updates when node gets visited
    while fring.isEmpty() != 1:
        state, path = fring.pop()

        for x in problem.getSuccessors(state):
            cur_state = x[0]
            cur_step = x[1]

            while cur_state not in visited_list:
                if problem.isGoalState(cur_state):
                    final = path + [cur_step]
                    return final

                fring.push( (cur_state, path + [cur_step]) )
                visited_list.append( cur_state )

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    fring = util.Queue()
    visited_list = []

    fring.push( (problem.getStartState(), []) )

    #goes through the fring while its not empty visiting the nodes not visited looking for goal
    #visited_list gets updates when node gets visited
    while fring.isEmpty() != 1:
        state, path = fring.pop()

        for x in problem.getSuccessors(state):
            cur_state = x[0]
            cur_step = x[1]

            while cur_state not in visited_list:
                if problem.isGoalState(cur_state):
                    final = path + [cur_step]
                    return final

                fring.push( (cur_state, path + [cur_step]) )
                visited_list.append( cur_state )

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
	
    fring = [] #this will be the proirity queue
    visited_list = []

    heappush(fring, (0, (problem.getStartState(), []) ) ) #priority and getStartState are pushed into the fring
    visited_list.append( problem.getStartState() )

    while fring: #iterates until goal state found
        fring_element = heappop(fring)
        _priority, _tuple = fring_element
        state, path = _tuple

        if state not in visited_list:
            visited_list.append( state )

        if problem.isGoalState( state ):
            return path

        for x in problem.getSuccessors(state):
            cur_state = x[0]
            cur_step = x[1]

            if cur_state not in visited_list: 
                heappush(fring, (problem.getCostOfActions(path+[cur_step]), (cur_state, path + [cur_step]) ) )

    util.raiseNotDefined()

    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    

    fring = [] #this will be the proirity queue
    visited_list = []

    #will be pushed onto the heap, will get organized automatically based on the priority number
    heappush(fring, (heuristic(problem.getStartState(), problem), (problem.getStartState(), []) ) ) #priority and getStartState are pushed into the fring
    visited_list.append( problem.getStartState() )

    while fring: #iterates until goal state found
        fring_element = heappop(fring)
        _priority, _tuple = fring_element
        state, path = _tuple

        if state not in visited_list:
            visited_list.append( state )

        if problem.isGoalState( state ):
            return path

        for x in problem.getSuccessors(state):
            cur_state = x[0]
            cur_step = x[1]

            if cur_state not in visited_list: 
                heappush(fring, (problem.getCostOfActions(path+[cur_step])+heuristic(cur_state, problem), (cur_state, path + [cur_step]) ) )

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
