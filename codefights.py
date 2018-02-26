#!/usr/bin/python3

from collections import Counter


#https://codefights.com/arcade/python-arcade/caravan-of-collections/pE4t3DcoTRfwHwYG8 
def frequencyAnalysis(encryptedText):
    c = Counter(encryptedText)
    # print(c.most_common(1)[0][0])
    # print(c.elements)
    # print(c['C'])
    return c.most_common(1)[0][0]



def main():
    encryptedText = "$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ"
    print(frequencyAnalysis(encryptedText))
    return

if __name__ == '__main__':
    main()