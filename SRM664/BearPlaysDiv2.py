class BearPlaysDiv2:
    def equalPiles(self, A, B, C):
        mem = set()
        def equalPile(a, b, c):
            if a == b == c:
                return True
            elif tuple(sorted([a, b, c])) in mem:
                return False
            else:
                mem.add(tuple(sorted([a, b, c])))
                ab = False
                if b > a:
                    ab = equalPile(2 * a, b - a, c) 
                elif a > b:
                    ab = equalPile(a - b, 2 * b, c)
                if ab:
                    return True
                bc = False
                if c > b:
                    bc = equalPile(a, 2 * b, c - b) 
                elif b > c: 
                    bc = equalPile(a, b - c, 2 * c)
                if bc:
                    return True
                ac = False
                if c > a:
                    ac = equalPile(2 * a, b, c - a) 
                elif a > c:
                    ac = equalPile(a - c, b, 2 * c)
                if ac:
                    return True
                return ab or ac or bc
        if equalPile(A, B, C):
            return "possible"
        else:
            return "impossible"        
bearPlaysDiv2 = BearPlaysDiv2()
print bearPlaysDiv2.equalPiles(10, 15, 35)
print bearPlaysDiv2.equalPiles(1, 1, 2)
print bearPlaysDiv2.equalPiles(4, 6, 8)
print bearPlaysDiv2.equalPiles(18, 18, 18)
print bearPlaysDiv2.equalPiles(225, 500, 475)
