#!/usr/bin/python3
import random
import time
import sys


def is_sorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

def edge_case1(a):
    descending = True
    for idx, val in enumerate(a[:-1]):
        if a[idx+1] > val:
            descending = False
            break
    if descending:
        print("Edge case!")
    return descending

def universityReportsSlow(a):
    # Complete this function
    if edge_case1(a):
        return len(a) - 1

    for size in range(1, len(a)):
        left_idx = 0
        left_not_sorted = False
        for idx, val in enumerate(a[left_idx:len(a)-size+1]):
            if left_not_sorted:
                break
            idx = idx + left_idx
            compare_sorted = a[left_idx:idx] + a[idx+size:]
            # print(compare_sorted)
            # print('removing sublist from {} to {}'.format(idx, idx+size))
            if not is_sorted(compare_sorted):
                continue
            print(compare_sorted)
            return size
def universityReports(a):
    if edge_case1(a):
        return len(a) - 1
    if a == sorted(a):
        return 0
    descending = []
    for idx, val in enumerate(a[:-1]):
        if a[idx+1] < val:
            descending.append(idx)
    print(descending)
    r = descending[-1]
    l = descending[0] + 1
    print(a[r])
    size = r - l + 1
    if a[r + 1] > a[l - 1]:
        return min([len(a) - 1, size])
    if r + 1 > len(a) - 1:
        return min([len(a) - 1, size])
    
    for idx, val in enumerate(a[r + 1:]):
        if idx == 0:
            if (r + 2 > len(a) - 1) or (l - 2 <= 0):
                return min([len(a) - 1, size + 1])
            continue
        print(idx,val)
        if (r + idx + 1 > len(a) - 1) or (l - idx - 1 <= 0):
            return min([len(a) - 1, size + idx])
        print('{}, {} should be index 4, 991'.format(l-1-idx, a[l-1-idx]))
        print('left: a[{}] = {} < {}'.format(l-1-idx, a[l - 1 - idx], a[r + 1]))
        print('right: a[{}] = {} > {}'.format(idx, val, a[l-1]))
        if (val > a[l - 1]) or (a[l - 1 - idx] < a[r + 1]):
            return min([len(a) - 1, size + idx])
    print(len(a))
    return min([len(a) - 1, size + idx + 1])
    
"""
input:
1
4
4 3 2 1

1
5
2 3 1 5 4
"""
def main():
    # a_random_input = random.sample(range(1,10001), 10000)
    # a_random_input = random.sample(range(1,1000), 999)
    # print('1')
    # print(len(a_random_input))
    # print(' '.join(list(map(str, a_random_input))))
    # return
    t = int(input().strip())
    for a0 in range(0,2,t*2):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        # a = sorted(a)[:20] + a[21:24] + sorted(a)[24:]
        start = time.time()
        result = 'ANSWER: {}'.format(universityReportsSlow(a))
        end = time.time()
        print(result)
        print(end - start)

        start = time.time()
        result = 'ANSWER: {}'.format(universityReports(a))
        end = time.time()
        print(result)
        print(end - start)
    return

if __name__ == "__main__":
    main()
