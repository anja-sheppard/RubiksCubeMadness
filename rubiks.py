import pprint
class Cube(object):
    colors = {"top": "red", "back": "green", "front": "blue", "right": "white", "bottom": "orange", "left": "yellow"}
    def __init__(self):
        self.cube = [[[[] for k in range(3)] for j in range(3)] for i in range(3)]
    def printy(self):
        return pprint.pprint(self.cube)
    def generate(self):
        for i in range(3):
            for j in range(3):
                self.cube[0][i][j].append("front")
                self.cube[2][i][j].append("back")
            self.cube[0][0][i].append("top")
            self.cube[1][0][i].append("top")
            self.cube[2][0][i].append("top")
            self.cube[0][2][i].append("bottom")
            self.cube[1][2][i].append("bottom")
            self.cube[2][2][i].append("bottom")
            self.cube[0][i][0].append("left")
            self.cube[1][i][0].append("left")
            self.cube[2][i][0].append("left")
            self.cube[0][i][2].append("right")
            self.cube[1][i][2].append("right")
            self.cube[2][i][2].append("right")

class Pieces(object):
    def __init__(self, numSides):
        self.numSides = numSides
        keys = ["front", "left", "back", "right", "top", "bottom"]
        self.sides = {key: None for key in keys}
        self.sideList = []
    def assignColors(self, listy):
        for i in range(len(listy)):
            self.sides[listy[i]] = Cube.colors[listy[i]]

class Squares(object):
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return self.color
    def __repr(self):
        return "'" + str(self) + "'"
