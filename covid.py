#!/usr/bin/python3


def verify_spot(matrix, spot, pos=[]):
	# if pos[0] - spot < 0 or pos[0] + spot > len(matrix):
	# 	return "Pared"
	# if pos[1] - spot < 0 or pos[1] + spot > len(matrix):
	# 	return "Pared"
    for i in range(-spot, spot + 1):
        for j in range (-spot, spot + 1):
            #print("<{},{}> = {}".format(i,j,matrix[pos[0] + i][pos[1] + j]))
            if matrix[pos[0] + i][pos[1] + j] == 1:
                print("Collision in: ({}, {})".format(pos[0] + i, pos[1] + i))
                return False
    return True

def print_matrix(matrix):
    print("________________________________")
    for x in matrix:
        print(*x, sep=" ")
    print("________________________________")

spots = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 0, 1, 0, 0, 0, 0, 0],
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
        print("arriba")
        for i in range(abs(x1 - x2)):
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
        print("abajo")
        for i in range(abs(x1 - x2)):
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
        print("izq")
        for i in range(abs(y1 - y2)):
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
        print("derecha")
        for i in range(abs(y1 - y2)):
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

