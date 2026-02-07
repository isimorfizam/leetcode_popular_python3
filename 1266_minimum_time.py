class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x_axis = [0]
        y_axis = [0]
        time = 0
        for i in range(1, len(points)) :
            point = points[i]
            previous_point = points[i-1]

            time += max(abs(point[0] - previous_point[0]), abs(point[1] - previous_point[1]))
        return time
        

'''
Important : Between 2 points, the steps(aka seconds taken) will be equal to maximum of difference between x and y coordinate.
'''