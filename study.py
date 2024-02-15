import random

def selectionSort(ary):
	for i in range(0, len(ary)-1):
		number = i	
		for k in range(i+1, len(ary)): # 가장 작은 수를 앞쪽에 배치했으므로 i+1부터 시작
			if ary[number] > ary[k]:
				number = k # find the index of the smallest number
		temp = ary[i] # 가장 작은 수를 앞쪽으로 옮기기 위해 임시로 저장
		ary[i] = ary[number] # 가장 작은 수를 앞쪽으로 옮김
		ary[number] = temp 
		# ary[i], ary[number] = ary[number], ary[i] # 다른 표현 방식
	return ary


## 전역 변수 선언 부분 ##
array = [random.randint(1, 200) for _ in range(10)]

## 메인 코드 부분 ##
print('정렬 전 -->', array)
dataAry = selectionSort(array)
print('정렬 후 -->', array)
