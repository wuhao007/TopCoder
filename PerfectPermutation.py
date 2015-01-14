class PerfectPermutation:
    def reorder(self, P):
        pass

    def permutation(self, P):
        def helper(rst, path, num):
            if num:
                n = len(num)
                for i in range(n):
                    k = num.pop(i)
                    path += [k]
                    helper(rst, path, num)
                    num.insert(i, k)
                    path.pop()
            else:
                rst += [path[:]]
        rst = []
        helper(rst, [], P)
        return rst

    def perfect_permutation(self, A):
        Q = []
        for a in A:
            b = [0]
            perfect = True
            for i in range(1, len(a)):
                e = a[b[i - 1]]
                if e in b:
                    perfect = False    
                    break
                else:
                    b += [e]
            if perfect:
                Q += [a]
        return Q
pp = PerfectPermutation()                
A = pp.permutation([0, 1, 2, 3, 4])
print A
print pp.perfect_permutation(A)
