#!/usr/bin/python3
import random
import time
import sys

def universityReports(a):
    # Complete this function
    descending = True
    for idx, val in enumerate(a[:-1]):
        if a[idx+1] > val:
            descending = False
            break
    if descending:
        return len(a) - 1
    for size in range(len(a) - 1):
        for idx, val in enumerate(a):
            compare_sorted = a[0:idx] + a[idx+size:]
            # slow
            # if compare_sorted == sorted(compare_sorted):
            #     return size
            min_val = a[0]
            found = True
            # print(idx, val)
            for idx, val in enumerate(compare_sorted[:-1]):
                if (val < min_val) or (compare_sorted[idx+1] < val):
                    found = False
                    break
            if found:
                print('Found answer at index {}, value {}'.format(idx, val))
                return size

    print("ERROR, fix ur algorithm!!")
    return

"""
input:
1
4
4 3 2 1
"""
def main():
    # a_random_input = random.sample(range(1,1000000000), 10000)
    # a_random_input = random.sample(range(1,445), 444)
    # print('1')
    # print(len(a_random_input))
    # print(' '.join(list(map(str, a_random_input))))
    # return
    t = int(input().strip())
    for a0 in range(0,2,t*2):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        start = time.time()
        result = universityReports(a)
        end = time.time()
        print(result)
        print(end - start)
    return

if __name__ == "__main__":
    main()
