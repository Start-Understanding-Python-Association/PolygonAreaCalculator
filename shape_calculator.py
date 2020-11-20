class Rectangle:
    """Quadrilateral with length not equal to width and 4 right angles."""

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, width):
        self.width = width
        return

    def set_height(self, height):
        self.height = height
        return

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        count = 0
        picture = ''
        while count < self.height:
            picture = picture + '*' * self.width + '\n'
            count = count + 1
        return picture

    def get_amount_inside(self, shape):
        side_by_sides = int(self.width / shape.width)
        how_deep = int(self.height / shape.height)
        return side_by_sides * how_deep


class Square(Rectangle):
    """Quadrilateral with length equal to width and 4 right angles."""

    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        self.side = side

    def __str__(self):
        return 'Square(side=' + str(self.side) + ')'

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.side = width
        self.width = width
        self.height = width

    def set_height(self, height):
        self.side = height
        self.width = height
        self.height = height
