# 1 0 1 0 1
#   0 1 0 1
#     1 0 1
#       0 1
#         1


for i in range(5,0,-1):
    for s in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print((j + 1)% 2,end=" ")
    print()
