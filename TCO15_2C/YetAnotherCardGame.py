class YetAnotherCardGame:
    def maxCards(self, petr, snuke):
        petr_s = sorted(petr)
        snuke_s = sorted(snuke)
        cnt = 0
        previous = -1
        turn = True
        while len(petr_s) > 0 and len(snuke_s) > 0:
            if turn:
                if petr_s:
                    p = petr_s[0]
                    if p > previous:
                        if snuke_s:
                            s = snuke_s[0]
                            if p > s:
                                if p > petr_s[-1]:
                                    petr_s.pop()
                                    continue
                        petr_s.pop(0)
                        cnt += 1
                        previous = p
                    else:
                        petr_s += [p]
                        petr_s.pop(0)
                else:
                    break
            else:
                if snuke_s:
                    s = snuke_s[0]
                    if s > previous:
                        if petr_s:
                            p = petr_s[0]
                            if s > p:
                                if s > snuke_s[-1]:
                                    snuke_s.pop()
                                    continue
                        snuke_s.pop(0)
                        cnt += 1
                        previous = s
                    else:
                        snuke_s += [s]
                        snuke_s.pop(0)
                else:
                    break
            turn = not turn
        return cnt
yetAnotherCardGame = YetAnotherCardGame()
print yetAnotherCardGame.maxCards((2, 5), (3, 1))
print
print yetAnotherCardGame.maxCards((1,1,1,1,1), (1,1,1,1,1))
print
print yetAnotherCardGame.maxCards((1,4,6,7,3), (1,7,1,5,7))
print
