def printMove(fr, to):
    print(str(fr) + '-->' + str(to))

def Hanoi(n, fr, tem, to):
    '''
    n: int, 盤子數.
    fr: string, 初始柱子
    tem: string, 暫存的柱子
    to: string, 目標柱子
    '''
    if n == 1:
        printMove(fr, to)
    elif n == 0:
        print('no disk')
    else:
        Hanoi(n - 1, fr, to, tem)
        Hanoi(1, fr, tem, to)
        Hanoi(n - 1, tem, fr, to)

print(Hanoi(0, 'A', 'B', 'C'))