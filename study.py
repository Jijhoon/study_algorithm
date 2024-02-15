import random


## 함수 선언 부분 ##
def quickSort(ary):
    n = len(ary)
    if n <= 1:  # 정렬할 리스트의 개수가 1개 이하면
        return ary

    pivot = ary[n // 2]  # 기준값을 중간 값으로 지정
    leftAry, midAry, rightAry = [], [], []
    print("pivot-->", pivot)
    for num in ary:  # 기준값보다 작으면 leftAry, 크면 rightAry, 같으면 midAry에 추가
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
        else:
            midAry.append(num)

    return quickSort(leftAry) + midAry + quickSort(rightAry)


## 전역 변수 선언 부분 ##
dataAry = [random.randint(1, 200) for _ in range(10)]

## 메인 코드 부분 ##
print("정렬 전 -->", dataAry)
dataAry = quickSort(dataAry)
print("정렬 후 -->", dataAry)
# 27 83 44 11 159 94 74 147 171 // 190
# 27 83 44 11 94 74 147 // 159 // 171 // 190
# 11 // 27 83 44 94 74 147 // 159 // 171 // 190
# 11 // 27 83 44 74 // 94 // 147 // 159 // 171 // 190
# 11 // 27 // 44 // 83 74 // 94 // 147 // 159 // 171 // 190
# 11 // 27 // 44 // 74 // 83 // 94 // 147 // 159 // 171 // 190
