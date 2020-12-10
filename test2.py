import pygame

class Node():
    def __init__(self,parent=None,position=None):
        self.parent=parent
        self.position=position

        self.g=0
        self.h=0
        self.f=0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze,start,end,display=None):

    start_node=Node(None,start)
    start_node.g=start_node.h=start_node.f=0
    end_node=Node(None,end)
    end_node.g=end_node.h=end_node.f=0

    open_list=[]
    close_list=[]

    open_list.append(start_node)

    counter=0
    while len(open_list)>0:
        #Selecting the current Node
        current_node=open_list[0]
        current_index=0
        for index,item in enumerate(open_list):
            if(item.f < current_node.f):
                current_node=item
                current_index=index
        open_list.pop(current_index)
        close_list.append(current_node)

        #Check if its the goal node
        if(current_node==end_node):
            path=[]
            current=current_node
            while current is not None:
                path.append(current.position)
                current=current.parent
            return path[::-1]

        #coding the bots movement
        children=[]
        for new_pos in [(0,1),(0,-1),(1,0),(-1,0)]:
            node_pos=(current_node.position[0]+new_pos[0],current_node.position[1]+new_pos[1])
            #check if the new node position is within the game
            if(node_pos[0]<0 or node_pos[1]<0 or node_pos[0]>(len(maze)-1) or node_pos[1]>(len(maze[len(maze)-1])-1) ):
                continue
            #check if the new node is within the obstacles
            if maze[node_pos[0]][node_pos[1]]==1:
                continue
            #Create a new node
            new_node=Node(current_node,node_pos)
            children.append(new_node)

            #checks to add the new children items to either close or open list
            for child in children:
                #in case the child is already in the close list
                for item in close_list:
                    if(child==item):
                        continue

                child.g=current_node.g+1
                child.h=((child.position[0]-end_node.position[0])**2)+((child.position[1]-end_node.position[1])**2)
                #child.h=(abs(child.position[0]-end_node.position[0]))+(abs(child.position[1]-end_node.position[1]))
                #child.h=0
                child.f=child.g+child.h

                #in case the item is in the open list
                for item in open_list:
                    if child==item and child.g>item.g:
                        continue

                #finally append it to the open list
                open_list.append(child)
        for item in open_list:
            print("open_list>>",item.position)
        for item in close_list:
            print("close_list",item.position)
        print("This is loop number number>>",counter)
        counter=counter+1
        #for pygame
        for item in open_list:
            maze[item.position[0]][item.position[1]]=4#pink color searching area
        for row in range(10):
            for col in range(10):
                color=white
                if(maze[row][col]==4):
                    color=pink
                if(maze[row][col]==1):
                    color=red
                pygame.draw.rect(display,color,((margin+width)*col+margin,(margin+height)*row+margin,width,height))
        clock.tick(20)
        pygame.display.flip()
        



pygame.init()
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)#obstacles-->1
green=(0,255,0)#final path color-->5
blue=(0,0,255)#starting point-->2
orange=(255,165,0)#ending point-->3
pink=(255,182,193)#searching color-->4

display=pygame.display.set_mode((400,400))
clock=pygame.time.Clock()

maze=[]
for row in range(10):
    maze.append([])
    for col in range(10):
        maze[row].append(0)

start=None
end=None
decider=''

height=35
width=35
margin=5

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

        if event.type==pygame.MOUSEBUTTONDOWN and decider=='':
            pos=pygame.mouse.get_pos()
            col=pos[0]//(width+margin)
            row=pos[1]//(height+margin)
            start=(row,col)#sets the starting point
            maze[row][col]=2#2 stand for green and starting point
            print("start",start,maze)

        if event.type==pygame.MOUSEBUTTONUP and decider=='':
            pos=pygame.mouse.get_pos()
            col=pos[0]//(width+margin)
            row=pos[1]//(height+margin)
            end=(row,col)#sets the ending point
            maze[row][col]=3#3 stand for orange and ending point
            print("end",end,maze)

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                decider='OBS'
                print(decider)

        if event.type == pygame.MOUSEBUTTONDOWN and decider=='OBS':
            pos=pygame.mouse.get_pos()
            col=pos[0]//(width+margin)
            row=pos[1]//(height+margin)
            maze[row][col]=1#1stand for red and obstacles
            print("obs",maze)

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                decider='START'
                path=astar(maze,start,end,display)
                if len(path)!=0:
                    for items in path:
                        maze[items[0]][items[1]]=5
                print(path)
        

        display.fill(black)
        for row in range(10):
            for col in range(10):
                color=white
                if(maze[row][col]==1):
                    color=red
                if(maze[row][col]==2):
                    color=blue
                if(maze[row][col]==3):
                    color=orange
                if(maze[row][col]==4):
                    color=pink
                if(maze[row][col]==5):
                    color=green
                pygame.draw.rect(display,color,((margin+width)*col+margin,(margin+height)*row+margin,width,height))
        clock.tick(60)
        pygame.display.flip()