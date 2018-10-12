<<<<<<< HEAD
from heapq import heappop, heappushimport mathdef Find_Euclidean_Distance(start, finish):    x1, y1 = start;    x2, y2 = finish;    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5 # finds the Euclidean distance between the 2 pointsdef find_path (source_point, destination_point, mesh):    """    Searches for a path from source_point to destination_point through the mesh    Args:        source_point: starting point of the pathfinder        destination_point: the ultimate goal the pathfinder must reach        mesh: pathway constraints the path adheres to    Returns:        A path (list of points) from source_point to destination_point if exists        A list of boxes explored by the algorithm    """    path = []    boxes = {}    distances = {} #measured distance of best path to that box    detail_points = {} #the dict of boxes to points where the point is the last point in its best path    sourceBox = (0, 0, 0, 0)    destinationBox = (0, 0, 0, 0)    for box in mesh["boxes"]:        if(source_point[0] >= box[0]) and (source_point[0] <= box[1]) and (source_point[1] >= box[2]) and (source_point[1] <= box[3]):            sourceBox = box        if(destination_point[0] >= box[0]) and (destination_point[0] <= box[1]) and (destination_point[1] >= box[2]) and (destination_point[1] <= box[3]):            destinationBox = box    frontqueue = [(0, source_point, sourceBox)]    distances[sourceBox] = 0    boxes[sourceBox] = -1    detail_points[sourceBox] = source_point    while frontqueue:        current_estimation, current_point, current_box = heappop(frontqueue)        if current_box == destinationBox:            break        for adjbox in mesh['adj'][current_box]:            xpoints = range( max(current_box[0],adjbox[0]), min(current_box[1],adjbox[1]) + 1 )            ypoints = range( max(current_box[2],adjbox[2]), min(current_box[3],adjbox[3]) + 1 )            minx = -1            miny = -1            minEst = math.inf            for x in xpoints:                for y in ypoints:                    newEstimation = distances[current_box] + Find_Euclidean_Distance(current_point, (x, y)) + Find_Euclidean_Distance((x,y), destination_point)                    if(newEstimation < minEst):                        minEst = newEstimation                        minx = x                        miny = y            if minx != -1:                if (adjbox not in distances) or (minEst < distances[adjbox] + Find_Euclidean_Distance(detail_points[adjbox], destination_point)):                    boxes[adjbox] = current_box                    distances[adjbox] = distances[current_box] + Find_Euclidean_Distance(current_point, (minx, miny))                    detail_points[adjbox] = (minx, miny)                    heappush(frontqueue, (minEst, (minx, miny), adjbox))    boxIter = boxes[destinationBox]    path.insert(0, ([destination_point[0], destination_point[1]] , [detail_points[boxIter][0],detail_points[boxIter][1]]))    while boxIter != -1:        prev = boxes[boxIter]        if prev != -1:            path.insert(0, ([detail_points[boxIter][0],detail_points[boxIter][1]] , [detail_points[prev][0], detail_points[prev][1]]))        elif(prev == -1):            path.insert(0, ([source_point[0], source_point[1]] , [detail_points[boxIter][0],detail_points[boxIter][1]]))        boxIter = boxes[boxIter]    return path, boxes.keys()
=======
from heapq import heappop, heappushimport math#ARGS: start = pair(x,y) finish = pair(x,y)def Find_Euclidean_Distance(start, finish):    x1, y1 = start;    x2, y2 = finish;    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5 # finds the Euclidean distance between the 2 pointsdef find_path (source_point, destination_point, mesh):    """    Searches for a path from source_point to destination_point through the mesh    Args:        source_point: starting point of the pathfinder        destination_point: the ultimate goal the pathfinder must reach        mesh: pathway constraints the path adheres to    Returns:        A path (list of points) from source_point to destination_point if exists        A list of boxes explored by the algorithm    """    path = []    boxes = {} #dict of all visited boxes    distances = {}    totaldistances = {}    detail_points = {}    sourcebox = (0, 0, 0, 0)    destinationbox = (0, 0, 0, 0)    for box in mesh["boxes"]:        if(source_point[0] >= box[0]) and (source_point[0] <= box[1]) and (source_point[1] >= box[2]) and (source_point[1] <= box[3]):            sourcebox = box        if(destination_point[0] >= box[0]) and (destination_point[0] <= box[1]) and (destination_point[1] >= box[2]) and (destination_point[1] <= box[3]):            destinationbox = box    frontqueue = [(0, source_point, sourcebox)]    distances[sourcebox] = 0    totaldistances[sourcebox] = 0    boxes[sourcebox] = -1    detail_points[sourcebox] = source_point    while frontqueue:        current_dist, current_point, current_box = heappop(frontqueue)        if current_box == destinationbox:            break        for adjbox in mesh['adj'][current_box]:            xpoints = range( max(current_box[0],adjbox[0]), min(current_box[1],adjbox[1]) + 1 )            ypoints = range( max(current_box[2],adjbox[2]), min(current_box[3],adjbox[3]) + 1 )            minx = -1            miny = -1            minDist = math.inf            for x in xpoints:                for y in ypoints:                    # total to prev + prev to current point + current point to end                    #going to need to update this line to pull minx,miny. i think distances is wrong - dustin                    #newDistance = current_dist + Find_Euclidean_Distance(current_point, (x,y)) + Find_Euclidean_Distance( (x, y), destination_point)                    newDistance = distances[current_box] + Find_Euclidean_Distance(detail_points[current_box], (x,y)) + Find_Euclidean_Distance( (x, y), destination_point)                    if newDistance < minDist:                        minDist = newDistance                        minx = x                        miny = y            #if new path or new shortest path found, update it            # maybe a problem with distances[adjbox]            if minx != -1 and (adjbox not in distances or minDist < distances[adjbox] + Find_Euclidean_Distance( (minx, miny), destination_point)):                print("xpoints: ", xpoints, "\nypoints: ", ypoints, "\nminx, miny: ", minx, ", ", miny)                detail_points[adjbox] = (minx, miny)                distances[adjbox] = minDist - Find_Euclidean_Distance( (minx, miny), destination_point)                totaldistances[adjbox] = minDist                boxes[adjbox] = current_box                heappush(frontqueue, ( minDist, (minx,miny), adjbox))    box = boxes[destinationbox]    boxpath = []    path.insert(0, ([destination_point[0], destination_point[1]] , [detail_points[box][0],detail_points[box][1]]))    while box != -1:        prev = boxes[box]        print(detail_points[box])        if(prev != -1):            path.insert(0, ([detail_points[box][0],detail_points[box][1]] , [detail_points[prev][0], detail_points[prev][1]]))        elif(prev == -1):            path.insert(0, ([source_point[0], source_point[1]] , [detail_points[box][0],detail_points[box][1]]))        box = boxes[box]            return path, boxes.keys()
>>>>>>> 2a0402f1339f440a8e3c225cb04a8e9dca23de18
