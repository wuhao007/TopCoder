class LuckyXor:
    def construct(self, a):
        for b in range(a + 1, 101):
            n = a ^ b
            f = True
            for s in str(n):
                if s != '4' and s != '7':
                    f = False
                    break
            if f:
                return b
        return -1
luckyXor = LuckyXor()
print luckyXor.construct(4)
print luckyXor.construct(19)
print luckyXor.construct(88)
print luckyXor.construct(36)
                
