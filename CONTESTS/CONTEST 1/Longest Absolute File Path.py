class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        pathlen = {0:0}
        for l in input.splitlines():
            name = l.lstrip('\t')
            depth = len(l)-len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth]+len(name))
            else:
                pathlen[depth+1]=pathlen[depth]+len(name)+1
        return maxlen
