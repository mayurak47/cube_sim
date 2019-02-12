import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import random

from PIL import Image
class Cube():
    faces = ['front', 'back', 'up', 'down', 'left', 'right']
    def __init__(self):
        self.reset()
    def reset(self):
        self.state = {'up':np.array([['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]),
                'front':np.array([['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]),
                'left':np.array([['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]),
                'right':np.array([['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]),
                'back':np.array([['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]),
                'down':np.array([['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']])}
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

    def perform(self, moves):
        for move in moves:
            if move=="R":
                self.right()
            if move=="R2":
                self.right()
                self.right()
            if move=="R'":
                self.r_prime()
            if move=="L":
                self.left()
            if move=="L2":
                self.left()
                self.left()
            if move=="L'":
                self.l_prime()
            if move=="F":
                self.front()
            if move=="F2":
                self.front()
                self.front()
            if move=="F'":
                self.f_prime()
            if move=="U":
                self.up()
            if move=="U2":
                self.up()
                self.up()
            if move=="U'":
                self.u_prime()
            if move=="D":
                self.down()
            if move=="D2":
                self.down()
                self.down()
            if move=="D'":
                self.d_prime()
            if move=="B":
                self.back()
            if move=="B2":
                self.back()
                self.back()
            if move=="B'":
                self.b_prime()
            print(move, end=" ")
        print()

    def locate_edge(self, cols):
        if self.state['front'][1][2] == cols[0] and self.state['right'][1][0] == cols[1]:
            return ("front", "right")
        if self.state['front'][1][2] == cols[1] and self.state['right'][1][0] == cols[0]:
            return ("right", "front")

        if self.state['front'][1][0] == cols[0] and self.state['left'][1][2] == cols[1]:
            return ("front", "left")
        if self.state['front'][1][0] == cols[1] and self.state['left'][1][2] == cols[0]:
            return ("left", "front")

        if self.state['front'][0][1] == cols[0] and self.state['up'][2][1] == cols[1]:
            return ("front", "up")
        if self.state['front'][0][1] == cols[1] and self.state['up'][2][1] == cols[0]:
            return ("up", "front")

        if self.state['front'][2][1] == cols[0] and self.state['down'][0][1] == cols[1]:
            return ("front", "down")
        if self.state['front'][2][1] == cols[1] and self.state['down'][0][1] == cols[0]:
            return ("down", "front")

        if self.state['up'][1][2] == cols[0] and self.state['right'][0][1] == cols[1]:
            return ("up", "right")
        if self.state['up'][1][2] == cols[1] and self.state['right'][0][1] == cols[0]:
            return ("right", "up")

        if self.state['up'][1][0] == cols[0] and self.state['left'][0][1] == cols[1]:
            return ("up", "left")
        if self.state['up'][1][0] == cols[1] and self.state['left'][0][1] == cols[0]:
            return ("left", "up")

        if self.state['down'][1][2] == cols[0] and self.state['right'][2][1] == cols[1]:
            return ("down", "right")
        if self.state['down'][1][2] == cols[1] and self.state['right'][2][1] == cols[0]:
            return ("right", "down")

        if self.state['down'][1][0] == cols[0] and self.state['left'][2][1] == cols[1]:
            return ("down", "left")
        if self.state['down'][1][0] == cols[1] and self.state['left'][2][1] == cols[0]:
            return ("left", "down")

        if self.state['back'][1][2] == cols[0] and self.state['left'][1][0] == cols[1]:
            return ("back", "left")
        if self.state['back'][1][2] == cols[1] and self.state['left'][1][0] == cols[0]:
            return ("left", "back")

        if self.state['back'][1][0] == cols[0] and self.state['right'][1][2] == cols[1]:
            return ("back", "right")
        if self.state['back'][1][0] == cols[1] and self.state['right'][1][2] == cols[0]:
            return ("right", "back")

        if self.state['back'][0][1] == cols[0] and self.state['up'][0][1] == cols[1]:
            return ("back", "up")
        if self.state['back'][0][1] == cols[1] and self.state['up'][0][1] == cols[0]:
            return ("up", "back")

        if self.state['back'][2][1] == cols[0] and self.state['down'][2][1] == cols[1]:
            return ("back", "down")
        if self.state['front'][2][1] == cols[1] and self.state['down'][2][1] == cols[0]:
            return ("down", "back")

    def randomize(self):
        scramble = []
        moves = ['R', 'L', 'U', 'D', 'F', 'B', 'R2', "R'", 'L2', "L'", 'U2', "U'", 'D2', "D'", 'F2', "F'", 'B2', "B'"]
        for i in range(20):
            x = random.randint(0, 17)
            if not scramble:
                scramble.append(moves[x])
            else:
                while scramble[i-1][0] == moves[x][0]:
                    x = random.randint(0, 17)
                scramble.append(moves[x])
        self.perform(scramble)

    def cross(self):
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
                self.perform(["B'", "L'"])
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
                self.perform(["L", "D'", "L'", "B2"])
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
                self.perform(["L", "B", "L'"])
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
