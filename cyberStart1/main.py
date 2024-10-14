tuple1 = ("x1","y2")
tuple2 = ("x2","y2")

#print(tuple1[0]-tuple2[0])

points = [tuple1,tuple2]

print(type(points))

def euclideanDistance(tuple1,tuple2):
    distance = (tuple2[0]-tuple1[0])+(tuple2[1]-tuple1[1])
    print("test")
    return print(distance)

for i in len(points):
    euclideanDistance(points[i],points[i+1])

euclideanDistance((1,2),(3,4))