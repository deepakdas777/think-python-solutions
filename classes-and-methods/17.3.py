# Write a str method for the Point class. Create a Point object and print it.



class Point(object):
    def __init__(self, x=10, y=20):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

point = Point()
print point
