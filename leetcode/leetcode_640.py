class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        s = eval(equation.replace('x', 'j').replace('=','-(') + ')', {'j':1j})
        a, b = s.real, s.imag
        return 'x=%d' %-(a/b) if b else 'No solution' if a else 'Infinite solutions' 