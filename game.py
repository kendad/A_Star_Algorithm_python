import pygame

black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)

width=20
height=20

margin=5

grid=[]
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)


pygame.init()
window_size=[255,255]
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("A* Algorithm Visulization")
done=False
clock=pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            #col=pos[0]//(width+margin)
            #row=pos[1]//(height+margin)
            #grid[row][col]=1
            #print("clicked",pos,"Grid Coordinates",row,col)
            print("Mouse Position",pos)

    screen.fill(black)
    for row in range(10):
        for col in range(10):
            color=white
            if grid[row][col]==1:
                color=red
            pygame.draw.rect(screen,
                            color,
                            [(margin+width)*column+margin,
                            (margin+height)*row+margin,
                            width,height
                            ])#x,y,width,heiht
    clock.tick(60)
    pygame.display.flip()
pygame.quit()