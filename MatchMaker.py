class MatchMaker:
    def getBestMatches(self, members, currentUser, sf):
        current_gender = ''
        current_request = ''
        current_answers = []
        for member in members:
            element = member.split()
            if element[0] == currentUser:
                current_gender = element[1]
                current_request = element[2]
                current_answers += element[3:]
                break
        tmp = {}
        for member in members:
            element = member.split()
            if element[0] != currentUser:
                if current_request == element[1]:
                    score = 0
                    for i in range(len(current_answers)):
                        if current_answers[i] == element[3 + i]:
                            score += 1
                    if score >= sf:
                        if score in tmp:
                            tmp[score] += [element[0]]
                        else:
                            tmp[score] = [element[0]]
        ret = []
        for key in sorted(tmp.keys(), key = lambda x : -x):
            ret += tmp[key]
        return tuple(ret)
             
match_maker = MatchMaker()
members = ("BETTY F M A A C C", "TOM M F A D C A", "SUE F M D D D D", "ELLEN F M A A C A", "JOE M F A A C A", "ED M F A D D A", "SALLY F M C D A B", "MARGE F M A A C C")
print match_maker.getBestMatches(members, "BETTY", 2)
print match_maker.getBestMatches(members, "JOE", 1)
print match_maker.getBestMatches(members, "MARGE", 4)
print match_maker.getBestMatches(("BETTY F M A A C C", "TOM M F A D C A", "SUE F M D D D D", "ELLEN F M A A C A", "JOE M F A A C A", "ED M F A D D A", "SALLY F M C D A B", "MARGE F M A A C C"), "BETTY", 2)
print match_maker.getBestMatches(("BETTY F M A A C C", "TOM M F A D C A", "SUE F M D D D D", "ELLEN F M A A C A", "JOE M F A A C A", "ED M F A D D A", "SALLY F M C D A B", "MARGE F M A A C C"), "JOE", 1)
                
