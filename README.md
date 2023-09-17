## pacmanAi
This assignment is taken from https://inst.eecs.berkeley.edu/~cs188/sp22/project1/

The original code can be found at https://inst.eecs.berkeley.edu/~cs188/sp22/assets/files/search.zip

# Summary
In this project, we tried to implement different search algorithms, design a few heuristics for different problems, and design an Agent that uses a greedy algorithm to eat all the dots or foods in the maze.

Implementation of different functions and classes that were required for questions went rather smoothly, as Mahdi, a member of the team was familiar with this project beforehand, although some challenge was faced when solving question 7, as it required a strong heuristic.

The way we went about implementation was that we first designed a general search algorithm, which takes a mode as an input and depending on the mode uses a type of queue, which corresponds to one of the search algorithms. We could have implemented each search algorithm separately, which would have optimized memory consumption, considering that different algorithms have different memory requirements, but that would have caused a lot of code redundancy. 

When trying different search algorithms, it was seen that with DFS or depth-first search, parts of the mazes and states that were further from the goal state or were in paths containing dead ends were explored earlier even though it was not necessary to use these states to reach the goal. Also, the paths obtained from DFS were not the optimal paths.  

By using BFS or breath-first search, on average more states were investigated, though the paths obtained via BFS were optimal. Also, the order of state exploration in BFS is layered in such a way that the farther away we look from the starting point and closer to the goal state, the fewer states have been investigated.

In continuation, the paths produced by UCS or uniform cost search were also the optimal paths and in fact, the output produced by UCS is the same as BFS since the weight of all edges or costs from one state to a successor state is equal to 1. If the costs were more dynamic, that is the cost acted like a performance measure as well, then UCS would have produced better answers and investigated fewer states. 

Finally, In the outputs produced by A* or astar, it can be seen that the states that were closer to the starting location were investigated more, and also the investigated states are more related and closer to the optimal path to the goal state concerning the heuristic used.
Keep in mind that the way we can see the order of the states explored is via the brightness of the states, that is the brighter the state, the earlier it was explored and expanded upon, as can be seen in the picture below:

![image](https://github.com/MahdiTheGreat/pacmanAi/assets/47212121/4924118f-172c-4977-8673-1f7fb7d2fdb8)

All in all, A* had the best performance amongst the optimal search algorithms, if our performance measure is the number of states explored while trying to find the optimal answer, However depending on the problem and the application, other search algorithms may be more appropriate. For example, if there is a limitation on memory or when we are not looking for an optimal answer, especially when searching an infinite graph, DFS or iterative depth-first may be more appropriate. If having the optimal answer is important, but we can't use an informed search, as we don't know beforehand which actions we'll let us reach the goal quicker and essentially we have to use brute force to find the solution, then BFS is recommended. For example, the traveling salesman problem can be solved with BFS. Of course, if we have to use brute force and we have the cost of the actions, then UCS would be better suited. 

While A* is good and all, finding both an admissible and consistent heuristic is hard, especially in situations where the difference between an optimal answer and a non-optimal answer is negligible. This is where the greedy best-first approach comes into play, where we use a heuristic that only cares about the next step, rather than planning the entire path to the goal. The downside is that even though greedy best-first performs okay most of the time and is very quick, there is a very slim possibility that it may search the entire search tree to find an answer, which depending on the use case could be disastrous.  A good example of the usage of greedy best-first approach is the layout trickyMaze, as A* takes some time to find an optimal path, while greedy best-first method solves it pretty quickly and is a bit more reactive, even though with greedy best-first the overall cost is more.




 




