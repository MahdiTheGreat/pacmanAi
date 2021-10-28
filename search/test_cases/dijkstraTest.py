import itertools
import copy
stuff = [1, 2, 3,4]
import itertools
list(itertools.permutations([1, 2, 3]))

corners=[(1, 1), (1, 8), (1, 16), (1, 17)]
currentPosition=(1,6)
locations=[]


def manhattanDistance(position, nextPosition):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = nextPosition
    print()
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def costCalulator(costDict,source,corners):
    if len(corners) == 0:
        return 0
    elif len(corners)==1:
            return manhattanDistance(source,corners[0])
    else:
        if (source,tuple(corners)) in costDict.keys():
            return costDict[(source,tuple(corners))]
        else:
         currentLocation=copy.deepcopy(source)
         costs = []
         for i in range(1,len(corners),1):
             costs.append(costCalulator(costDict,currentLocation,corners[0:i])+
                          manhattanDistance(corners[i-1],corners[i])+
                          costCalulator(costDict,corners[i],corners[i+1:len(corners)]))
             print()
         print()
         minCost=min(costs)
         costDict[(source,tuple(corners))]=minCost
         print()
         return minCost

def foodHeuristic(currentLocation,corners):
    cornersPermutations=list(itertools.permutations(corners))
    costDict=dict()
    costs=[]
    paths=[]
    print()
    for i in range(len(cornersPermutations)):
        costs.append(costCalulator(costDict,currentLocation,list(corners)))
        paths.append(cornersPermutations[i])
        print()
    print()
    return min(costs)

print(foodHeuristic(currentPosition,corners))







