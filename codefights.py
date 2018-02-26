#!/usr/bin/python3

from collections import Counter
from itertools import cycle

#https://codefights.com/arcade/python-arcade/caravan-of-collections/pE4t3DcoTRfwHwYG8 
def frequencyAnalysis(encryptedText):
    c = Counter(encryptedText)
    # print(c.most_common(1)[0][0])
    # print(c.elements)
    # print(c['C'])
    return c.most_common(1)[0][0]

def cyclicName(name, n):
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)


def main():
    # encryptedText = "$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ"
    # print(frequencyAnalysis(encryptedText))
    print(cyclicName('nicecoder', 15))
    return

if __name__ == '__main__':
    main()