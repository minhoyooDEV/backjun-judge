# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    # write your code in Python 3.6

    total = 0
    zero_count = 0

    for i in range(0, len(A)):
        temp_sum = A[i]

        # If sole element is zero
        if A[i] == 0:
            total += 1
            if zero_count > 0:
                total += zero_count
            zero_count += 1
            if total > 1000000000:
                return -1
        else:
            for j in range(i + 1, len(A)):
                temp_sum += A[j]

                if temp_sum == 0:
                    if zero_count == 0:
                        total += 1
                    else:
                        total += 1*zero_count

                    if total > 1000000000:
                        return -1

            zero_count = 0
    return total
