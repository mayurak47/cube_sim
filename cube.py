import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from PIL import Image
class cube():
    def __init__(self):
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


c = cube()
while True:
    print("1. Show face\n2. Move\n3. Exit")
    x = int(input())
    if x==1:
        print("Which face?")
        y = input()
        c.disp(y)
    if x==2:
        y = input()
        for move in y:
            if move=='f' or move=='F':
                c.front()
            if move=='r' or move=='R':
                c.right()
            if move=='u' or move=='U':
                c.up()
            if move=='l' or move=='L':
                c.left()
            if move=='d' or move=='D':
                c.down()
            if move=='b' or move=='b':
                c.back()
    if x==3:
        break
