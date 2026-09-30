class Solution(object):
    def numberOfSubstrings(self, s):

        last = {'a': -1, 'b': -1, 'c': -1}
        count = 0

        for i in range(len(s)):
            last[s[i]] = i
            count += min(last['a'], last['b'], last['c']) + 1

        return count
