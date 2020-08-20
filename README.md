A Rubik's cube simulator with a set of utilities for mostly personal use. Included support for visualization, scramble generation and optimal solution generation. The 3x3 cube is solved using the CFOP method and the 2x2 cube uses a graph-theoretic approach.

<h2>Assumptions:</h2>
The cube is always positioned with white on top and orange in front. The cube is solvable, i.e. unreachable permutations like those attained by flipping a single cubie are not provided as input. The "rotate cube" refers to a 180° rotation about the F-B axis such that yellow is on top and orange is in front. The moves follow the standard convention - F, F', F2 etc. The colors are represented as 'w', 'y', 'g', 'b', 'r' and 'o'.



<h2>Usage:</h2>

<h3>cube_3x3.py:</h3>

    bash-3.2$ python3
    Python 3.8.5 (default, Jul 21 2020, 10:48:26) 
    [Clang 11.0.3 (clang-1103.0.32.62)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from cube_3x3 import Cube
    >>> cube = Cube()


Scramble + visualize + solve:

    >>> cube.randomize()
    D B2 L B L2 D R2 F2 U' F' L' D2 B2 U F L' D2 F U' L' 
    >>> cube.displayAll()
    >>> cube.solve()

    ---Cross---

    L' 
    D2 F2 
    R B' D' R2 
    R2 B R2 

    ---First layer corners---

    B D B' F' D' F 
    D2 R' D' R 
    L' D' L B' D' B 
    D2 B D' B' 

    ---Second layer---
    Rotate cube

    U F U' F' U' L' U L 
    B U' B' U' R' U R U F' U F U R U' R' 
    R' U R U B U' B' 
    U2 B' U B U L U' L' 

    ---OLL---

    U2 F U R U' R' F' 
    R U R' U R U2 R' 

    ---PLL---

    R' F R' B2 R F' R' B2 R2 
    U 
    R2 L2 D R2 L2 U R' L F2 R2 L2 B2 R' L U2 

Input specific state:

    >>> import numpy as np
    >>> cube.state['up'] = np.array([['o', 'o', 'o'], ['w', 'b', 'b'], ['g', 'r', 'b']])

Perform sequence of moves:

    >>> cube.perform(["F", "L", "U2", "B2", "R'", "D2"])
    F L U2 B2 R' D2 


<h3>cube_2x2.py:</h3>

    bash-3.2$ python3
    Python 3.8.5 (default, Jul 21 2020, 10:48:26) 
    [Clang 11.0.3 (clang-1103.0.32.62)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from cube_2x2 import Cube
    >>> c = Cube()    


Perform sequence of moves:

    >>> c.perform(["L", "F", "U2", "R", "F", "U2"])
    L F U2 R

Visualize:

    >>> c.display()
    Front
    r g
    o y

    Left
    r g
    b y

    Back
    r w
    b y

    Right
    w b
    g o

    Up
    b y
    w o

    Down
    g r
    o w

Solve:

    >>> from cube_2x2 import bfs
    >>> bfs(c, Cube())
    U2 F' R' U2 F' L' 
    2.154071807861328 seconds