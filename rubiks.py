import pprint
class Cube(object):
    colors = {"top": "red", "back": "green", "front": "blue", "right": "white", "bottom": "orange", "left": "yellow"}
    def __init__(self):
        self.cube = [[[[] for k in range(3)] for j in range(3)] for i in range(3)]
    def printy(self):

        #top
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(self.cube[2][0][i].sides["top"], end = "\t")
        print("")
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(self.cube[1][0][i].sides["top"], end = "\t")
        print("")
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(self.cube[0][0][i].sides["top"], end = "\t")
        print("\n")

        # left
        for k in range(len(self.cube[0])):
            print(self.cube[2][k][0].sides["left"], end = "\t")
        print(" ", end = "")
        #front
        for k in range(len(self.cube[0])):
            print(self.cube[0][0][k].sides["front"], end = "\t")
        print(" ", end = "")
        #right
        for k in range(len(self.cube[0])):
            print(self.cube[k][0][2].sides["right"], end = "\t")
        print(" ", end = "")
        #back
        for k in range(len(self.cube[0])):
            print(self.cube[2][0][2-k].sides["back"], end = "\t")
        print("")
        #left
        for k in range(len(self.cube[0])):
            print(self.cube[1][k][0].sides["left"], end = "\t")
        print(" ", end = "")
        #front
        for k in range(len(self.cube[0])):
            print(self.cube[0][1][k].sides["front"], end = "\t")
        print(" ", end = "")
        #right
        for k in range(len(self.cube[0])):
            print(self.cube[k][1][2].sides["right"], end = "\t")
        print(" ", end = "")
        #back
        for k in range(len(self.cube[0])):
            print(self.cube[2][1][2-k].sides["back"], end = "\t")
        print("")
        #left
        for k in range(len(self.cube[0])):
            print(self.cube[0][k][0].sides["left"], end = "\t")
        print(" ", end = "")
        #front
        for k in range(len(self.cube[0])):
            print(self.cube[0][2][k].sides["front"], end = "\t")
        print(" ", end = "")
        #right
        for k in range(len(self.cube[0])):
            print(self.cube[k][2][2].sides["right"], end = "\t")
        print(" ", end = "")
        #back
        for k in range(len(self.cube[0])):
            print(self.cube[2][2][2-k].sides["back"], end = "\t")
        print("\n")


        #bottom
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(self.cube[0][2][i].sides["bottom"], end = "\t")
        print("")
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(self.cube[1][2][i].sides["bottom"], end = "\t")
        print("")
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(self.cube[2][2][i].sides["bottom"], end = "\t")
        print("")


        #return pprint.pprint(self.cube)
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
        for i in range(len(self.cube)):
            for j in range(len(self.cube[0])):
                for k in range(len(self.cube[0][0])):
                    self.cube[i][j][k] = Pieces(self.cube[i][j][k])
    def L(self):
        
        self.printy()

class Pieces(object):
    def __init__(self, listy):
        keys = ["front", "left", "back", "right", "top", "bottom"]
        self.sides = {key: None for key in keys}
        for i in range(len(listy)):
            self.sides[listy[i]] = Cube.colors[listy[i]]
    #TODO: make str and repr hooks

class Squares(object):
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return self.color
    def __repr(self):
        return "'" + str(self) + "'"


def play(c):
    i = input("What's your play? ")
    if i == "L" or "l":
        c.L()


c = Cube()
c.generate()
c.printy
play(c)
