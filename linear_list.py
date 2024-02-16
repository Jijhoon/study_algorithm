# def find_and_insert_data(friend, number) :
# 	find = -1
# 	for i in range(len(connection)) :
# 		pair = connection[i]
# 		if number >= pair[1] :
# 			find = i
# 			break
# 	if find == -1 :
# 		find = len(connection)

# 	insert_data(find, (friend, number))


# def insert_data(position, friend):
# 	if position < 0 or position > len(connection):
# 		print("You write the wrong position. Please try again.")
# 		return

# 	connection.append(None)
# 	kLen = len(connection)

# 	for i in range(kLen - 1, position, -1):
# 		connection[i] = connection[i - 1]
# 		connection[i - 1] = None

# 	connection[position] = friend


# connection = [('이름1', 200), ('이름2', 150), ('이름3', 90), ('이름4', 30), ('이름5', 15)]

# if __name__ == "__main__":

# 	while True:
# 		data = input("the name of the friend-->")
# 		count = int(input("connecting count-->"))
# 		find_and_insert_data(data, count)
# 		print(connection)

##------------------------------------------------------------##
		
def printPoly(t_x, p_x) :
	polyStr = "P(x) = "
	
	for i in range(len(p_x)) :
		term = t_x[i]
		coef = p_x[i]

		if (coef >= 0) :		
			polyStr += "+"
		polyStr += str(coef) + "x^" + str(term) + " "

	return polyStr


def calcPoly(xVal, t_x, p_x) :
	retValue = 0
	
	for i in range(len(px)) :
		term = t_x[i]
		coef = p_x[i]	
		retValue += coef * xValue ** term

	return retValue

tx = [300, 20, 0]
px = [7, -4, 5] 

if __name__ == "__main__" :

	pStr = printPoly(tx, px)
	print(pStr)

	xValue = int(input("X 값-->"))

	pxValue = calcPoly(xValue, tx, px)
	print(pxValue)  
