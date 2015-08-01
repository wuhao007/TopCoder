class BearCheats:
    def eyesight(self, A, B):
        a = str(A)
        b = str(B)
        n = len(a)
        flag = True
        for i in range(n):
            if a[i] != b[i]:
                if flag:
                    flag = False
                else:
                    return "glasses"
        return "happy"
bearCheats = BearCheats()
print bearCheats.eyesight(8072, 3072)
print bearCheats.eyesight(508, 540)
print bearCheats.eyesight(854000, 854000)
print bearCheats.eyesight(1, 6)
print bearCheats.eyesight(385900, 123000)


        
