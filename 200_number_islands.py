class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # breadth first search - iterative approach
        def bfs(r, c) :
            search_queue = deque()
            visit.add((r,c))  # we keep track of what we already processed
            search_queue.append((r,c)) #we append what next to search

            while search_queue :
                row, column = search_queue.popleft() # process first item in the que
                directions = [[1,0],[-1,0], [0,1], [0,-1]] # set horizontal and vertical neighbours
                # loop over all neighbours of interest
                for dr, dc in directions :
                    r = row + dr
                    c = column + dc

                    # this will keep the while loop alive as long as there are '1's in area of interest -> when there are no longer '1's it ends and goes back to main function with changed r,c as the last processed queue element
                    if r in range(rows) and c in range(columns) and grid[r][c]=='1' and (r,c) not in visit :
                        search_queue.append((r,c))
                        visit.add((r,c))
                    
    

        count = 0 
        rows = len(grid)
        columns = len(grid[0])
        visit = set() #set of all fields visited

        # check every position and do bfs over it's vertical and horizontal neighbours
        for row in range(rows) :
            for column in range(columns):
                if grid[row][column]=='1' and (row,column) not in visit :
                    bfs(row,column) # this will change visit list, thus skipping r,c that are already in visited
                    # if all are connected, row and column will be equal to the dimensions of the matrix
                    count += 1

        return count

# TIME COMPLEXITY - 4*m*n -> O(m*n) 