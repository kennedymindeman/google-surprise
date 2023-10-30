from solution_for_python2 import get_tile, get_valid_next_tiles, make_board, solution, tile_in_board


def test_board():
    board = make_board(8, 8)
    assert board[7][7] == 63
    assert board[0][0] == 0
    assert len(board) == 8
    assert set(map(len, board)) == {8}


def test_get_tile():
    board = make_board(8, 8)
    assert get_tile(8, board) == (1, 0)
    assert get_tile(3, board) == (0, 3)
    assert get_tile(63, board) == (7, 7)


def test_tile_in_board():
    board = make_board(8, 8)
    assert tile_in_board((7, 7), board)
    assert not tile_in_board((8, 7), board)
    assert not tile_in_board((7, 8), board)
    assert not tile_in_board((-1, 3), board)
    assert tile_in_board((0, 0), board)


def test_find_next_tile_options():
    board = make_board(8, 8)
    tile = (3, 3)
    next_moves = {(1, 2), (1, 4), (5, 2), (5, 4), (2, 1), (2, 5), (4, 1), (4, 5)}
    assert get_valid_next_tiles(tile, board) == next_moves

    tile = (0, 0)
    assert len(get_valid_next_tiles(tile, board)) == 2


def test_solution():
    board = make_board(8, 8)
    assert solution(19, 36) == 1
    assert solution(0, 1) == 3
    assert solution(5, 5) == 0



test_board()
test_get_tile()
test_tile_in_board()
test_find_next_tile_options()
test_solution()
