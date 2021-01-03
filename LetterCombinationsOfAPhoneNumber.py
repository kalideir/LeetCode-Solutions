class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hash = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        digits_arr = []
        for digit in digits:
            digits_arr.append(digit)
        print(digits_arr)
        correp_arr = [hash[digit] for digit in digits_arr]
        res = [f'{d1}{d2}' for arr in ]
        # incomplete
