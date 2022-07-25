from typing import List

class Solution:
    def add(cls, *args):
        pass

    def multiply(self, num1: str, num2: str) -> str:
        """
        Given two non-negative integers num1 and num2 represented as strings, 
        return the product of num1 and num2, also represented as a string.

        Note: You must not use any built-in BigInteger library or convert 
        the inputs to integer directly.
        """
        product = [0] * (len(num1) + len(num2))
        pos = len(product)-1
        
        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                product[tempPos] += int(n1) * int(n2)
                product[tempPos-1] += product[tempPos]//10
                product[tempPos] %= 10
                tempPos -= 1
            pos -= 1
            
        pt = 0
        while pt < len(product)-1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))


