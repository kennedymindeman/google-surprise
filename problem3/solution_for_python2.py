def solution(start, end):
    board = make_board(8, 8)
    start_tile = get_tile(start, board)
    end_tile = get_tile(end, board)

    depth = 0
    checked_tiles = {start_tile}
    while end_tile not in checked_tiles:
        depth += 1
        next_tiles = set()
        for tile in checked_tiles:
            next_tiles = next_tiles.union(get_valid_next_tiles(tile, board))

        checked_tiles = next_tiles

    return depth


def make_board(num_rows, num_cols):
    board = []
    for row_num in range(num_rows):
        row_start = row_num * num_cols
        row_end = row_start + num_cols
        board.append(list(range(row_start, row_end)))

    return board


def get_tile(value, board):
    for row_num, row in enumerate(board):
        if value in row:
            return row_num, row.index(value)

    raise ValueError("{} not in board: {}".format(value, board))


def get_valid_next_tiles(current_tile, board):
    options = get_next_tile_options(current_tile)
    return {tile for tile in options if tile_in_board(tile, board)}


def tile_in_board(tile, board):
    row_num, col_num = tile
    if row_num not in range(len(board)):
        return False

    return col_num in range(len(board[row_num]))


def get_next_tile_options(tile):
    def find_tile(row_offset, col_offset):
        row_num, col_num = tile
        return row_num + row_offset, col_num + col_offset

    next_tile_options = []
    for row_offset in [-2, 2]:
        options = [find_tile(row_offset, col_offset) for col_offset in [-1, 1]]
        next_tile_options.extend(options)

    for row_offset in [-1, 1]:
        options = [find_tile(row_offset, col_offset) for col_offset in [-2, 2]]
        next_tile_options.extend(options)

    return set(next_tile_options)
