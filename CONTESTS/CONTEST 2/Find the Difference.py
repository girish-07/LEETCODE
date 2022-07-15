class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr = [i for i in t if i not in s or t.count(i)!=s.count(i)]
        return str(arr[0])
