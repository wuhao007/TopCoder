class PerfectPermutation:
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

    def reorder(self, P):
        def dfs(i, s):
            if i not in s:
                s.add(i)
                dfs(P[i], s)
        s = set()
        cnt = 0
        for i in range(len(P)):
            if i not in s:
                dfs(i, s)
                cnt += 1
        return 0 if cnt == 1 else cnt 

pp = PerfectPermutation()
print pp.reorder((0, 1, 2))
print pp.reorder((2, 0, 1))
print pp.reorder((2, 0, 1, 4, 3))
print pp.reorder((0, 5, 3, 2, 1, 4))
print pp.reorder((4, 2, 6, 0, 3, 5, 9, 7, 8, 1))
