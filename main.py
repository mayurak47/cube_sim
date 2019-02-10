from cube import Cube
c = Cube()
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
