class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        import re
        from collections import defaultdict
        temps = list(filter(lambda c:c, re.split('([A-Z]{1}[a-z]?|\(|\)|\d+)', formula)))
        stack, i = [defaultdict(int)], 0
        while i < len(temps):
            temp = temps[i]
            if temp == '(' or temp == '[':
                stack.append(defaultdict(int))
            else:
                count = 1
                if i+1 < len(temps) and temps[i+1].isdigit():
                    count , i = int(temps[i+1]), i+1
                atoms = stack.pop() if temp==')' or temp==']' else {temp: 1}
                for atom in atoms:
                    stack[-1][atom] += atoms[atom]*count
            i += 1
        return "".join([atom + (str(count) if count > 1 else "") for atom, count in sorted(stack[-1].items())])
    
                    
        
