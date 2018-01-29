class Solution(object):
    """ Point:
          palindromic number: A palindromic number or numeral palindrome is a number that remains the same when its digits are reversed.
    """
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        s = str(x)
        sum = len(s)
        n =  sum / 2
        for i in range(n):
            if s[i] != s[sum-i-1]:
                return False
        return True
