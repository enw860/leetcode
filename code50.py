class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
        """
        if n == 0:
            return float(1)
        elif n < 0:
            return 1 / self.myPow(x, -1 * n)

        return self.myPow(x * x, n/2) if n % 2 == 0 else x * self.myPow(x, n - 1)
            

if __name__ == "__main__":
    s = Solution()
    r = s.myPow(3.0, -3)
    print(r)