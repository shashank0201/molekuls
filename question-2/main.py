import typing


def main(tomato_grid: typing.List[typing.List[int]]):
    # START WRITING CODE HERE
    import collections
    N = len(tomato_grid)
    M = len(tomato_grid[0])
    Q = collections.deque()
    totalGood = 0
    #Find all good and append all rotten to queue
    for i in range(N):
        for j in range(M):
            if tomato_grid[i][j] == 1:
                totalGood += 1
            if tomato_grid[i][j] == 2:
                Q.appendleft((i,j,0))
    
    maxLevel = 0
    while Q:
        r, c, level = Q.pop()
        #Check all neighboors
        for x, y in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            if (0 <= x < N) and (0 <= y < M) and tomato_grid[x][y] == 1:
                tomato_grid[x][y] = 2 #Set to 2 - mark rotten or visited
                totalGood -= 1
                Q.appendleft((x,y, level+1))
                if level+1 > maxLevel:
                    maxLevel = level+1   
    if totalGood > 0:
        return -1
    return maxLevel


if __name__ == "__main__":
    tomato_grid = [
        [-1, 1, 0, -1, 1],
        [1, 0, 1, -1, 1],
        [1, 0, 0, -1, 1],
    ]
    r1 = main(tomato_grid)
    if r1 >1:
        print("Tomatoes will be rotten")
    if r1<0:
        print("All tomatoes cannot be rotten")

