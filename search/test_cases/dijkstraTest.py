import itertools
import copy
stuff = [1, 2, 3,4]
import itertools
list(itertools.permutations([1, 2, 3]))
import util

#corners=[(1, 1), (1, 8), (1, 16), (1, 17)]
#currentLocation=(1,6)
corners=[(1, 2), (6,2)]
currentLocation=(2,4)



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

def costCalulator(costDict,source,corners):

    stack=util.Stack()
    stack.push([source,corners])
    print()
    while not stack.isEmpty():
     arg=stack.pop()
     source=arg[0]
     corners=arg[1]
     print()
     costs=[]
     nextArg = None
     i=0
     c1=0
     c2=0
     c3=0
     if not (source,tuple(corners)) in costDict.keys():
      print()
      if len(corners) == 0:
          costs.append(0)
          print()
      elif len(corners) == 1:
          costs.append(manhattanDistance(source, corners[0]))
          print()
      else:
          for i in range(1,len(corners),1):
           loopSource=source
           loopCorners=corners[0:i]
           if (loopSource, tuple(loopCorners)) in costDict.keys():
               c1=costDict[(loopSource,tuple(loopCorners))]
           else:
               nextArg=[loopSource,loopCorners]
               costs=[]
               print()
               break

           loopSource=corners[i]
           loopCorners = corners[i+1:len(corners)]
           if (loopSource, tuple(loopCorners)) in costDict.keys():
               c2 = costDict[(loopSource, tuple(loopCorners))]
           else:
               nextArg = [loopSource, loopCorners]
               costs = []
               print()
               break

           c3=manhattanDistance(corners[i-1],corners[i])
           print()

           costs.append(c1+c2+c3)
           print()

     if len(costs):
         costDict[(source,tuple(corners))]=min(costs)
         print()
     elif nextArg!=None:
          stack.push(arg)
          stack.push(nextArg)
          print()



def foodHeuristic(currentLocation,corners):
    cornersPermutations=list(itertools.permutations(corners))
    costDict=dict()
    costs=[]
    for i in range(len(cornersPermutations)):
        costCalulator(costDict,currentLocation,list(cornersPermutations[i]))
    keys=list(costDict.keys())
    print()
    for i in range(len(keys)):
        if len(keys[i][1])==len(corners):
            key=keys[i]
            cost=costDict[key]
            print()
            costs.append(cost)
    print()
    return min(costs)



print(foodHeuristic(currentLocation,corners))







