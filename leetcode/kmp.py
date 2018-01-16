class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, t, p):
        # write your code here                
        if t==None or p==None:
            return -1

        def gen_pnext(p):
            i, k, m = 0, -1, len(p)
            pnext = [-1]*m
            while i < m-1:
                if k == -1 or p[i]==p[k]:
                    i, k = i+1, k+1
                    if p[i]==p[k]:
                        pnext[i] = pnext[k]
                    else:
                        pnext[i] = k
                else:
                    k = pnext[k]
            return pnext
        pnext=gen_pnext(p)
        j, i = 0, 0
        n, m = len(t), len(p)
        while j < n and i < m:
            if i == -1 or t[j] == p[i]:
                j, i = j+1, i+1
            else:
                i = pnext[i]
        if i==m:
            return j-i
        return -1
        