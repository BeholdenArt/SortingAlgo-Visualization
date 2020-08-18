import pygame 
import math
import random 
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 0, 0


width = int(input("Enter width(Must be a multiple of 10) : "))
height = int(input("Enter height(Must be a multiple of 10) : "))
if ((width > 80 or height > 80) and (width%10 == 0 and height%10 == 0)): 
	WINDOW_WIDTH = width
	WINDOW_HEIGHT = height
else:
	WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

arr = []
R, G, B = [], [], []

def setup(): 
	global WINDOW_WIDTH, WINDOW_HEIGHT, arr, R, G, B, solved
	for i in range(WINDOW_WIDTH):
		R.append(random.randint(10, 255))
		G.append(random.randint(10, 255))
		B.append(random.randint(10, 255))
		arr.append(random.randint(10, WINDOW_HEIGHT))


def reset():
	global arr, R, G, B
	arr = []
	R, G, B = [], [], []
	setup()

def SelectionSort():
	i = 0
	while (i < len(arr)): 
		for j in range(i+1, len(arr)): 
			if (arr[i] < arr[j]):
				arr[i], arr[j] = arr[j], arr[i]
				break
		i+=1


def DrawWindow():
	global arr, WINDOW_HEIGHT, R, G, B
	width = 10

	for i in range(0, len(arr), 10): 
		pygame.draw.rect(window, (R[i], G[i], B[i]), (i, WINDOW_HEIGHT, width, -arr[i]))

	pygame.display.update()


def main():
	global WINDOW_WIDTH, WINDOW_HEIGHT, solved

	run = True
	clock = pygame.time.Clock()
	setup() 

	while run: 
		window.fill((0, 0, 0))
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break 

		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_SPACE]: 
			SelectionSort()
		if pressed[pygame.K_r]:
			reset()

		DrawWindow()

	pygame.quit() 


if __name__ == "__main__": 
	main() 