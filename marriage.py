
# CS3100 - Fall 2023 - Programming Assignment 1
#################################
# Collaboration Policy: You may discuss the problem and the overall
# strategy with up to 4 other students, but you MUST list those people
# in your submission under collaborators.  You may NOT share code,
# look at others' code, or help others debug their code.  Please read
# the syllabus carefully around coding.  Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: srp9jd
# Collaborators: wre6st, ezp9xp, uyp7dr
# Sources: Introduction to Algorithms, Cormen
#################################
from collections import deque

class Marriage:
    lukePath = []
    lorelaiPath = []
    combinedStart = ()
    combinedEnd = ()
    combinedRooms = {}
    combinedPath = []

    def __init__(self):
        return

    def getLukePath(self):
        for combinedRoom in self.combinedPath:
            self.lukePath.append(combinedRoom[0])
        return self.lukePath

    def getLorelaiPath(self):
        for combinedRoom in self.combinedPath:
            self.lorelaiPath.append(combinedRoom[1])
        return self.lorelaiPath

    # This is the method that should set off the computation
    # of marriage.  It takes as input a list lines of input
    # as strings.  You should parse that input and then compute
    # the shortest paths that both Luke and Lorelai should take.
    # The class fields of lukePath and lorelaiPath should be filled
    # with their respective paths.  The getters above will be called
    # by the grader script.
    #
    # @return the length of the shortest paths (in rooms)
    def compute(self, file_data):
        size = int(file_data[0])    # first line given is number of rooms
        lukeSE = file_data[1].split()
        lorelaiSE = file_data[2].split()
        startRoom = ((int)(lukeSE[0]),(int)(lorelaiSE[0]))
        endRoom = ((int)(lukeSE[1]),(int)(lorelaiSE[1]))
        graph = {}
        #create input graph
        for i in range(size):
            graph[i] = []
            lines = file_data[i+3].split()
            graph[i].append(i)
            for neighbors in lines:
                graph[i].append(int(neighbors))
        #create combined nodes
        # checks if second room is not the same nor adjacent to the first room, if not, create combined node
        for firstRoom in graph:
            for secondRoom in graph:
                if secondRoom not in graph[firstRoom]:
                    self.combinedRooms[(firstRoom, secondRoom)] = []
        #print(self.combinedRooms)
        #create combined graph
        for combinedRoom in self.combinedRooms:
            for neighborOne in graph[combinedRoom[0]]:
                for neighborTwo in graph[combinedRoom[1]]:
                    if(neighborOne, neighborTwo) in self.combinedRooms.keys():
                        self.combinedRooms[combinedRoom].append((neighborOne,neighborTwo))
        #print(self.combinedRooms)
        #BFS
        # queue starts at startRoom and initalizes queue with startRoom
        toVisit = deque([(startRoom, [startRoom])])
        seen = set()
        while toVisit:
            current, tempPath = toVisit.popleft()
            if current == endRoom:
                self.combinedPath = tempPath
                return len(tempPath)
            if current not in seen:
                seen.add(current)
            neighbors = self.combinedRooms.get(current, [])
            for neighbor in neighbors:
                if neighbor != current:
                    path = list(tempPath)
                    path.append(neighbor)
                    toVisit.append((neighbor, path))