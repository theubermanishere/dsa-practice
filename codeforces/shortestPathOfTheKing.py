s = str(input())
t = str(input())



def calculateMoves(s,t):
    # Input parsing
    cols = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    sx = cols[s[0]]
    sy = int(s[1])
    tx = cols[t[0]]
    ty = int(t[1])

    # Calculating moves
    moves = []
    while True:
        xflag = 0
        yflag = 0
        xmove = ''
        ymove = ''
        move = ''
        if sx != tx:
            xflag = 1
            if sx < tx:
                xmove = 'R'
                sx = sx + 1
            else:
                xmove = 'L'
                sx = sx - 1
        if sy != ty:
            yflag = 1
            if sy < ty:
                ymove = 'U'
                sy = sy + 1
            else:
                ymove = 'D'
                sy = sy - 1
        if xflag: move = move + xmove
        if yflag: move = move + ymove
        if (not xflag and not yflag):
            break
        else:
            moves.append(move)

    # Output Parsing
    print(len(moves))
    for i in moves:
        print(i)
    return



calculateMoves(s,t)
