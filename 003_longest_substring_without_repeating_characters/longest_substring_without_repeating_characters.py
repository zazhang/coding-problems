class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        lastRepeating = -1
        longestSubstring = 0
        positions = {}
        for i in range(0, len(s)):
            #print 'step %s' % i
            if s[i] in positions and lastRepeating < positions[s[i]]:
                lastRepeating = positions[s[i]]
                #print 'lastrepeating is %s' % lastRepeating
            if i-lastRepeating > longestSubstring:
                longestSubstring = i-lastRepeating
                #print longestSubstring
            positions[s[i]] = i
        return longestSubstring

    def lengthOfLongestSubstring1(self, s):  ## still have problems, can only identify nonrepeat characters not substring
        nonrepeatlist = list()
        repeatlist = list()
        table = dict()
        for i in range(0, len(s)):
            if i > 0 and s[i] not in table:
                nonrepeatlist.append(s[i])
            elif i > 0 and s[i] in table:
                repeatlist.append(s[i])
            else:
                nonrepeatlist.append(s[i])
            table[s[i]] = i
        return len(nonrepeatlist)


if __name__ == "__main__":
    a = Solution()
    print a.lengthOfLongestSubstring('pwwkew')
