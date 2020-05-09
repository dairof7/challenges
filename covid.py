#!/usr/bin/python3


def verify_spot(matrix, spot, pos=[]):
	# if pos[0] - spot < 0 or pos[0] + spot > len(matrix):
	# 	return "Pared"
	# if pos[1] - spot < 0 or pos[1] + spot > len(matrix):
	# 	return "Pared"
	for i in range(1, spot + 1):
		if matrix[pos[0] - i][pos[1] - i] == 1:
			return False
		if matrix[pos[0] - i][pos[1]] == 1:
			return False
		if matrix[pos[0] - i][pos[1] + i] == 1:
			return False
		if matrix[pos[0]][pos[1] - i] == 1:
			return False
		if matrix[pos[0]][pos[1] + i] == 1:
			return False
		if matrix[pos[0] + i][pos[1] - i] == 1:
			return False
		if matrix[pos[0] + i][pos[1]] == 1:
			return False
		if matrix[pos[0] + i][pos[1] + i] == 1:
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
		[0, 1, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]
	]
allowed_spots = 1

x1 = int(input("coordenada en x ini: "))
y1 = int(input("coordenada en y ini: "))

x2 = int(input("coordenada en x fin: "))
y2 = int(input("coordenada en y fin: "))
spots[x1][y1] = "x"
print_matrix(spots)
if ((x1-x2 != 0) ^ (y1-y2 != 0)):
    # vertical move
    if (x1 - x2 > 0):
        spots[x1][y1] = 0
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

