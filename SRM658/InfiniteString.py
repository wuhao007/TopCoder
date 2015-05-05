class InfiniteString:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def equal(self, s, t):
        ls = len(s)
        lt = len(t)
        lg = self.gcd(ls, lt)
        gs = s[0:lg]
        gt = t[0:lg]
        if gs != gt:
            return "Not equal"
        elif s == gs * (ls / lg) and t == gt * (lt / lg):
            return "Equal"
        else:
            return "Not equal"
infiniteString = InfiniteString()
print infiniteString.gcd(1,5)
print infiniteString.gcd(5,1)
print infiniteString.gcd(15,2)
print infiniteString.equal("abc", "abcabc")
print infiniteString.equal("abc", "bca")
        
        
