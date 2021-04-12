# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://www.programmersought.com/article/82496639663/

def solution(A, X, Y, Z):

    maxX = 0
    maxY = 0
    maxZ = 0
    time = 0

    maxD = max(X, Y, Z)

    data = {}

    while True:
        for i, car in enumerate(A):
            if car != 0 and car <= X and time >= maxX:
                X -= car
                data[i] = time
                maxX += car
                A[i] = 0
                break

        for i, car in enumerate(A):
            if car != 0 and car <= Y and time >= maxY:
                Y -= car
                data[i] = time
                maxY += car
                A[i] = 0
                break

        for i, car in enumerate(A):
            if car != 0 and car <= Z and time >= maxZ:
                Z -= car
                data[i] = time
                maxZ += car
                A[i] = 0
                break

        time += 1

        if time > maxD:
            break

    if len(data) != len(A):
        return -1

    return data[len(A)- 1]

