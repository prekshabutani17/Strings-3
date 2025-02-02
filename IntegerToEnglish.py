"""
Time Complexity : O(1)
Space Complexity : O(1)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        self.below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",                     "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",                              "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",                    "Eighty", "Ninety"]
        
        self.thousands = ["", "Thousand", "Million", "Billion"]
        if num == 0:
            return "Zero"
        result = ""
        i = 0
        # First we start from last three digits if any in a number and accordingly
        # assign a string from thousands list and call a helper recursively on rest
        # and find their indices in the above arrays and their respective strings
        while num > 0:
            if num % 1000 != 0:
                result = self.helper(num%1000) + self.thousands[i] + " " + result
            num = num // 1000
            i += 1
        return result.strip()
    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20: return self.below_20[num] + " "
        elif num < 100: return self.tens[num // 10] + " " + self.helper(num % 10)
        else: return self.below_20[num // 100] + " Hundred " + self.helper(num%100)