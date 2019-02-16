import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import random

from PIL import Image
class Cube():
    faces = ['front', 'back', 'up', 'down', 'left', 'right']
    moves = 0
    def __init__(self):
        self.reset()
    def reset(self):
        self.state = {'up':np.array([['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]),
                'front':np.array([['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]),
                'left':np.array([['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]),
                'right':np.array([['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]),
                'back':np.array([['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]),
                'down':np.array([['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']])}
        self.last_scramble = None
    def disp(self, face):
        def show(color):
            if color == 'r':
                img = Image.new('RGB', (30, 30), color='red')
            elif color == 'b':
                img = Image.new('RGB', (30, 30), color='blue')
            elif color == 'g':
                img = Image.new('RGB', (30, 30), color='green')
            elif color == 'o':
                img = Image.new('RGB', (30, 30), color='orange')
            elif color == 'w':
                img = Image.new('RGB', (30, 30), color='white')
            elif color == 'y':
                img = Image.new('RGB', (30, 30), color='yellow')
            return img

        fig, ax = plt.subplots(3, 3)
        for i in range(3):
            for j in range(3):
                ax[i][j].set_xticklabels([])
                ax[i][j].set_yticklabels([])
                img = show(self.state[face][i][j])
                ax[i][j].imshow(img, interpolation='none')
        fig.suptitle(face.capitalize())
        fig.show()

    def right(self):
        temp = copy.deepcopy(self.state)
        self.state['up'][:, 2] = temp['front'][:, 2]
        self.state['front'][:, 2] = temp['down'][:, 2]
        self.state['back'][:, 0] = (temp['up'][:, 2])[::-1]
        self.state['down'][:, 2] = (temp['back'][:, 0])[::-1]
        self.state['right'][0, :] = temp['right'][:, 0][::-1]
        self.state['right'][:, 0] = temp['right'][2, :]
        self.state['right'][:, 2] = temp['right'][0, :]
        self.state['right'][2, :] = temp['right'][:, 2][::-1]


    def front(self):
        temp = copy.deepcopy(self.state)
        self.state['up'][2, :] = temp['left'][:, 2][::-1]
        self.state['left'][:, 2] = temp['down'][0, :]
        self.state['right'][:, 0] = (temp['up'][2, :])
        self.state['down'][0, :] = (temp['right'][:, 0])[::-1]
        self.state['front'][0, :] = temp['front'][:, 0][::-1]
        self.state['front'][:, 0] = temp['front'][2, :]
        self.state['front'][:, 2] = temp['front'][0, :]
        self.state['front'][2, :] = temp['front'][:, 2][::-1]

    def down(self):
        temp = copy.deepcopy(self.state)
        self.state['back'][2, :] = temp['right'][2, :]
        self.state['left'][2, :] = temp['back'][2, :]
        self.state['right'][2, :] = temp['front'][2, :]
        self.state['front'][2, :] = temp['left'][2, :]
        self.state['down'][0, :] = temp['down'][:, 0][::-1]
        self.state['down'][:, 0] = temp['down'][2, :]
        self.state['down'][:, 2] = temp['down'][0, :]
        self.state['down'][2, :] = temp['down'][:, 2][::-1]

    def up(self):
        temp = copy.deepcopy(self.state)
        self.state['back'][0, :] = temp['left'][0, :]
        self.state['left'][0, :] = temp['front'][0, :]
        self.state['right'][0, :] = temp['back'][0, :]
        self.state['front'][0, :] = temp['right'][0, :]
        self.state['up'][0, :] = temp['up'][:, 0][::-1]
        self.state['up'][:, 0] = temp['up'][2, :]
        self.state['up'][:, 2] = temp['up'][0, :]
        self.state['up'][2, :] = temp['up'][:, 2][::-1]

    def left(self):
        temp = copy.deepcopy(self.state)
        self.state['back'][:, 2] = temp['down'][:, 0][::-1]
        self.state['up'][:, 0] = temp['back'][:, 2][::-1]
        self.state['down'][:, 0] = temp['front'][:, 0]
        self.state['front'][:, 0] = temp['up'][:, 0]
        self.state['left'][0, :] = temp['left'][:, 0][::-1]
        self.state['left'][:, 0] = temp['left'][2, :]
        self.state['left'][:, 2] = temp['left'][0, :]
        self.state['left'][2, :] = temp['left'][:, 2][::-1]

    def front(self):
        temp = copy.deepcopy(self.state)
        self.state['up'][2, :] = temp['left'][:, 2][::-1]
        self.state['left'][:, 2] = temp['down'][0, :]
        self.state['right'][:, 0] = (temp['up'][2, :])
        self.state['down'][0, :] = (temp['right'][:, 0])[::-1]
        self.state['front'][0, :] = temp['front'][:, 0][::-1]
        self.state['front'][:, 0] = temp['front'][2, :]
        self.state['front'][:, 2] = temp['front'][0, :]
        self.state['front'][2, :] = temp['front'][:, 2][::-1]

    def back(self):
        temp = copy.deepcopy(self.state)
        self.state['up'][0, :] = temp['right'][:, 2]
        self.state['left'][:, 0] = temp['up'][0, :][::-1]
        self.state['right'][:, 2] = (temp['down'][2, :])[::-1]
        self.state['down'][2, :] = (temp['left'][:, 0])
        self.state['back'][0, :] = temp['back'][:, 0][::-1]
        self.state['back'][:, 0] = temp['back'][2, :]
        self.state['back'][:, 2] = temp['back'][0, :]
        self.state['back'][2, :] = temp['back'][:, 2][::-1]

    def up_down(self):
        n = copy.deepcopy(self)
        n.perform(["F2"], False)
        self.state["front"] = copy.deepcopy(n.state["front"])
        n.perform(["F2"], False)
        n.perform(["L2"], False)
        self.state["right"] = copy.deepcopy(n.state["left"])
        n.perform(["L2"], False)
        n.perform(["R2"], False)
        self.state["left"] = copy.deepcopy(n.state["right"])
        n.perform(["R2"], False)
        n.perform(["B2"], False)
        self.state["back"] = copy.deepcopy(n.state["back"])
        n.perform(["B2"], False)
        n.perform(["D2"], False)
        self.state["up"] = copy.deepcopy(n.state["down"])
        n.perform(["D2"], False)
        n.perform(["U2"], False)
        self.state["down"] = copy.deepcopy(n.state["up"])
        n.perform(["U2"], False)


    def r_prime(self):
        self.right()
        self.right()
        self.right()

    def f_prime(self):
        self.front()
        self.front()
        self.front()

    def u_prime(self):
        self.up()
        self.up()
        self.up()

    def d_prime(self):
        self.down()
        self.down()
        self.down()

    def l_prime(self):
        self.left()
        self.left()
        self.left()

    def b_prime(self):
        self.back()
        self.back()
        self.back()

    def perform(self, moves, param=True):
        for move in moves:
            if move=="R":
                self.right()
            elif move=="R2":
                self.right()
                self.right()
            elif move=="R'":
                self.r_prime()
            elif move=="L":
                self.left()
            elif move=="L2":
                self.left()
                self.left()
            elif move=="L'":
                self.l_prime()
            elif move=="F":
                self.front()
            elif move=="F2":
                self.front()
                self.front()
            elif move=="F'":
                self.f_prime()
            elif move=="U":
                self.up()
            elif move=="U2":
                self.up()
                self.up()
            elif move=="U'":
                self.u_prime()
            elif move=="D":
                self.down()
            elif move=="D2":
                self.down()
                self.down()
            elif move=="D'":
                self.d_prime()
            elif move=="B":
                self.back()
            elif move=="B2":
                self.back()
                self.back()
            elif move=="B'":
                self.b_prime()
            if param==True:
                print(move, end=" ")
        self.moves += len(moves)
        if param == True:
            print()

    def locate_edge(self, cols):
        if self.state['front'][1][2] == cols[0] and self.state['right'][1][0] == cols[1]:
            return ("front", "right")
        elif self.state['front'][1][2] == cols[1] and self.state['right'][1][0] == cols[0]:
            return ("right", "front")

        elif self.state['front'][1][0] == cols[0] and self.state['left'][1][2] == cols[1]:
            return ("front", "left")
        elif self.state['front'][1][0] == cols[1] and self.state['left'][1][2] == cols[0]:
            return ("left", "front")

        elif self.state['front'][0][1] == cols[0] and self.state['up'][2][1] == cols[1]:
            return ("front", "up")
        elif self.state['front'][0][1] == cols[1] and self.state['up'][2][1] == cols[0]:
            return ("up", "front")

        elif self.state['front'][2][1] == cols[0] and self.state['down'][0][1] == cols[1]:
            return ("front", "down")
        elif self.state['front'][2][1] == cols[1] and self.state['down'][0][1] == cols[0]:
            return ("down", "front")

        elif self.state['up'][1][2] == cols[0] and self.state['right'][0][1] == cols[1]:
            return ("up", "right")
        elif self.state['up'][1][2] == cols[1] and self.state['right'][0][1] == cols[0]:
            return ("right", "up")

        elif self.state['up'][1][0] == cols[0] and self.state['left'][0][1] == cols[1]:
            return ("up", "left")
        elif self.state['up'][1][0] == cols[1] and self.state['left'][0][1] == cols[0]:
            return ("left", "up")

        elif self.state['down'][1][2] == cols[0] and self.state['right'][2][1] == cols[1]:
            return ("down", "right")
        elif self.state['down'][1][2] == cols[1] and self.state['right'][2][1] == cols[0]:
            return ("right", "down")

        elif self.state['down'][1][0] == cols[0] and self.state['left'][2][1] == cols[1]:
            return ("down", "left")
        elif self.state['down'][1][0] == cols[1] and self.state['left'][2][1] == cols[0]:
            return ("left", "down")

        elif self.state['back'][1][2] == cols[0] and self.state['left'][1][0] == cols[1]:
            return ("back", "left")
        elif self.state['back'][1][2] == cols[1] and self.state['left'][1][0] == cols[0]:
            return ("left", "back")

        elif self.state['back'][1][0] == cols[0] and self.state['right'][1][2] == cols[1]:
            return ("back", "right")
        elif self.state['back'][1][0] == cols[1] and self.state['right'][1][2] == cols[0]:
            return ("right", "back")

        elif self.state['back'][0][1] == cols[0] and self.state['up'][0][1] == cols[1]:
            return ("back", "up")
        elif self.state['back'][0][1] == cols[1] and self.state['up'][0][1] == cols[0]:
            return ("up", "back")

        elif self.state['back'][2][1] == cols[0] and self.state['down'][2][1] == cols[1]:
            return ("back", "down")
        elif self.state['back'][2][1] == cols[1] and self.state['down'][2][1] == cols[0]:
            return ("down", "back")

    def randomize(self):
        def opp(x):
            if x == 'F':
                return 'B'
            if x == 'B':
                return 'F'
            if x == 'R':
                return 'L'
            if x == 'L':
                return 'R'
            if x == 'U':
                return 'D'
            if x == 'D':
                return 'U'

        scramble = []
        moves = ['R', 'L', 'U', 'D', 'F', 'B', 'R2', "R'", 'L2', "L'", 'U2', "U'", 'D2', "D'", 'F2', "F'", 'B2', "B'"]
        for i in range(20):
            x = random.randint(0, 17)
            if not scramble:
                scramble.append(moves[x])
            else:
                while ((scramble[i-1][0] == moves[x][0]) or (scramble[i-1][0] == opp(moves[x][0]))):
                    x = random.randint(0, 17)
                scramble.append(moves[x])
        self.perform(scramble)
        self.moves -= 20
        self.last_scramble = scramble

    def cross(self):
        self.moves = 0
        def solve_w_b():
            pos = self.locate_edge(('w', 'b'))
            if pos == ("front", "right"):
                self.perform(["F2", "L'"])
            elif pos == ("right", "front"):
                self.perform(["F'", "U"])
            elif pos == ("front", "left"):
                self.perform(["L'"])
            elif pos == ("left", "front"):
                self.perform(["F", "U"])
            elif pos == ("back", "right"):
                self.perform(["R'", "U2"])
            elif pos == ("right", "back"):
                self.perform(["B", "U'"])
            elif pos == ("back", "left"):
                self.perform(["L"])
            elif pos == ("left", "back"):
                self.perform(["B'", "U'"])
            elif pos == ("down", "left"):
                self.perform(["L2"])
            elif pos == ("left", "down"):
                self.perform(["L'", "F", "U"])
            elif pos == ("down", "front"):
                self.perform(["D'", "L2"])
            elif pos == ("front", "down"):
                self.perform(["F", "L'"])
            elif pos == ("down", "right"):
                self.perform(["D2", "L2"])
            elif pos == ("right", "down"):
                self.perform(["D'", "F", "L'"])
            elif pos == ("down", "back"):
                self.perform(["D", "L2"])
            elif pos == ("back", "down"):
                self.perform(["B'", "L"])
            elif pos == ("up", "back"):
                self.perform(["U'"])
            elif pos == ("back", "up"):
                self.perform(["B", "L"])
            elif pos == ("up", "right"):
                self.perform(["U2"])
            elif pos == ("right", "up"):
                self.perform(["R'", "F'", "U"])
            elif pos == ("up", "front"):
                self.perform(["U"])
            elif pos == ("front", "up"):
                self.perform(["F'", "L'"])
            elif pos == ("left", "up"):
                self.perform(["L", "F'", "D'", "L2"])
        def solve_w_o():
            pos = self.locate_edge(('w', 'o'))
            if pos == ("front", "right"):
                self.perform(["R'", "D'", "F2"])
            elif pos == ("right", "front"):
                self.perform(["F'"])
            elif pos == ("front", "left"):
                self.perform(["F'", "D", "R", "F'"])
            elif pos == ("left", "front"):
                self.perform(["F"])
            elif pos == ("back", "right"):
                self.perform(["R", "D'", "F2"])
            elif pos == ("right", "back"):
                self.perform(["R2", "F'"])
            elif pos == ("back", "left"):
                self.perform(["L'", "D", "F2", "L"])
            elif pos == ("left", "back"):
                self.perform(["L2", "F", "L2"])
            elif pos == ("down", "left"):
                self.perform(["D", "F2"])
            elif pos == ("left", "down"):
                self.perform(["L'", "F", "L"])
            elif pos == ("down", "front"):
                self.perform(["F2"])
            elif pos == ("front", "down"):
                self.perform(["D", "R", "F'"])
            elif pos == ("down", "right"):
                self.perform(["D'", "F2"])
            elif pos == ("right", "down"):
                self.perform(["R", "F'"])
            elif pos == ("down", "back"):
                self.perform(["D2", "F2"])
            elif pos == ("back", "down"):
                self.perform(["D'", "R", "F'"])
            elif pos == ("up", "back"):
                self.perform(["B2", "D2", "F2"])
            elif pos == ("back", "up"):
                self.perform(["B'", "R", "D'", "F2"])
            elif pos == ("up", "right"):
                self.perform(["R2", "D'", "F2"])
            elif pos == ("right", "up"):
                self.perform(["R'", "F'"])
            elif pos == ("front", "up"):
                self.perform(["F", "R'", "D'", "F2"])
        def solve_w_g():
            pos = self.locate_edge(('w', 'g'))
            if pos == ("front", "right"):
                self.perform(["R"])
            elif pos == ("right", "front"):
                self.perform(["R'", "D'", "F'", "R", "F"])
            elif pos == ("front", "left"):
                self.perform(["L", "D2", "R2", "L'"])
            elif pos == ("left", "front"):
                self.perform(["F'", "D", "R2", "F"])
            elif pos == ("back", "right"):
                self.perform(["R'"])
            elif pos == ("right", "back"):
                self.perform(["R", "D'", "F'", "R", "F"])
            elif pos == ("back", "left"):
                self.perform(["B2", "R'"])
            elif pos == ("left", "back"):
                self.perform(["B", "D'", "R2"])
            elif pos == ("down", "left"):
                self.perform(["D2", "R2"])
            elif pos == ("left", "down"):
                self.perform(["D'", "B", "R'"])
            elif pos == ("down", "front"):
                self.perform(["D", "R2"])
            elif pos == ("front", "down"):
                self.perform(["F'", "R", "F"])
            elif pos == ("down", "right"):
                self.perform(["R2"])
            elif pos == ("right", "down"):
                self.perform(["D", "B", "R'"])
            elif pos == ("down", "back"):
                self.perform(["D'", "R2"])
            elif pos == ("back", "down"):
                self.perform(["B", "R'"])
            elif pos == ("up", "back"):
                self.perform(["B2", "D'", "R2"])
            elif pos == ("back", "up"):
                self.perform(["B'", "R'"])
            elif pos == ("right", "up"):
                self.perform(["R", "B'", "D'", "R2"])
        def solve_w_r():
            pos = self.locate_edge(('w', 'r'))
            if pos == ("front", "right"):
                self.perform(["R'", "D", "B2", "R"])
            elif pos == ("right", "front"):
                self.perform(["R2", "B", "R2"])
            elif pos == ("front", "left"):
                self.perform(["L", "D'", "L'", "B2"])
            elif pos == ("left", "front"):
                self.perform(["F'", "D2", "F", "B2"])
            elif pos == ("back", "right"):
                self.perform(["R", "D", "R'", "B2"])
            elif pos == ("right", "back"):
                self.perform(["B"])
            elif pos == ("back", "left"):
                self.perform(["L'", "D'", "L", "B2"])
            elif pos == ("left", "back"):
                self.perform(["B'"])
            elif pos == ("down", "left"):
                self.perform(["D'", "B2"])
            elif pos == ("left", "down"):
                self.perform(["L", "B'", "L'"])
            elif pos == ("down", "front"):
                self.perform(["D2", "B2"])
            elif pos == ("front", "down"):
                self.perform(["D", "R'", "B", "R"])
            elif pos == ("down", "right"):
                self.perform(["D", "B2"])
            elif pos == ("right", "down"):
                self.perform(["R'", "B", "R"])
            elif pos == ("down", "back"):
                self.perform(["B2"])
            elif pos == ("back", "down"):
                self.perform(["D'", "R'", "B", "R"])
            elif pos == ("back", "up"):
                self.perform(["B'", "R", "D", "R'", "B2"])
        solve_w_b()
        solve_w_o()
        solve_w_g()
        solve_w_r()

    def verify_cross(self):
        return self.locate_edge(("w", "o")) == ("up", "front") and self.locate_edge(("w", "g")) == ("up", "right") and self.locate_edge(("w", "r")) == ("up", "back") and self.locate_edge(("w", "b")) == ("up", "left")

    def first_layer_corners(self):
        def solve_w_o_b():
            if self.state["front"][0][0] == 'w' and self.state["left"][0][2] == 'o' and self.state["up"][2][0] == 'b':
                self.perform(["F'", "D'", "F", "D", "F'", "D'", "F"])
            elif self.state["front"][0][0] == 'b' and self.state["left"][0][2] == 'w' and self.state["up"][2][0] == 'o':
                self.perform(["L", "D", "L'", "D'", "L", "D", "L'"])
            elif self.state["front"][0][2] == 'w' and self.state["right"][0][0] == 'b' and self.state["up"][2][2] == 'o':
                self.perform(["F", "D", "F'", "D", "F'", "D", "F"])
            elif self.state["front"][0][2] == 'o' and self.state["right"][0][0] == 'w' and self.state["up"][2][2] == 'b':
                self.perform(["R'", "L", "D'", "L'", "R"])
            elif self.state["front"][0][2] == 'b' and self.state["right"][0][0] == 'o' and self.state["up"][2][2] == 'w':
                self.perform(["R'", "D2", "R", "F'", "D", "F"])
            elif self.state["up"][0][2] == 'o' and self.state["right"][0][2] == 'w' and self.state["back"][0][0] == 'b':
                self.perform(["B'", "D2", "B", "F'", "D2", "F", "D", "F'", "D'", "F"])
            elif self.state["up"][0][2] == 'w' and self.state["right"][0][2] == 'b' and self.state["back"][0][0] == 'o':
                self.perform(["B'", "D2", "B", "L", "D", "L'"])
            elif self.state["up"][0][2] == 'b' and self.state["right"][0][2] == 'o' and self.state["back"][0][0] == 'w':
                self.perform(["B'", "D'", "B", "L", "D'", "L'"])
            elif self.state["up"][0][0] == 'o' and self.state["left"][0][0] == 'b' and self.state["back"][0][2] == 'w':
                self.perform(["B", "F'", "D", "F", "B'"])
            elif self.state["up"][0][0] == 'b' and self.state["left"][0][0] == 'w' and self.state["back"][0][2] == 'o':
                self.perform(["L'", "D", "F'", "D'", "F2", "L", "F'"])
            elif self.state["up"][0][0] == 'w' and self.state["left"][0][0] == 'o' and self.state["back"][0][2] == 'b':
                self.perform(["B", "D", "B'", "F'", "D'", "F"])
            elif self.state["front"][2][0] == 'o' and self.state["left"][2][2] == 'w' and self.state["down"][0][0] == 'b':
                self.perform(["D'", "F'", "D", "F"])
            elif self.state["front"][2][0] == 'w' and self.state["left"][2][2] == 'b' and self.state["down"][0][0] == 'o':
                self.perform(["F'", "D'", "F"])
            elif self.state["front"][2][0] == 'b' and self.state["left"][2][2] == 'o' and self.state["down"][0][0] == 'w':
                self.perform(["F'", "D2", "F", "D", "F'", "D'", "F"])
            elif self.state["front"][2][2] == 'w' and self.state["right"][2][0] == 'o' and self.state["down"][0][2] == 'b':
                self.perform(["D2", "F'", "D", "F"])
            elif self.state["front"][2][2] == 'o' and self.state["right"][2][0] == 'b' and self.state["down"][0][2] == 'w':
                self.perform(["R'", "D2", "R", "F'", "D'", "F"])
            elif self.state["front"][2][2] == 'b' and self.state["right"][2][0] == 'w' and self.state["down"][0][2] == 'o':
                self.perform(["L", "D'", "L'"])
            elif self.state["right"][2][2] == 'b' and self.state["down"][2][2] == 'o' and self.state["back"][2][0] == 'w':
                self.perform(["L", "D2", "L'"])
            elif self.state["right"][2][2] == 'w' and self.state["down"][2][2] == 'b' and self.state["back"][2][0] == 'o':
                self.perform(["F'", "D2", "F"])
            elif self.state["right"][2][2] == 'o' and self.state["down"][2][2] == 'w' and self.state["back"][2][0] == 'b':
                self.perform(["D2", "F'", "D2", "F", "D", "F'", "D'", "F"])
            elif self.state["left"][2][0] == 'o' and self.state["down"][2][0] == 'b' and self.state["back"][2][2] == 'w':
                self.perform(["F'", "D", "F"])
            elif self.state["left"][2][0] == 'w' and self.state["down"][2][0] == 'o' and self.state["back"][2][2] == 'b':
                self.perform(["D", "F'", "D'", "F"])
            elif self.state["left"][2][0] == 'b' and self.state["down"][2][0] == 'w' and self.state["back"][2][2] == 'o':
                self.perform(["D", "F'", "D2", "F", "D", "F'", "D'", "F"])

        def solve_w_o_g():
            if self.state["front"][0][2] == 'w' and self.state["right"][0][0] == 'o' and self.state["up"][2][2] == 'g':
                self.perform(["R'", "D", "R", "D'", "R'", "D", "R"])
            elif self.state["front"][0][2] == 'g' and self.state["right"][0][0] == 'w' and self.state["up"][2][2] == 'o':
                self.perform(["R'", "D'", "R", "D", "R'", "D'", "R"])

            elif self.state["up"][0][2] == 'g' and self.state["right"][0][2] == 'w' and self.state["back"][0][0] == 'o':
                self.perform(["R", "D2", "R2", "D", "R"])
            elif self.state["up"][0][2] == 'o' and self.state["right"][0][2] == 'g' and self.state["back"][0][0] == 'w':
                self.perform(["B'", "D'", "B", "R'", "D'", "R"])
            elif self.state["up"][0][2] == 'w' and self.state["right"][0][2] == 'o' and self.state["back"][0][0] == 'g':
                self.perform(["B'", "D2", "B", "R'", "D", "R"])

            elif self.state["up"][0][0] == 'g' and self.state["left"][0][0] == 'o' and self.state["back"][0][2] == 'w':
                self.perform(["B", "D", "B'", "R'", "D", "R"])
            elif self.state["up"][0][0] == 'o' and self.state["left"][0][0] == 'w' and self.state["back"][0][2] == 'g':
                self.perform(["L'", "D2", "L", "R'", "D'", "R"])
            elif self.state["up"][0][0] == 'w' and self.state["left"][0][0] == 'g' and self.state["back"][0][2] == 'o':
                self.perform(["L'", "R'", "D2", "R", "L"])

            elif self.state["front"][2][0] == 'g' and self.state["left"][2][2] == 'w' and self.state["down"][0][0] == 'o':
                self.perform(["R'", "D", "R"])
            elif self.state["front"][2][0] == 'w' and self.state["left"][2][2] == 'o' and self.state["down"][0][0] == 'g':
                self.perform(["D", "R'", "D'", "R"])
            elif self.state["front"][2][0] == 'o' and self.state["left"][2][2] == 'g' and self.state["down"][0][0] == 'w':
                self.perform(["D", "R'", "D2", "R", "D", "R'", "D'", "R"])

            elif self.state["front"][2][2] == 'w' and self.state["right"][2][0] == 'g' and self.state["down"][0][2] == 'o':
                self.perform(["D'", "R'", "D", "R"])
            elif self.state["front"][2][2] == 'o' and self.state["right"][2][0] == 'w' and self.state["down"][0][2] == 'g':
                self.perform(["R'", "D'", "R"])
            elif self.state["front"][2][2] == 'g' and self.state["right"][2][0] == 'o' and self.state["down"][0][2] == 'w':
                self.perform(["R'", "D2", "R", "D", "R'", "D'", "R"])

            elif self.state["right"][2][2] == 'w' and self.state["down"][2][2] == 'o' and self.state["back"][2][0] == 'g':
                self.perform(["D2", "R'", "D", "R"])
            elif self.state["right"][2][2] == 'o' and self.state["down"][2][2] == 'g' and self.state["back"][2][0] == 'w':
                self.perform(["D'", "R'", "D'", "R"])
            elif self.state["right"][2][2] == 'g' and self.state["down"][2][2] == 'w' and self.state["back"][2][0] == 'o':
                self.perform(["D'", "R'", "D2", "R", "D", "R'", "D'", "R"])

            elif self.state["left"][2][0] == 'g' and self.state["down"][2][0] == 'o' and self.state["back"][2][2] == 'w':
                self.perform(["R'", "D2", "R"])
            elif self.state["left"][2][0] == 'w' and self.state["down"][2][0] == 'g' and self.state["back"][2][2] == 'o':
                self.perform(["D2", "R'", "D'", "R"])
            elif self.state["left"][2][0] == 'o' and self.state["down"][2][0] == 'w' and self.state["back"][2][2] == 'g':
                self.perform(["D2", "R'", "D2", "R", "D", "R'", "D'", "R"])

        def solve_w_r_g():
            if self.state["up"][0][2] == 'r' and self.state["right"][0][2] == 'w' and self.state["back"][0][0] == 'g':
                self.perform(["R", "D", "R'", "D2", "B'", "D", "B"])
            elif self.state["up"][0][2] == 'g' and self.state["right"][0][2] == 'r' and self.state["back"][0][0] == 'w':
                self.perform(["B'", "D'", "B", "D", "B'", "D'", "B"])

            elif self.state["up"][0][0] == 'r' and self.state["left"][0][0] == 'g' and self.state["back"][0][2] == 'w':
                self.perform(["B", "D2", "B2", "D", "B"])
            elif self.state["up"][0][0] == 'g' and self.state["left"][0][0] == 'w' and self.state["back"][0][2] == 'r':
                self.perform(["L'", "D'", "L", "B'", "D'", "B"])
            elif self.state["up"][0][0] == 'w' and self.state["left"][0][0] == 'r' and self.state["back"][0][2] == 'g':
                self.perform(["L'", "D2", "L", "B'", "D", "B"])

            elif self.state["front"][2][0] == 'r' and self.state["left"][2][2] == 'w' and self.state["down"][0][0] == 'g':
                self.perform(["B'", "D2", "B"])
            elif self.state["front"][2][0] == 'w' and self.state["left"][2][2] == 'g' and self.state["down"][0][0] == 'r':
                self.perform(["D2", "B'", "D'", "B"])
            elif self.state["front"][2][0] == 'g' and self.state["left"][2][2] == 'r' and self.state["down"][0][0] == 'w':
                self.perform(["D2", "B'", "D2", "B", "D", "B'", "D'", "B"])

            elif self.state["front"][2][2] == 'w' and self.state["right"][2][0] == 'r' and self.state["down"][0][2] == 'g':
                self.perform(["B'", "D", "B"])
            elif self.state["front"][2][2] == 'g' and self.state["right"][2][0] == 'w' and self.state["down"][0][2] == 'r':
                self.perform(["D", "B'", "D'", "B"])
            elif self.state["front"][2][2] == 'r' and self.state["right"][2][0] == 'g' and self.state["down"][0][2] == 'w':
                self.perform(["D", "B'", "D2", "B", "D", "B'", "D'", "B"])

            elif self.state["right"][2][2] == 'w' and self.state["down"][2][2] == 'g' and self.state["back"][2][0] == 'r':
                self.perform(["D'", "B'", "D", "B"])
            elif self.state["right"][2][2] == 'g' and self.state["down"][2][2] == 'r' and self.state["back"][2][0] == 'w':
                self.perform(["B'", "D'", "B"])
            elif self.state["right"][2][2] == 'r' and self.state["down"][2][2] == 'w' and self.state["back"][2][0] == 'g':
                self.perform(["B'", "D2", "B", "D", "B'", "D'", "B"])

            elif self.state["left"][2][0] == 'r' and self.state["down"][2][0] == 'g' and self.state["back"][2][2] == 'w':
                self.perform(["D2", "B'", "D", "B"])
            elif self.state["left"][2][0] == 'w' and self.state["down"][2][0] == 'r' and self.state["back"][2][2] == 'g':
                self.perform(["D'", "B'", "D'", "B"])
            elif self.state["left"][2][0] == 'g' and self.state["down"][2][0] == 'w' and self.state["back"][2][2] == 'r':
                self.perform(["D'", "B'", "D2", "B", "D", "B'", "D'", "B"])

        def solve_w_r_b():
            if self.state["up"][0][0] == 'b' and self.state["left"][0][0] == 'r' and self.state["back"][0][2] == 'w':
                self.perform(["B", "D", "B'", "D2", "L'", "D", "L"])
            elif self.state["up"][0][0] == 'r' and self.state["left"][0][0] == 'w' and self.state["back"][0][2] == 'b':
                self.perform(["L'", "D'", "L", "D", "L'", "D'", "L"])

            elif self.state["front"][2][0] == 'b' and self.state["left"][2][2] == 'w' and self.state["down"][0][0] == 'r':
                self.perform(["D2", "L'", "D", "L"])
            elif self.state["front"][2][0] == 'w' and self.state["left"][2][2] == 'r' and self.state["down"][0][0] == 'b':
                self.perform(["B", "D'", "B'"])
            elif self.state["front"][2][0] == 'r' and self.state["left"][2][2] == 'b' and self.state["down"][0][0] == 'w':
                self.perform(["D'", "B", "D2", "B'", "D'", "B", "D", "B'"])

            elif self.state["front"][2][2] == 'w' and self.state["right"][2][0] == 'b' and self.state["down"][0][2] == 'r':
                self.perform(["L'", "D2", "L"])
            elif self.state["front"][2][2] == 'r' and self.state["right"][2][0] == 'w' and self.state["down"][0][2] == 'b':
                self.perform(["B", "D2", "B'"])
            elif self.state["front"][2][2] == 'b' and self.state["right"][2][0] == 'r' and self.state["down"][0][2] == 'w':
                self.perform(["D2", "B", "D2", "B'", "D2", "L'", "D", "L"])

            elif self.state["right"][2][2] == 'w' and self.state["down"][2][2] == 'r' and self.state["back"][2][0] == 'b':
                self.perform(["L'", "D", "L"])
            elif self.state["right"][2][2] == 'r' and self.state["down"][2][2] == 'b' and self.state["back"][2][0] == 'w':
                self.perform(["D2", "B", "D'", "B'"])
            elif self.state["right"][2][2] == 'b' and self.state["down"][2][2] == 'w' and self.state["back"][2][0] == 'r':
                self.perform(["D", "B", "D2", "B'", "D2", "L'", "D", "L"])

            elif self.state["left"][2][0] == 'b' and self.state["down"][2][0] == 'r' and self.state["back"][2][2] == 'w':
                self.perform(["D'", "L'", "D", "L"])
            elif self.state["left"][2][0] == 'w' and self.state["down"][2][0] == 'b' and self.state["back"][2][2] == 'r':
                self.perform(["L'", "D'", "L"])
            elif self.state["left"][2][0] == 'r' and self.state["down"][2][0] == 'w' and self.state["back"][2][2] == 'b':
                self.perform(["L'", "D2", "L", "D", "L'", "D'", "L"])

        solve_w_o_b()
        solve_w_o_g()
        solve_w_r_g()
        solve_w_r_b()

    def verify_corners(self):
        return (self.state["up"] == np.array([['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']])).all() and (self.state["front"][0] == np.array(['o', 'o', 'o'])).all() and (self.state["right"][0] == np.array(['g', 'g', 'g'])).all() and (self.state["back"][0] == np.array(['r', 'r', 'r'])).all() and (self.state["left"][0] == np.array(['b', 'b', 'b'])).all()

    def second_layer(self):
        def solve_g_o():
            pos = self.locate_edge(('g', 'o'))
            if pos == ("front", "left"):
                self.perform(["F", "U'", "F'", "U", "L'", "U2", "L", "U2", "L'", "U", "L"])
            elif pos == ("front", "right"):
                self.perform(["R", "U'", "R'", "U'", "F'", "U", "F", "U", "L'", "U", "L", "U", "F", "U'", "F'"])
            elif pos == ("right", "front"):
                self.perform(["F2", "U2", "F2", "U2", "F2"])
            elif pos == ("back", "right"):
                self.perform(["B", "U'", "B'", "U'", "R'", "U", "R", "U", "F", "U'", "F'", "U'", "L'", "U", "L"])
            elif pos == ("right", "back"):
                self.perform(["B", "U'", "B'", "U'", "R'", "U", "R", "U2", "L'", "U", "L", "U", "F", "U'", "F'"])
            elif pos == ("back", "left"):
                self.perform(["B'", "U", "B", "U", "L", "U'", "L'", "U'", "F", "U'", "F'", "U'", "L'", "U", "L"])
            elif pos == ("left", "back"):
                self.perform(["L2", "U2", "L2", "U2", "L2"])
            elif pos == ("front", "up"):
                self.perform(["U2", "F", "U'", "F'", "U'", "L'", "U", "L"])
            elif pos == ("left", "up"):
                self.perform(["U", "F", "U'", "F'", "U'", "L'", "U", "L"])
            elif pos == ("back", "up"):
                self.perform(["F", "U'", "F'", "U'", "L'", "U", "L"])
            elif pos == ("right", "up"):
                self.perform(["U'", "F", "U'", "F'", "U'", "L'", "U", "L"])
            elif pos == ("up", "front"):
                self.perform(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
            elif pos == ("up", "left"):
                self.perform(["U2", "L'", "U", "L", "U", "F", "U'", "F'"])
            elif pos == ("up", "back"):
                self.perform(["U", "L'", "U", "L", "U", "F", "U'", "F'"])
            elif pos == ("up", "right"):
                self.perform(["L'", "U", "L", "U", "F", "U'", "F'"])

        def solve_b_o():
            pos = self.locate_edge(('b', 'o'))
            if pos == ("front", "right"):
                self.perform(["R", "U'", "R'", "U", "F'", "U2", "F", "U2", "F'", "U", "F"])
            elif pos == ("back", "right"):
                self.perform(["B", "U'", "B'", "U'", "R'", "U", "R", "U", "F'", "U", "F", "U", "R", "U'", "R'"])
            elif pos == ("right", "back"):
                self.perform(["R2", "U2", "R2", "U2", "R2"])
            elif pos == ("back", "left"):
                self.perform(["B'", "U", "B", "U", "L", "U'", "L'", "U'", "F'", "U", "F", "U", "R", "U'", "R'"])
            elif pos == ("left", "back"):
                self.perform(["B'", "U", "B", "U", "L", "U'", "L'", "U2", "R", "U'", "R'", "U'", "F'", "U", "F"])
            elif pos == ("front", "up"):
                self.perform(["U2", "F'", "U", "F", "U", "R", "U'", "R'"])
            elif pos == ("left", "up"):
                self.perform(["U", "F'", "U", "F", "U", "R", "U'", "R'"])
            elif pos == ("back", "up"):
                self.perform(["F'", "U", "F", "U", "R", "U'", "R'"])
            elif pos == ("right", "up"):
                self.perform(["U'", "F'", "U", "F", "U", "R", "U'", "R'"])
            elif pos == ("up", "front"):
                self.perform(["U", "R", "U'", "R'", "U'", "F'", "U", "F"])
            elif pos == ("up", "left"):
                self.perform(["R", "U'", "R'", "U'", "F'", "U", "F"])
            elif pos == ("up", "back"):
                self.perform(["U'", "R", "U'", "R'", "U'", "F'", "U", "F"])
            elif pos == ("up", "right"):
                self.perform(["U2", "R", "U'", "R'", "U'", "F'", "U", "F"])

        def solve_b_r():
            pos = self.locate_edge(('b', 'r'))
            if pos == ("back", "right"):
                self.perform(["B", "U'", "B'", "U'", "R'", "U", "R", "U'", "B", "U'", "B'", "U'", "R'", "U", "R"])
            elif pos == ("back", "left"):
                self.perform(["B'", "U", "B", "U", "L", "U'", "L'", "U", "B", "U'", "B'", "U'", "R'", "U", "R"])
            elif pos == ("left", "back"):
                self.perform(["B2", "U2", "B2", "U2", "B2"])
            elif pos == ("front", "up"):
                self.perform(["B", "U'", "B'", "U'", "R'", "U", "R"])
            elif pos == ("left", "up"):
                self.perform(["U'", "B", "U'", "B'", "U'", "R'", "U", "R"])
            elif pos == ("back", "up"):
                self.perform(["U2", "B", "U'", "B'", "U'", "R'", "U", "R"])
            elif pos == ("right", "up"):
                self.perform(["U", "B", "U'", "B'", "U'", "R'", "U", "R"])
            elif pos == ("up", "front"):
                self.perform(["U", "R'", "U", "R", "U", "B", "U'", "B'"])
            elif pos == ("up", "left"):
                self.perform(["R'", "U", "R", "U", "B", "U'", "B'"])
            elif pos == ("up", "back"):
                self.perform(["U'", "R'", "U", "R", "U", "B", "U'", "B'"])
            elif pos == ("up", "right"):
                self.perform(["U2", "R'", "U", "R", "U", "B", "U'", "B'"])

        def solve_g_r():
            pos = self.locate_edge(('g', 'r'))
            if pos == ("back", "left"):
                self.perform(["B'", "U", "B", "U'", "L", "U2", "L'", "U2", "L", "U'", "L'"])
            elif pos == ("front", "up"):
                self.perform(["B'", "U", "B", "U", "L", "U'", "L'"])
            elif pos == ("left", "up"):
                self.perform(["U'", "B'", "U", "B", "U", "L", "U'", "L'"])
            elif pos == ("back", "up"):
                self.perform(["U2", "B'", "U", "B", "U", "L", "U'", "L'"])
            elif pos == ("right", "up"):
                self.perform(["U", "B'", "U", "B", "U", "L", "U'", "L'"])
            elif pos == ("up", "front"):
                self.perform(["U'", "L", "U'", "L'", "U'", "B'", "U", "B"])
            elif pos == ("up", "left"):
                self.perform(["U2", "L", "U'", "L'", "U'", "B'", "U", "B"])
            elif pos == ("up", "back"):
                self.perform(["U", "L", "U'", "L'", "U'", "B'", "U", "B"])
            elif pos == ("up", "right"):
                self.perform(["L", "U'", "L'", "U'", "B'", "U", "B"])

        solve_g_o()
        solve_b_o()
        solve_b_r()
        solve_g_r()

    def verify_f2l(self):
        return (self.state["front"][1:2] == np.array([['o', 'o', 'o'], ['o', 'o', 'o']])).all() and (self.state["left"][1:2] == np.array([['g', 'g', 'g'], ['g', 'g', 'g']])).all() and (self.state["back"][1:2] == np.array([['r', 'r', 'r'], ['r', 'r', 'r']])).all() and (self.state["right"][1:2] == np.array([['b', 'b', 'b'], ['b', 'b', 'b']])).all()

    def oll(self):
        cnt = int(self.state['up'][0][1]=='y') + int(self.state['up'][1][2]=='y') + int(self.state['up'][2][1]=='y') + int(self.state['up'][1][0]=='y')
        while(cnt != 4):
            if cnt == 0:
                self.perform(["F", "U", "R", "U'", "R'", "F'"])
            elif cnt == 2:
                if self.state['up'][1][0] == 'y' and self.state['up'][1][2] == 'y':
                    self.perform(["F", "R", "U", "R'", "U'", "F'"])
                elif self.state['up'][0][1] == 'y' and self.state['up'][2][1] == 'y':
                    self.perform(["U", "F", "R", "U", "R'", "U'", "F'"])
                elif self.state['up'][0][1] == 'y' and self.state['up'][1][0] == 'y':
                    self.perform(["F", "U", "R", "U'", "R'", "F'"])
                elif self.state['up'][0][1] == 'y' and self.state['up'][1][2] == 'y':
                    self.perform(["U'", "F", "U", "R", "U'", "R'", "F'"])
                elif self.state['up'][2][1] == 'y' and self.state['up'][1][2] == 'y':
                    self.perform(["U2", "F", "U", "R", "U'", "R'", "F'"])
                elif self.state['up'][1][0] == 'y' and self.state['up'][2][1] == 'y':
                    self.perform(["U", "F", "U", "R", "U'", "R'", "F'"])
            cnt = int(self.state['up'][0][1]=='y') + int(self.state['up'][1][2]=='y') + int(self.state['up'][2][1]=='y') + int(self.state['up'][1][0]=='y')

        cnt = int(self.state['up'][0][0]=='y') + int(self.state['up'][0][2]=='y') + int(self.state['up'][2][0]=='y') + int(self.state['up'][2][2]=='y')
        if cnt == 0:
            while not (self.state['front'][0][2] == 'y' and self.state['back'][0][0] == 'y'):
                self.perform(["U"])
            if self.state['front'][0][0] == 'y' :
                self.perform(["F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"])
            else:
                self.perform(["R", "U2", "R2", "U'", "R2", "U'", "R2", "U2", "R"])
        elif cnt == 1:
            while self.state['up'][2][0] != 'y':
                self.perform(["U"])
            if self.state['front'][0][2] == 'y':
                self.perform(["R", "U", "R'", "U", "R", "U2", "R'"])
            else:
                self.perform(["U", "R'", "U'", "R", "U'", "R'", "U2", "R"])
        elif cnt == 2:
            if (self.state['up'][0][0] == 'y' and self.state['up'][0][2] == 'y') or (self.state['up'][0][2] == 'y' and self.state['up'][2][2] == 'y') or (self.state['up'][2][2] == 'y' and self.state['up'][2][0] == 'y') or (self.state['up'][0][0] == 'y' and self.state['up'][2][0] == 'y'):
                while not (self.state['up'][0][0] == 'y' and self.state['up'][0][2] == 'y'):
                    self.perform(["U"])
                if self.state['front'][0][0] == 'y' and self.state['front'][0][2] == 'y':
                    self.perform(["R2", "D", "R'", "U2", "R", "D'", "R'", "U2", "R'"])
                else:
                    self.perform(["U'", "R'", "F'", "L", "F", "R", "F'", "L'", "F"])
            else:
                while not (self.state['up'][0][0] == 'y' and self.state['up'][2][2] == 'y' and self.state['left'][0][2] == 'y'):
                    self.perform(["U"])
                self.perform(["R'", "F'", "L'", "F", "R" ,"F'", "L", "F"])

    def verify_oll(self):
        return (self.state["up"] == np.array([['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']])).all()

    def pll(self):
        while not ((self.state["front"][0][0] == self.state["front"][0][2]) and (self.state["right"][0][0] == self.state["right"][0][2]) and (self.state["back"][0][0] == self.state["back"][0][2]) and (self.state["left"][0][0] == self.state["left"][0][2])):
            for i in range(3):
                if self.state['back'][0][0] == self.state['back'][0][2]:
                    break
                self.perform(["U"])
            self.perform(["R'", "F", "R'", "B2", "R", "F'", "R'", "B2", "R2"])
        while not ((self.state["front"][0][0] == 'o' and self.state["front"][0][2] == 'o') and (self.state["right"][0][0] == 'b' and self.state["right"][0][2] == 'b') and (self.state["back"][0][0] == 'r' and self.state["back"][0][2] == 'r') and (self.state["left"][0][0] == 'g' and self.state["left"][0][2] == 'g')):
            self.perform(["U"])

        cnt = int(self.state["front"][0][1] == 'o') + int(self.state["right"][0][1] == 'b') + int(self.state["back"][0][1] == 'r') + int(self.state["left"][0][1] == 'g')
        if cnt == 0:
            if self.state["front"][0][1] == 'r':
                self.perform(["R2", "L2", "D", "R2", "L2", "U2", "R2", "L2", "D", "R2", "L2"])
            elif self.state["front"][0][1] == 'b':
                self.perform(["R2", "L2", "D", "R2", "L2", "U", "R'", "L", "F2", "R2", "L2", "B2", "R'", "L", "U2"])
            elif self.state["front"][0][1] == 'g':
                self.perform(["U", "R2", "L2", "D", "R2", "L2", "U", "R'", "L", "F2", "R2", "L2", "B2", "R'", "L", "U"])
        elif cnt == 1:
            while not ((self.state["back"][0][0] == self.state["back"][0][1]) and (self.state["back"][0][1] == self.state["back"][0][2])):
                self.perform(["U"])
            if self.state["left"][0][2] == self.state["front"][0][1]:
                self.perform(["R2", "U", "R", "U", "R'", "U'", "R'", "U'", "R'", "U", "R'"])
            else:
                self.perform(["R", "U'", "R", "U", "R", "U", "R", "U'", "R'", "U'", "R2"])
            while not self.state["front"][0][0] == 'o':
                self.perform(["U"])

    def verify_pll(self):
        return (self.state["front"][0] == np.array(['o', 'o', 'o'])).all() and (self.state["left"][0] == np.array(['g', 'g', 'g'])).all() and (self.state["back"][0] == np.array(['r', 'r', 'r'])).all() and (self.state["right"][0] == np.array(['b', 'b', 'b'])).all()


    def solve(self):
        print("\n---Cross---\n")
        self.cross()
        assert(self.verify_cross())
        print("\n---First layer corners---\n")
        self.first_layer_corners()
        assert(self.verify_corners())
        print("\n---Second layer---")
        print("Rotate cube\n")
        self.up_down()
        self.second_layer()
        assert(self.verify_f2l())
        print("\n---OLL---\n")
        self.oll()
        assert(self.verify_oll())
        print("\n---PLL---\n")
        self.pll()
        assert(self.verify_pll())
