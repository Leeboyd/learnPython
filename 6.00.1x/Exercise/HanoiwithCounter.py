def Hanoi(n, fr, tem, to):
    '''
    n: int, 盤子數.
    fr: string, 初始柱子
    tem: string, 暫存的柱子
    to: string, 目標柱子
    '''
    global stepCount

    if n > 0:
        # step 1: 將 n - 1 個移到暫存
        Hanoi(n - 1, fr, to, tem)
        stepCount += 1

        # step 2: 將最後一格移動到目標
        # Hanoi(1, fr, tem, to)
        print('stepCount: {}'.format(stepCount))
        print('{} --> {}'.format(fr, to))

        # step 3: 將 n - 1 個從暫存移動到目標
        Hanoi(n - 1, tem, fr, to)

stepCount = 0
print(Hanoi(3, 'A', 'B', 'C'))