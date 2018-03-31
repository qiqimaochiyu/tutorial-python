class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self._min = 0

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        if not self.stack:
            self._min = number
            self.stack.append(number)
        else:
            if number <= self._min:
                self.stack.append(self._min)
                self._min = number
                self.stack.append(number)
            else:
                self.stack.append(number)
        

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.stack)==1:
            return self.stack.pop()
        else:
            if self.stack[len(self.stack)-1] == self._min:
                ans = self.stack.pop()
                self._min = self.stack.pop()
                return ans
            else:
                return self.stack.pop()
    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self._min
