


def traverse(triangle, currval = 0, maxval = 0, row = 0, element = 0):
    currval += triangle[row][element]
    if row + 1 == len(triangle):
        if currval > maxval:
            return currval
        else:
            return maxval
    else:
        maxval = traverse(triangle, currval, maxval, row + 1, element)
        maxval = traverse(triangle, currval, maxval, row + 1, element + 1)
    return maxval

def upwards(tri, lower):
    if len(lower) == 1: 
        return lower
    else:
        lower = [max(lower[i], lower[i+1]) + b for i,b in enumerate(tri[-1])]
        return upwards(tri[:-1], lower) 
    
def main():
    filename = "p067_triangle.txt"
#    filename = "test.txt"
    trifile = open(filename)
    triangle = []
    for l in trifile.readlines():
        triangle.append([int(i) for i in l.split()])

    print(upwards(triangle[:-1], triangle[-1]))

if __name__ == "__main__":
    main()
