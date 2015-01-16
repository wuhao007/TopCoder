class DifferentStrings:
    def minimize(self, A, B):
        mx = len(B)
        for j in range(len(B) - len(A) + 1):
            count = 0
            for i in range(len(A)):
                if A[i] != B[j + i]:
                    count += 1
            mx = min(count, mx)
        return mx
different_strings = DifferentStrings()
print different_strings.minimize("koder", "topcoder")
print different_strings.minimize("hello", "xello")
print different_strings.minimize("abc", "topabcoder")
print different_strings.minimize("adaabc", "aababbc")
print different_strings.minimize("giorgi", "igroig")
