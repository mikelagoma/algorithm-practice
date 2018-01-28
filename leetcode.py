# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#!/usr/bin/python
class Solution:
    digit_letter_map = {
        0 : [],
        1 : [],
        2 : ['a', 'b', 'c'],
        3 : ['d', 'e', 'f'],
        4 : ['g', 'h', 'i'],
        5 : ['j', 'k', 'l'],
        6 : ['m', 'n', 'o'],
        7 : ['p', 'q', 'r', 's'],
        8 : ['t', 'u', 'v'],
        9 : ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        buildup = list()
        digits = [int(d) for d in digits]
        for digit in digits:
            if not buildup:
                buildup = Solution.digit_letter_map[digit]
            else:
                new_buildup = list()
                for b in buildup:
                    new_buildup = [b + letter for letter in Solution.digit_letter_map[digit]]
                buildup = new_buildup
        return buildup

def main():
    s = Solution()
    print(s.letterCombinations('23'))

if __name__ == '__main__':
    main()