num_moves = 0


def print_move(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))


def towers(n, fr, to, spare):
    global num_moves
    if n == 1:
        print_move(fr, to)
        print fr, to, spare
        num_moves += 1
        print num_moves
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)

towers(10, 'f', 't', 's')
