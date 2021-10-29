import itertools
import copy
stuff = [1, 2, 3,4]
import itertools
list(itertools.permutations([1, 2, 3]))
import util
import math

#corners=[(1, 1), (1, 8), (1, 16), (1, 17)]
#currentLocation=(1,6)
#corners=[(1, 2), (6,2)]
#currentLocation=(2,4)
corners=((1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3))
currentLocation=(1,1)


def manhattanDistance(position, nextPosition):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = nextPosition
    print()
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

#def costCalulator(costDict,source,corners):
#
#    if len(corners) == 0:
#        return 0
#    elif len(corners)==1:
#            return manhattanDistance(source,corners[0])
#    else:
#        if (source,tuple(corners)) in costDict.keys():
#            return costDict[(source,tuple(corners))]
#        else:
#         currentLocation=copy.deepcopy(source)
#         costs = []
#         for i in range(1,len(corners),1):
#             costs.append(costCalulator(costDict,currentLocation,corners[0:i])+
#                          manhattanDistance(corners[i-1],corners[i])+
#                          costCalulator(costDict,corners[i],corners[i+1:len(corners)]))
#             print()
#         print()
#         minCost=min(costs)
#         costDict[(source,tuple(corners))]=minCost
#         print()
#         return minCost

def costCalulator(costDict,source,corners,Min):

    stack=util.Stack()
    stack.push([source,corners])
    notDone=True
    print()
    while not stack.isEmpty() and notDone:
     arg=stack.pop()
     source=arg[0]
     corners=arg[1]
     nextArg = None
     c1=-1
     c2=-1
     cost=-1
     print()

     if not (source,tuple(corners)) in costDict.keys():
      print()

      if len(corners) == 0:
          costDict[(source,tuple(corners))]=0
          print()

      elif len(corners) == 1:
          costTemp=manhattanDistance(source, corners[0])
          costDict[(source,tuple(corners))]=costTemp
          if costTemp>Min:
              notDone=False
          print()

      else:
          #for i in range(1,len(corners),1):
        loopSource=source
        loopCorners=corners[0:len(corners)-1]
        if (loopSource, tuple(loopCorners)) in costDict.keys():
            c1=costDict[(loopSource,tuple(loopCorners))]
            if c1>Min:notDone=False
            print()
        else:
            nextArg=[loopSource,loopCorners]
            print()

        if nextArg==None:
         c2=manhattanDistance(corners[len(corners)-2],corners[len(corners)-1])
         if c2>Min:notDone=False
         cost=c1+c2
         print()

     if cost>-1:
         costDict[(source,tuple(corners))]=cost
         if cost>Min:notDone=False
         print()

     elif nextArg!=None:
          stack.push(arg)
          stack.push(nextArg)
          print()



def foodHeuristic(currentLocation,corners):
    cornersPermutations=itertools.permutations(corners)
    costDict=dict()
    costs=[]
    Min=math.inf
    for permutation in cornersPermutations:
        costCalulator(costDict,currentLocation,list(list(permutation)),Min)
        print()
    keys=list(costDict.keys())
    print()
    for i in range(len(keys)):
        if len(keys[i][1])==len(corners):
            key=keys[i]
            cost=costDict[key]
            if cost<Min:
                Min=cost

    print()
    return Min


print(foodHeuristic(currentLocation,corners))







