class ChessFloor:
    def minimumChanges(self, floor):
        def countColor(A, B, colTurn):
            if colTurn:
                if color in A:
                    A[color] += 1
                else:
                    A[color] = 1
            else:
                if color in B:
                    B[color] += 1
                else:
                    B[color] = 1
        def topTwo(colors):
            mx = 0
            topI = None
            topII = None
            for key, value in colors.items():
                if value >= mx:
                    mx = value
                    topII  = topI
                    topI = key
            return topI, topII
        one = {}
        two = {}
        rowTurn = True
        colTurn = True
        for row in floor:
            for color in row:
                countColor(one, two, colTurn)
                colTurn = not colTurn
            rowTurn = not rowTurn
            colTurn = rowTurn
        oneCnt = sum(one.values())
        twoCnt = sum(two.values())
        oneI, oneII = topTwo(one)
        twoI, twoII = topTwo(two)
        if oneI != twoI:
            return (oneCnt - one[oneI]) + (twoCnt - two[twoI]) 
        elif oneII == None and twoII == None:
            return min(oneCnt, twoCnt)
        elif oneII == None:
            return (oneCnt - one[oneI]) + (twoCnt - two[twoII]) 
        elif twoII == None:
            return (oneCnt - one[oneII]) + (twoCnt - two[twoI]) 
        else:
            return min((oneCnt - one[oneII]) + (twoCnt - two[twoI]), (oneCnt - one[oneI]) + (twoCnt - two[twoII]))
            
chessFloor = ChessFloor()
print chessFloor.minimumChanges(("aba", "bbb", "aba"))
print chessFloor.minimumChanges(("wbwbwbwb", "bwbwbwbw", "wbwbwbwb", "bwbwbwbw", "wbwbwbwb", "bwbwbwbw", "wbwbwbwb", "bwbwbwbw"))
print chessFloor.minimumChanges(("zz", "zz"))
print chessFloor.minimumChanges(("helloand", "welcomet", "osingler", "oundmatc", "hsixhund", "redandsi", "xtythree", "goodluck"))
print chessFloor.minimumChanges(("jecjxsengslsmeijrmcx", "tcfyhumjcvgkafhhffed", "icmgxrlalmhnwwdhqerc", "xzrhzbgjgabanfxgabed", "fpcooilmwqixfagfojjq", "xzrzztidmchxrvrsszii", "swnwnrchxujxsknuqdkg", "rnvzvcxrukeidojlakcy", "kbagitjdrxawtnykrivw", "towgkjctgelhpomvywyb", "ucgqrhqntqvncargnhhv", "mhvwsgvfqgfxktzobetn", "fabxcmzbbyblxxmjcaib", "wpiwnrdqdixharhjeqwt", "xfgulejzvfgvkkuyngdn", "kedsalkounuaudmyqggb", "gvleogefcsxfkyiraabn", "tssjsmhzozbcsqqbebqw", "ksbfjoirwlmnoyyqpbvm", "phzsdodppzfjjmzocnge"))
