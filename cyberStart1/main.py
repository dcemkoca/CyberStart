import math

points = [(0, 2), (0, 4), (0, 5), (0, 9), (0, 15)]
distances = []

def euclideanDistance(tuple1,tuple2):
    distance = math.sqrt(((tuple2[0]-tuple1[0]) ** 2)+((tuple2[1]-tuple1[1]) ** 2))
    return distance

for i in range(len(points)-1):
    x = euclideanDistance(points[i],points[i+1])
    distances.append(x)

print(distances)
maxDistance = distances[0]

for i in range(len(distances)):
    if distances[i] > maxDistance:
        maxDistance = distances[i]

print(maxDistance)


