# Shallow Copy
a = [1, 2, 3]
b = a
b.append(4)
print(f'a: {a}, b: {b}')

arr1 = [1, 2, 3]
arr2 = arr1
arr1.append(4)
print(f'arr1: {arr1}, arr2: {arr2}')

arr3 = [1, 2, 3, [4, 5, 6]]
arr4 = arr3[:]
arr4.append(7)
arr3[3].append(88)
print(f'arr3: {arr3}, arr4: {arr4}') # The inner list is a shallow copy.

# Deep Copy
c = [1, 2, 3]
d = list(c)
d.append(4)
print(f'c: {c}, d: {d}')

# Copy method
e = [1, 2, 3]
f = e.copy()
f.append(4)
print(f'e: {e}, f: {f}')

import copy
print('=' * 50)

arr1 = [1, 2, [99, 88, 77], 3]
arr2 = copy.deepcopy(arr1)      # copy 모듈 깊은 복사

print("1. 전체 출력")
print(f'arr1 : {arr1}, address : {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')

print("\n2. 리스트에 새 value 추가")
arr1.append(0)
print('arr1.append(0)')
print(f'arr1 : {arr1}, address : {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')

print("\n3. 리스트 내부 리스트.")
print(f"arr1[2] : {arr1[2]}, address : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]}, address : {hex(id(arr2[2]))}")

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[2].append(10)
print("arr1[2].append(10)")
print(f"arr1[2] : {arr1[2]}, address : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]}, address : {hex(id(arr2[2]))}")

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, address : {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')
# 출처: https://blockdmask.tistory.com/576
