from datetime import datetime

_row = list(range(8))
CHESS_BOARD = []
for _i in range(8):
	CHESS_BOARD.append([8 * _i + element for element in _row])

DOWN2LEFT1 = -17  # row >= 2, column >= 1
DOWN2RIGHT1 = -15  # row >= 2, column <= 6
DOWN1LEFT2 = -10  # row >= 1, column >= 2
DOWN1RIGHT2 = -6  # row >= 1, column <= 5
UP1LEFT2 = 6  # row <= 6, column >= 2
UP1RIGHT2 = 10  # row <= 6, column <= 5
UP2LEFT1 = 15  # row <= 5, column >= 1
UP2RIGHT1 = 17  # row <= 5, column <= 6

ALLOWED_MOVES = [DOWN2LEFT1, DOWN2RIGHT1, DOWN1LEFT2, DOWN1RIGHT2, UP1LEFT2, UP1RIGHT2, UP2LEFT1, UP2RIGHT1]


def is_valid_move(source, move):
	if not isinstance(source, int):
		raise ValueError('{} must be int.'.format(source))
	if not isinstance(move, int):
		raise ValueError('{} must be int.'.format(move))
	if not(0 <= source <= 63):
		return False
	new_destination = source + move
	if not(0 <= new_destination <= 63):
		return False
	if move not in ALLOWED_MOVES:
		return False
	row, column = find_location(source)
	if move == 17 and row <= 5 and column <= 6:
		return True
	if move == 15 and row <= 5 and column >= 1:
		return True
	if move == 10 and row <= 6 and column <= 5:
		return True
	if move == 6 and row <= 6 and column >= 2:
		return True
	if move == -6 and row >= 1 and column <= 5:
		return True
	if move == -10 and row >= 1 and column >= 2:
		return True
	if move == -15 and row >= 2 and column <= 6:
		return True
	if move == -17 and row >= 2 and column >= 1:
		return True
	return False


def get_proximity_move(source, destination):
	if not isinstance(source, int):
		raise ValueError('{} must be int.'.format(source))
	if not isinstance(destination, int):
		raise ValueError('{} must be int.'.format(destination))
	distance = destination - source
	moves = []
	for move in ALLOWED_MOVES:
		new_source = source + move
		new_distance = destination - new_source
		if (new_distance in ALLOWED_MOVES or new_distance == 0) and is_valid_move(source, move) and is_valid_move(new_source, new_distance):
			moves.append(move)
	if moves:
		if distance < 0:
			return min(moves)
		return max(moves)
	return None


