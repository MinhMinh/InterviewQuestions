import collections

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, words):
        words.append(start)
        words.append(end)
        n = len(start)
        d = {}
        
        for w in words:
            d[w] = 0;
        d[start] = 1;
              
        q = collections.deque()
        q.append(start)
        
        while len(q) > 0:
            s = q.popleft()
            chars = list(s)
            for i in range(n):
                head = ''.join(chars[0:i])
                tail = ''.join(chars[i + 1:n])
                
                for j in range(ord('a'), ord('z')):
                     t = head + chr(j) + tail
                     if t in d and d[t] == 0:
                        d[t] = d[s] + 1
                        q.append(t)
                        if t == end: return d[t]
                        
        return 0
                        
                
S = Solution()
print S.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])  
              
      
        
