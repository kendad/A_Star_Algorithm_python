import pygame

pygame.init()
black=(0,0,0)
white=(255,255,255)

display=pygame.display.set_mode((400,400))
clock=pygame.time.Clock()

maze=[]
for row in range(10):
    maze.append([])
    for col in range(10):
        maze[row].append(0)
print(maze)

height=35
width=35
margin=5

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            col=pos[0]//(width+margin)
            row=pos[1]//(height+margin)
            print(row,col)
            print("Position Of Mouse>>",pos)

        display.fill(black)
        for row in range(10):
            for col in range(10):
                pygame.draw.rect(display,white,((margin+width)*col+margin,(margin+height)*row+margin,width,height))
        clock.tick(60)
        pygame.display.flip()

