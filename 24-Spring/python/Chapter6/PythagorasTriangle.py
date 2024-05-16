# 피타고라스의 정리를 만족하는 삼각형들을 모두 찾아보자.
# 삼각형 한 변의 길이는 1부터 30 이하이다.

# answer = []
# for x in range(1,31):
#     for y in range(1,31):
#         for z in range(1,31):
#             if x**2 + y**2 == z**2:
#                 answer.append((x,y,z))
# print(answer)

result = [
    (x,y,z) for x in range(1,31) for y in range(1,31) for z in range(1,31) if x**2 + y**2 == z**2
]
print(result)
