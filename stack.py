def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE - 1:
        return True
    else:
        return False


def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True 
    else:
        return False


def push(data):
    global SIZE, stack, top
    if is_stack_full():
        return
    top += 1
    stack[top] = data


def pop():
    global SIZE, stack, top
    if is_stack_empty():
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def peek():
    global SIZE, stack, top
    if is_stack_empty():
        return None
    return stack[top]


SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":

    stoneAry = ["주황", "초록", "파랑", "보라", "빨강", "노랑"]

    print("과자집에 가는길 : ", end=" ")
    for stone in stoneAry:
        push(stone)
        print(stone, "-->", end=" ")
    print("과자집")

    print("우리집에 오는길 : ", end=" ")
    while True:
        stone = pop()
        if stone == None:
            break
        print(stone, "-->", end=" ")
    print("우리집")


##------------------------------------------------##
    
SIZE = 100
stack = [ None for _ in range(SIZE) ]
top = -1

if __name__ == "__main__" :

	with open("진달래꽃.txt", 'r', encoding='UTF8') as rfp :
		lineAry = rfp.readlines()

	print("----- 원본 -----")
	for line in lineAry :
		push(line)
		print(line, end = ' ')
	print()

	print("----- 거꾸로 처리된 결과 -----")
	while True :
		line = pop()
		if line == None :
			break

		miniStack = [None for _ in range(len(line))]
		miniTop = -1

		for ch in line :
			miniTop += 1
			miniStack[miniTop] = ch

		while True :
			if miniTop == -1 :
				break
			ch = miniStack[miniTop]
			miniTop -= 1
			print(ch, end = ' ')
