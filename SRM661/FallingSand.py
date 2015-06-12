class FallingSand:
    def simulate(self, board):
        height = len(board)
        width = len(board[0])
        result = [[col for col in row] for row in board]
        for col in range(width):
            i = 0
            j = 0
            while i <= height:
                if i == height or result[i][col] == 'x':
                    k = i - 1
                    while j < k:
                        if result[j][col] != 'o':
                            j += 1 
                        elif result[k][col] != '.':
                            k -= 1
                        else:
                            result[k][col] = 'o'
                            result[j][col] = '.'
                            k -= 1
                            j += 1
                    j = i + 1
                i += 1
        return tuple([''.join(row) for row in result])
fallingSand = FallingSand()
print fallingSand.simulate(("..o..", "..x.o", "....x", ".....", "oo.oo")) == ("..o..", "..x.o", "....x", ".....", "oo.oo")
print fallingSand.simulate(("ooooxooo.ooxo.oxoxoooox.....x.oo")) == ("ooooxooo.ooxo.oxoxoooox.....x.oo")
print fallingSand.simulate(("o", ".", "o", ".", "o", ".", ".")) == (".", ".", ".", ".", "o", "o", "o")
print fallingSand.simulate(("oxxxxooo", "xooooxxx", "..xx.ooo", "oooox.o.", "..x.....")) == ("oxxxxooo", "x.oo.xxx", "..xxo...", ".oo.x.o.", "ooxo.ooo" )
print fallingSand.simulate( ("..o..o..o..o..o..o..o..o..o..o..o", "o..o..o..o..o..o..o..o..o..o..o..", ".o..o..o..o..o..o..o..o..o..o..o.", "...xxx...xxx...xxxxxxxxx...xxx...", "...xxx...xxx...xxxxxxxxx...xxx...", "...xxx...xxx......xxx......xxx...", "...xxxxxxxxx......xxx......xxx...", "...xxxxxxxxx......xxx......xxx...", "...xxxxxxxxx......xxx......xxx...", "...xxx...xxx......xxx............", "...xxx...xxx...xxxxxxxxx...xxx...", "...xxx...xxx...xxxxxxxxx...xxx...", "..o..o..o..o..o..o..o..o..o..o..o", "o..o..o..o..o..o..o..o..o..o..o..", ".o..o..o..o..o..o..o..o..o..o..o.")) == (".................................", ".................................", "...ooo...ooo...ooooooooo...ooo...", "...xxx...xxx...xxxxxxxxx...xxx...", "...xxx...xxx...xxxxxxxxx...xxx...", "...xxxoooxxx......xxx......xxx...", "...xxxxxxxxx......xxx......xxx...", "...xxxxxxxxx......xxx......xxx...", "...xxxxxxxxx......xxx......xxx...", "...xxx...xxx......xxx............", "...xxx...xxx...xxxxxxxxx...xxx...", "...xxx...xxx...xxxxxxxxx...xxx...", ".................................", "ooo.........ooo.........ooo...ooo", "ooooooooooooooooooooooooooooooooo" )
        
        
        
