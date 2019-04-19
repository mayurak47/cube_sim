import copy
import time
import numpy as np
class Face:
    def __init__(self, color=None):
        self.f = []
        if not color:
            print("Enter colors - ")
            for i in range(2):
                x = input()
                x = x.split(" ")
                self.f.append(x)
        else:
            self.f.append([color, color])
            self.f.append([color, color])
        self.f = np.array(self.f)


    def disp(self):
        print(self.f[0][0] + " " + self.f[0][1])
        print(self.f[1][0] + " " + self.f[1][1])
    def __eq__(self, other):
        return (self.f == other.f).all()
    def __hash__(self):
        h = 7
        h = 31*h+ord(self.f[0][0])
        h = 31*h+ord(self.f[0][1])
        h = 31*h+ord(self.f[1][0])
        h = 31*h+ord(self.f[1][1])
        return h

class Cube:
    facecodes = ['f', 'l', 'b', 'r', 'u', 'd']
    facenames = ["Front", "Left", "Back", "Right", "Up", "Down"]
    # faces = {}
    def __init__(self, cube=None):
        self.faces = {}
        if not cube:
            self.faces['f'] = Face('o')
            self.faces['l'] = Face('b')
            self.faces['b'] = Face('r')
            self.faces['r'] = Face('g')
            self.faces['u'] = Face('w')
            self.faces['d'] = Face('y')
        else:
            self.faces['f'] = cube.faces['f']
            self.faces['l'] = cube.faces['l']
            self.faces['b'] = cube.faces['b']
            self.faces['r'] = cube.faces['r']
            self.faces['u'] = cube.faces['u']
            self.faces['d'] = cube.faces['d']

    def __eq__(self, other):
        for face in self.facecodes:
            if not self.faces[face] == other.faces[face]:
                return False
        return True
    def __hash__(self):
        h = 7
        for face in self.facecodes:
            h = 31*h + self.faces[face].__hash__()
        return h
    def display(self):
        for face in self.facecodes:
            print(face)
            self.faces[face].disp()
            print()
    def right(self):
        temp = copy.deepcopy(self.faces)
        self.faces['u'].f[:,1] = temp['f'].f[:,1]
        self.faces['f'].f[:,1] = temp['d'].f[:,1]
        self.faces['d'].f[:,1] = temp['b'].f[:,0][::-1]
        self.faces['b'].f[:,0] = temp['u'].f[:,1][::-1]
        self.faces['r'].f[0][0] = temp['r'].f[1][0]
        self.faces['r'].f[0][1] = temp['r'].f[0][0]
        self.faces['r'].f[1][1] = temp['r'].f[0][1]
        self.faces['r'].f[1][0] = temp['r'].f[1][1]
    def front(self):
        temp = copy.deepcopy(self.faces)
        self.faces['u'].f[1,:] = temp['l'].f[:,1][::-1]
        self.faces['r'].f[:,0] = temp['u'].f[1,:]
        self.faces['d'].f[0,:] = temp['r'].f[:,0][::-1]
        self.faces['l'].f[:,1] = temp['d'].f[0,:]
        self.faces['f'].f[0][0] = temp['f'].f[1][0]
        self.faces['f'].f[0][1] = temp['f'].f[0][0]
        self.faces['f'].f[1][1] = temp['f'].f[0][1]
        self.faces['f'].f[1][0] = temp['f'].f[1][1]
    def up(self):
        temp = copy.deepcopy(self.faces)
        self.faces['b'].f[0,:] = temp['l'].f[0,:]
        self.faces['r'].f[0,:] = temp['b'].f[0,:]
        self.faces['f'].f[0,:] = temp['r'].f[0,:]
        self.faces['l'].f[0,:] = temp['f'].f[0,:]
        self.faces['u'].f[0][0] = temp['u'].f[1][0]
        self.faces['u'].f[0][1] = temp['u'].f[0][0]
        self.faces['u'].f[1][1] = temp['u'].f[0][1]
        self.faces['u'].f[1][0] = temp['u'].f[1][1]
    def left(self):
        temp = copy.deepcopy(self.faces)
        self.faces['u'].f[:,0] = temp['b'].f[:,1][::-1]
        self.faces['f'].f[:,0] = temp['u'].f[:,0]
        self.faces['d'].f[:,0] = temp['f'].f[:,0]
        self.faces['b'].f[:,1] = temp['d'].f[:,0][::-1]
        self.faces['l'].f[0][0] = temp['l'].f[1][0]
        self.faces['l'].f[0][1] = temp['l'].f[0][0]
        self.faces['l'].f[1][1] = temp['l'].f[0][1]
        self.faces['l'].f[1][0] = temp['l'].f[1][1]
    def down(self):
        temp = copy.deepcopy(self.faces)
        self.faces['b'].f[1,:] = temp['r'].f[1,:]
        self.faces['r'].f[1,:] = temp['f'].f[1,:]
        self.faces['f'].f[1,:] = temp['l'].f[1,:]
        self.faces['l'].f[1,:] = temp['b'].f[1,:]
        self.faces['d'].f[0][0] = temp['d'].f[1][0]
        self.faces['d'].f[0][1] = temp['d'].f[0][0]
        self.faces['d'].f[1][1] = temp['d'].f[0][1]
        self.faces['d'].f[1][0] = temp['d'].f[1][1]
    def back(self):
        temp = copy.deepcopy(self.faces)
        self.faces['u'].f[0,:] = temp['r'].f[:,1]
        self.faces['r'].f[:,1] = temp['d'].f[1,:][::-1]
        self.faces['d'].f[1,:] = temp['l'].f[:,0]
        self.faces['l'].f[:,0] = temp['u'].f[0,:][::-1]
        self.faces['b'].f[0][0] = temp['b'].f[1][0]
        self.faces['b'].f[0][1] = temp['b'].f[0][0]
        self.faces['b'].f[1][1] = temp['b'].f[0][1]
        self.faces['b'].f[1][0] = temp['b'].f[1][1]

