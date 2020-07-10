class Solution():
    def getNext(self, p):

        pLen = len(p)
        k = -1
        j = 0
        nextP = [0]

        while j < pLen - 1:
            if k == -1 or p[j] == p[k]:
                k = k + 1
                j = j + 1

                if p[j] != p[k]:
                    nextP.append(k)
                else:
                    nextP.append(nextP[k])
            else:
                k = nextP[k]
        return nextP

    def KmpSearch(self, s, p, nextP):
        i = 0
        j = 0
        sLen = len(s)
        pLen = len(p)

        while i < sLen and j < pLen:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = nextP[j]
        if j == pLen:
            return i - j
        else:
            return -1


if __name__ == '__main__':
    a = Solution()

    s = 'BBC ABCDAB ABCDABCDABDE'
    p = 'ABCDABD'

    nextP = a.getNext(p)
    print(nextP)

    position = a.KmpSearch(s, p, nextP)
    print(position)
