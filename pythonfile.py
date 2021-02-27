import pygame
import buttonfile
import random

# User inputs grid size
# Left click = open tile
# Right click = flag
# (potential, later) score implementation
# (if have time) pixel art/more complex look for mine/flag

rows = 10
cols = 15

nodeList = []
for i in range(cols):
	for j in range(rows):
		num = random.randint(0, 10)
		if num < 3:
			text = "*"
		else:
			text = ""
		newNode = buttonfile.Button((255, 255, 255), i*50 + 50, j*50 + 50, 50, 50, text)
		nodeList.append(newNode)

# index - cols | top
# index + cols | bottom
# index - 1 | left
# index + 1 | right
# index - cols - 1 | top left
# index - cols + 1 | top right
# index + cols - 1 | bottom left
# index + cols + 1 | bottom right


def numneighbors(list, index):
	num = 0
	topleft = True
	top = True
	topright = True
	left = True
	right = True
	botleft = True
	bot = True
	botright = True
	if index <= cols:
		topleft = False
		top = False
		topright = False
	if index >= len(nodeList) - cols:
		botleft = False
		bot = False
		botright = False
	if index % cols == 0:
		topleft = False
		left = False
		botleft = False
	if index % cols == cols - 1:
		topright = False
		right = False
		botright = False
	if topleft and nodeList[index - cols - 1].text == "*":
		num += 1
	if top and nodeList[index - cols].text == "*":
		num += 1
	if topright and nodeList[index - cols + 1].text == "*":
		num += 1
	if left and nodeList[index - 1].text == "*":
		num += 1
	if right and nodeList[index + 1].text == "*":
		num += 1
	if botleft and nodeList[index + cols - 1].text == "*":
		num += 1
	if bot and nodeList[index + cols].text == "*":
		num += 1
	if botright and nodeList[index + cols + 1].text == "*":
		num += 1
	return num

for i in range(rows*cols):
	if nodeList[i].text != "*":
		text = str(numneighbors(nodeList, i))
		if text == "0":
			text = ""
		nodeList[i].text = text

def main():
	pygame.init()
	mainwindow = pygame.display.set_mode((cols*50 + 100, rows*50 + 100))
	mainwindow.fill((255, 255, 255))

	running = True
	while running:
		mainwindow.fill((255, 255, 255))
		drawwindow(mainwindow)
		pygame.display.update()

		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()

			if event.type == pygame.QUIT:
				running = False
				pygame.quit()

			#if event.type == pygame.MOUSEMOTION:

def drawwindow(mainwindow):
	for i in nodeList:
		i.draw(mainwindow, (0, 0, 0))

main()
