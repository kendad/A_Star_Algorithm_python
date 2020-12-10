import A_logic_mod

def main():
    maze = [[0,0,1,0],
           [0,0,1,0],
           [0,0,1,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,1,0]]
    start=(0,0)
    end=(1,3)
    path=A_logic_mod.astar(maze,start,end)
    print(path)

if __name__ == "__main__":
    main()