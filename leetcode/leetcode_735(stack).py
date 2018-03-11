class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        for a in asteroids:
            if len(res) == 0 or a > 0:
                res.append(a)
            elif a < 0:
                while len(res) and res[-1] > 0:
                    if res[-1] == -a:
                        res.pop()
                        break
                    elif res[-1] + a < 0:
                        res.pop()
                        continue
                    elif res[-1] + a > 0:
                        break
                else:
                    res.append(a)
        return res
        