def newCube(cube):
    x = Cube()
    x.faces['f'] = cube.faces['f']
    x.faces['l'] = cube.faces['l']
    x.faces['b'] = cube.faces['b']
    x.faces['r'] = cube.faces['r']
    x.faces['u'] = cube.faces['u']
    x.faces['d'] = cube.faces['d']
    return x

def neighbors(cube):
    # tic = time.time()
    # cube.display()
    ls = []
    temp = copy.deepcopy(cube)
    temp.right()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.left()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.front()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.up()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.back()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.down()
    ls.append(temp)


    temp = copy.deepcopy(cube)
    temp.right()
    temp.right()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.left()
    temp.left()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.front()
    temp.front()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.up()
    temp.up()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.back()
    temp.back()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.down()
    temp.down()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.right()
    temp.right()
    temp.right()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.left()
    temp.left()
    temp.left()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.front()
    temp.front()
    temp.front()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.up()
    temp.up()
    temp.up()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.back()
    temp.back()
    temp.back()
    ls.append(temp)

    temp = copy.deepcopy(cube)
    temp.down()
    temp.down()
    temp.down()
    ls.append(temp)
    return ls

def bfs(src, dst):
    tic = time.time()
    visiteds = set()
    visiteds.add(src)
    visitedd = set()
    visitedd.add(dst)
    qs = []
    qs.append(src)
    qd = []
    qd.append(dst)
    preds = {src: None}
    predd = {dst: None}
    us, ud = None, None
    flag = False
    fin = None
    while len(qs)>0 and len(qd) >0:
        us = qs[0]
        ud = qd[0]
        if us == dst or ud == src:
            break
        qs.pop(0)
        qd.pop(0)
        for elem in neighbors(us):
            if not elem in visiteds:
                if elem in visitedd:
                    flag = True
                    fin = elem
                    break
                visiteds.add(elem)
                preds[elem] = us
                qs.append(elem)
        if flag==True:
            break
        for elem in neighbors(ud):
            if not elem in visitedd:
                if elem in visiteds:
                    fin = elem
                    flag = True
                    break
                visitedd.add(elem)
                predd[elem] = ud
                qd.append(elem)
        if flag == True:
            break
    path = []
    if fin in visiteds:
        temp = fin
        while preds[temp]:
            path.append(temp)
            temp = preds[temp]
        path.append(src)
        path.reverse()
        temp = ud
        while predd[temp]:
            path.append(temp)
            temp = predd[temp]
        path.append(dst)
    else:
        temp = us
        while preds[temp]:
            path.append(temp)
            temp = preds[temp]
        path.append(src)
        path.reverse()
        temp = fin
        while predd[temp]:
            path.append(temp)
            temp = predd[temp]
        path.append(dst)


    for i in range(len(path)-1):
        temp = copy.deepcopy(path[i])
        temp.right()
        if temp == path[i+1]:
            print("R", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.right()
        temp.right()
        if temp == path[i+1]:
            print("R2", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.right()
        temp.right()
        temp.right()
        if temp == path[i+1]:
            print("R'", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.front()
        if temp == path[i+1]:
            print("F", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.front()
        temp.front()
        if temp == path[i+1]:
            print("F2", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.front()
        temp.front()
        temp.front()
        if temp == path[i+1]:
            print("F'", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.up()
        if temp == path[i+1]:
            print("U", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.up()
        temp.up()
        if temp == path[i+1]:
            print("U2", end=" ")
            continue


        temp = copy.deepcopy(path[i])
        temp.up()
        temp.up()
        temp.up()
        if temp == path[i+1]:
            print("U'", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.left()
        if temp == path[i+1]:
            print("L", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.left()
        temp.left()
        if temp == path[i+1]:
            print("L2", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.left()
        temp.left()
        temp.left()
        if temp == path[i+1]:
            print("L'", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.back()
        if temp == path[i+1]:
            print("B", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.back()
        temp.back()
        if temp == path[i+1]:
            print("B2", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.back()
        temp.back()
        temp.back()
        if temp == path[i+1]:
            print("B'", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.down()
        if temp == path[i+1]:
            print("D", end=" ")
            continue

        temp = copy.deepcopy(path[i])
        temp.down()
        temp.down()
        if temp == path[i+1]:
            print("D2", end=" ")
            continue


        temp = copy.deepcopy(path[i])
        temp.down()
        temp.down()
        temp.down()
        if temp == path[i+1]:
            print("D'", end=" ")
            continue

    print()
    toc = time.time()
    print(toc-tic)

def __main__():
    a = Cube()
    b = Cube()
    print("Enter moves, terminate w/ -1")
    l = []
    x = input()
    while x!='-1':
        l.append(x)
        x = input()
    for elem in l:
        if elem=='R':
            b.right()
        elif elem=='L':
            b.left()
        elif elem=='F':
            b.front()
        elif elem=='D':
            b.down()
        elif elem=='U':
            b.up()
        else:
            b.back()
    bfs(b, a)

if __name__=="__main__":
    __main__()
