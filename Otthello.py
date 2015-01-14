'''
  A B C D E F G H       A B C D E F G H       A B C D E F G H       A B C D E F G H
1 - B - - B - B -     1 - B B - B - B -     1 - B B - B - B -     1 - B B - B - B - 
2 - - R - - R - -     2 - - B - - R - -     2 - - B - - R - -     2 - - B - - R - -
3 - - R - - R - -     3 - - B - - R - -     3 - - B - - R - -     3 - - B - - R - -
4 - - R R R R B - --> 4 - - B R R R B - --> 4 - - B B B B B - --> 4 - - B B B B B -
5 - - R - - R - -     5 - - B - - R - -     5 - - B - - R - -     5 - - B - - B - -
6 - - B - - - R -     6 - - B - - - R -     6 - - B - - - R -     6 - - B - - - B -
7 - - - - - - - B     7 - - - - - - - B     7 - - - - - - - B     7 - - - - - - - B
8 - - - - - - - -     8 - - - - - - - -     8 - - - - - - - -     8 - - - - - - - -
'''
class Tothello:
    def bestMove(redPieces, blackPieces, whoseTurn):
        matrix = [[0] * 8 for _ in range(8)]

        black_player = -1
        red_player = -1
        if whoseTurn == 'Black':
            black_player = 1
            red_player = 2
        else:
            black_player = 2
            red_player = 1
            

        def init_board(pieces, player, matrix):

            def convert2index(piece):
                return ord(piece[0]) - ord('A'), int(piece[1]) - 1

            for piece in pieces:
                row, col = convert2index(piece)
                matrix[row][col] = player
        
        player_1 = set()
        player_2 = set()

        init_board(redPieces, red_player, matrix, player_1, player_2)
        init_board(blackPieces, black_player, matrix, player_1, player_2)

        def search_possible_position(pieces):
            def dfs(piece, dx, dy):
                pass
            for piece in pieces:
                pass
