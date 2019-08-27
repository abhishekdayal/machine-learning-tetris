import pygame

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 250
TIME_DELAY = 750
CUBE_LEN = 25
X = 150 - CUBE_LEN / 2
Y = 0

INIT_ROW = 0
INIT_COL = 4


CURR_BOARD = [[0 for x in range(10)] for x in range(20)]
print(CURR_BOARD)

CURR_BOARD[INIT_ROW][INIT_COL] = 1

X_MIN, X_MAX = 0, WINDOW_WIDTH - CUBE_LEN
Y_MIN, Y_MAX = 0, WINDOW_HEIGHT - CUBE_LEN
VEL = CUBE_LEN

if __name__ == '__main__':
	run = True
	window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	while run:
		pygame.time.delay(TIME_DELAY)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		window.fill((0, 0, 0))
		for i in range(len(CURR_BOARD)):
			row = CURR_BOARD[i]
			for j in range(len(row)):
				if CURR_BOARD[i][j] == 1:
					pygame.draw.rect(window, (233, 0, 0), (j*CUBE_LEN, i*CUBE_LEN, CUBE_LEN, CUBE_LEN))
					
		# pygame.draw.rect(window, (234, 0, 0), (X, Y, CUBE_LEN, CUBE_LEN))
		pygame.display.update()



		# Y = min(Y + VEL, Y_MAX)


# move_list = [left, rotate, down]
#
#
# def usr_plays():
# 	move_list = []
# 	do_moves(moves)
#
#
#
# def ai_plays():
# 	do_moves(recommended_moves(...))
