#!/usr/bin/python3

def checkwall(matrix, dir, pos=[]):
    #print(len(matrix))
    #print(dir)
    #print(pos)
    if dir == "left" and pos[1] == 0:
        return -1
    if dir == "right" and pos[1] >= len(matrix) -1:
        #print("{}, {}".format(pos[1],len(matrix) -1))
        return -1
    if dir == "up" and pos[0] == 0:
        return -1
    if dir == "down" and pos[0] >= len(matrix) -1 :
        return -1
    return 1
    

def verify_spot(matrix, spot, pos=[]):
	#if pos[0] - spot < 0 or pos[0] + spot > len(matrix):
	#    return "Pared"
	#if pos[1] - spot < 0 or pos[1] + spot > len(matrix):
	# 	return "Pared"
    for i in range(-spot, spot + 1):
        for j in range (-spot, spot + 1):
            if pos[0]+i > len(matrix)-1 or pos[1]+j > len(matrix)-1:
                continue
            if matrix[pos[0] + i][pos[1] + j] == 1:
                print("Collision in: ({}, {})".format(pos[0] + i, pos[1] + j))
                return False
    return True

def print_matrix(matrix):
    print("________________________________")
    for x in matrix:
        print(*x, sep=" ")
    print("________________________________")

spots = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]
	]
allowed_spots = 2

x1 = int(input("coordenada en x ini: "))
y1 = int(input("coordenada en y ini: "))

x2 = int(input("coordenada en x fin: "))
y2 = int(input("coordenada en y fin: "))
spots[x1][y1] = "x"
print_matrix(spots)
if not verify_spot(spots, allowed_spots, [x1, y1]):
    print("cant move")
    exit ()

if ((x1-x2 != 0) ^ (y1-y2 != 0)):
    # vertical move
    if (x1 - x2 > 0):
        
        for i in range(abs(x1 - x2)):
            print("arriba")
            if checkwall(spots, "up", [x1, y1]) == -1:
                print("cant move to up because the wall")
                exit()
            x1 -= 1
            spots[x1][y1] = "x"
            print_matrix(spots)
            print([x1,y1])
            if not verify_spot(spots, allowed_spots, [x1, y1]):
                print("cant move")
                break
        else:
            print("done!")
    if (x1 - x2 < 0):
        
        for i in range(abs(x1 - x2)):
            print("abajo")
            if checkwall(spots, "down", [x1, y1]) ==-1:
                print("cant move to down because the wall")
                exit()
            x1 += 1
            spots[x1][y1] = "x"
            print_matrix(spots)
            print([x1,y1])
            if verify_spot(spots, allowed_spots, [x1, y1]) == False:
                print("cant move")
                break
        else:
            print("done!")
    # horizontal move
    if (y1 - y2 > 0):
        
        for i in range(abs(y1 - y2)):
            print("izq")
            if checkwall(spots, "left", [x1, y1]) ==-1:
                print("cant move to left because the wall")
                exit()
            y1 -= 1
            spots[x1][y1] = "x"
            print_matrix(spots)
            print([x1,y1])
            if not verify_spot(spots, allowed_spots, [x1, y1]):
                print("cant move")
                break
        else:
            print("done!")
    if (y1 - y2 < 0):
        
        for i in range(abs(y1 - y2)):
            print("derecha")
            if checkwall(spots, "right", [x1, y1]) == -1:
                print("cant move to right because the wall")
                exit()
            y1 += 1
            spots[x1][y1] = "x"
            print_matrix(spots)
            print([x1,y1])
            if not verify_spot(spots, allowed_spots, [x1, y1]):
                print("cant move")
                break
        else:
            print("done!")
else:
    print("not allowed")