def pick_next_move(source, destination):
	if not isinstance(source, int):
		raise ValueError('{} must be int.'.format(source))
	if not isinstance(destination, int):
		raise ValueError('{} must be int.'.format(destination))
	row, column = find_location(source)
	destination_row, destination_column = find_location(destination)
	distance = destination - source
	
	for move in ALLOWED_MOVES:
		if distance == move and is_valid_move(source, move):
			return move
	
	if distance == 0:
		return 0
	if row == destination_row:
		if distance == 7:
			if is_valid_move(source, UP2RIGHT1):
				return UP2RIGHT1
			if is_valid_move(source, UP1RIGHT2):
				return UP1RIGHT2
			if is_valid_move(source, DOWN2RIGHT1):
				return DOWN2RIGHT1
			if is_valid_move(source, DOWN1RIGHT2):
				return DOWN1RIGHT2
		if distance == 6:
			if is_valid_move(source, UP1RIGHT2):
				return UP1RIGHT2
			if is_valid_move(source, DOWN1RIGHT2):
				return DOWN1RIGHT2
		if distance == 5:
			if is_valid_move(source, UP1RIGHT2):
				return UP1RIGHT2
			if is_valid_move(source, DOWN1RIGHT2):
				return DOWN1RIGHT2
		if distance == 4:
			if is_valid_move(source, UP1RIGHT2):
				return UP1RIGHT2
			if is_valid_move(source, DOWN1RIGHT2):
				return DOWN1RIGHT2
		if distance == 3:
			if is_valid_move(source, UP1RIGHT2):
				return UP1RIGHT2
			if is_valid_move(source, DOWN1RIGHT2):
				return DOWN1RIGHT2
		if distance == 2:
			if is_valid_move(source, UP2RIGHT1):
				return UP2RIGHT1
			if is_valid_move(source, DOWN2RIGHT1):
				return DOWN2RIGHT1
		if distance == 1:
			if is_valid_move(source, UP2RIGHT1):
				return UP2RIGHT1
			if is_valid_move(source, DOWN2RIGHT1):
				return DOWN2RIGHT1
		if distance == -1:
			if is_valid_move(source, UP2LEFT1):
				return UP2LEFT1
			if is_valid_move(source, DOWN2LEFT1):
				return DOWN2LEFT1
		if distance == -2:
			if is_valid_move(source, UP2LEFT1):
				return UP2LEFT1
			if is_valid_move(source, DOWN2LEFT1):
				return DOWN2LEFT1
		if distance == -3:
			if is_valid_move(source, UP1LEFT2):
				return UP1LEFT2
			if is_valid_move(source, DOWN1LEFT2):
				return DOWN1LEFT2
		if distance == -4:
			if is_valid_move(source, UP1LEFT2):
				return UP1LEFT2
			if is_valid_move(source, DOWN1LEFT2):
				return DOWN1LEFT2
		if distance == -5:
			if is_valid_move(source, UP1LEFT2):
				return UP1LEFT2
			if is_valid_move(source, DOWN1LEFT2):
				return DOWN1LEFT2
		if distance == -6:
			if is_valid_move(source, UP1LEFT2):
				return UP1LEFT2
			if is_valid_move(source, DOWN1LEFT2):
				return DOWN1LEFT2
		if distance == -7:
			if is_valid_move(source, DOWN2LEFT1):
				return DOWN2LEFT1
			if is_valid_move(source, UP1LEFT2):
				return UP1LEFT2
			if is_valid_move(source, DOWN1LEFT2):
				return DOWN1LEFT2
	move = get_proximity_move(source, destination)
	if move is not None:
		return move
	moves = []
	for move in ALLOWED_MOVES:
		new_source = source + move
		new_distance = destination - new_source
		if is_valid_move(source, move) and get_proximity_move(new_source, destination) is not None and 0 < new_distance <= 63:
			moves.append(move)
	if moves:
		if distance < 0:
			return min(moves)
		return max(moves)
	if distance > 17 and is_valid_move(source, UP2RIGHT1):
		return UP2RIGHT1
	if distance > 15 and is_valid_move(source, UP2LEFT1):
		return UP2LEFT1
	if distance > 10 and is_valid_move(source, UP1RIGHT2):
		return UP1RIGHT2
	if distance > 6 and is_valid_move(source, UP1LEFT2):
		return UP1LEFT2
	if distance < -17 and is_valid_move(source, DOWN2LEFT1):
		return DOWN2LEFT1
	if distance < -15 and is_valid_move(source, DOWN2RIGHT1):
		return DOWN2RIGHT1
	if distance < -10 and is_valid_move(source, DOWN1LEFT2):
		return DOWN1LEFT2
	if distance < -6 and is_valid_move(source, DOWN1RIGHT2):
		return DOWN1RIGHT2
	if distance > 0:
		possible_goals = [17, 15, 10, 6]
	else:
		possible_goals = [-17, -15, -10, -6]
	for move in possible_goals:
		new_source = source + move
		new_row, new_column = find_location(new_source)
		new_distance = destination - new_source
		if new_row == destination_row and is_valid_move(source, move) and -6 < new_distance < 6:
			moves.append(move)
	if moves:
		if distance < 0:
			return min(moves)
		return max(moves)


def find_location(value):
	if not isinstance(value, int):
		raise ValueError('{} must be int.'.format(value))
	return [value / 8, value % 8]


def solution(src, dest):
	if not isinstance(src, int) or not isinstance(dest, int) or 0 > src >= 64 or 0 > dest >= 64:
		return -1
	if src == dest:
		return 0
	moves = 0
	new_src = src
	while new_src != dest:
		new_src += pick_next_move(new_src, dest)
		print new_src
		moves += 1
	return moves


def main():
	for row in CHESS_BOARD:
		print '\t'.join(map(str, row))
	source, destination = map(int, raw_input('Enter source + destination: ').split())
	before = datetime.utcnow()
	print solution(source, destination)
	print 'Took {}ms'.format((datetime.utcnow() - before).total_seconds() * 1000)


if __name__ == '__main__':
	main()
