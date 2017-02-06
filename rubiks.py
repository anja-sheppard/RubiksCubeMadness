import pprint
import copy
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
        temptopList = []
        tempfrontList = []
        tempbottomList = []
        tempbackList = []
        for i in range(3):
            temptop = Pieces(list(self.cube[2-i][0][0].sides.keys()))
            temptop.sides = copyDict(self.cube[2-i][0][0].sides)
            temptopList.append(temptop)

            tempfront = Pieces(list(self.cube[0][i][0].sides.keys()))
            tempfront.sides = copyDict(self.cube[0][i][0].sides)
            tempfrontList.append(tempfront)

            tempbottom = Pieces(list(self.cube[i][2][0].sides.keys()))
            tempbottom.sides = copyDict(self.cube[i][2][0].sides)
            tempbottomList.append(tempbottom)

            tempback = Pieces(list(self.cube[2][2-i][0].sides.keys()))
            tempback.sides = copyDict(self.cube[2][2-i][0].sides)
            tempbackList.append(tempback)
        for i in range(3):
            self.cube[0][i][0].sides["top"] = temptopList[i].sides["back"]
            self.cube[0][i][0].sides["front"] = temptopList[i].sides["top"]
            self.cube[0][i][0].sides["left"] = temptopList[i].sides["left"]

            self.cube[i][2][0].sides["bottom"] = tempfrontList[i].sides["front"]
            self.cube[i][2][0].sides["back"] = tempfrontList[i].sides["bottom"]
            self.cube[i][2][0].sides["left"] = tempfrontList[i].sides["left"]

            self.cube[2][2-i][0].sides["back"] = tempbottomList[i].sides["bottom"]
            self.cube[2][2-i][0].sides["bottom"] = tempbottomList[i].sides["front"]
            self.cube[2][2-i][0].sides["left"] = tempbottomList[i].sides["left"]

            self.cube[2-i][0][0].sides["top"] = tempbackList[i].sides["back"]
            self.cube[2-i][0][0].sides["back"] = tempbackList[i].sides["bottom"]
            self.cube[2-i][0][0].sides["left"] = tempbackList[i].sides["left"]

        self.printy()
        

    def R(self):
        temptopList = []
        tempfrontList = []
        tempbottomList = []
        tempbackList = []
        for i in range(3):
            temptop = Pieces(list(self.cube[2-i][0][2].sides.keys()))
            temptop.sides = copyDict(self.cube[2-i][0][2].sides)
            temptopList.append(temptop)

            tempfront = Pieces(list(self.cube[0][i][2].sides.keys()))
            tempfront.sides = copyDict(self.cube[0][i][2].sides)
            tempfrontList.append(tempfront)

            tempbottom = Pieces(list(self.cube[i][2][2].sides.keys()))
            tempbottom.sides = copyDict(self.cube[i][2][2].sides)
            tempbottomList.append(tempbottom)

            tempback = Pieces(list(self.cube[2][2-i][2].sides.keys()))
            tempback.sides = copyDict(self.cube[2][2-i][2].sides)
            tempbackList.append(tempback)
        for i in range(3):
            self.cube[0][i][2].sides["top"] = tempbottomList[i].sides["front"]
            self.cube[0][i][2].sides["front"] = tempbottomList[i].sides["bottom"]
            self.cube[0][i][2].sides["right"] = tempbottomList[i].sides["right"]

            self.cube[i][2][2].sides["bottom"] = tempbackList[i].sides["back"]
            self.cube[i][2][2].sides["back"] = tempbackList[i].sides["top"]
            self.cube[i][2][2].sides["right"] = tempbackList[i].sides["right"]

            self.cube[2][2-i][2].sides["back"] = temptopList[i].sides["top"]
            self.cube[2][2-i][2].sides["bottom"] = temptopList[i].sides["back"]
            self.cube[2][2-i][2].sides["right"] = temptopList[i].sides["right"]

            self.cube[2-i][0][2].sides["top"] = tempfrontList[i].sides["front"]
            self.cube[2-i][0][2].sides["back"] = tempfrontList[i].sides["top"]
            self.cube[2-i][0][2].sides["right"] = tempfrontList[i].sides["right"]

        self.printy()

    def U(self):
        tempfrontList = []
        templeftList = []
        temprightList = []
        tempbackList = []
        for i in range(3):
            tempfront = Pieces(list(self.cube[0][0][i].sides.keys()))
            tempfront.sides = copyDict(self.cube[0][0][i].sides)
            tempfrontList.append(tempfront)
            
            templeft = Pieces(list(self.cube[2-i][0][0].sides.keys()))
            templeft.sides = copyDict(self.cube[2-i][0][0].sides)
            templeftList.append(templeft)
            
            tempright = Pieces(list(self.cube[2-i][0][2].sides.keys()))
            tempright.sides = copyDict(self.cube[2-i][0][2].sides)
            temprightList.append(tempright)
            
            tempback = Pieces(list(self.cube[2][0][i].sides.keys()))
            tempback.sides = copyDict(self.cube[2][0][i].sides)
            tempbackList.append(tempback)
        for i in range(3):
            print(tempfrontList[i].sides)
            self.cube[0][0][i].sides["front"] = temprightList[i].sides["right"]
            self.cube[0][0][i].sides["top"] = temprightList[i].sides["top"]

            self.cube[2-i][0][0].sides["left"] = tempfrontList[i].sides["front"]
            self.cube[2-i][0][0].sides["top"] = tempfrontList[i].sides["top"]

            self.cube[2][0][i].sides["back"] = templeftList[i].sides["left"]
            self.cube[2][0][i].sides["top"] = templeftList[i].sides["top"]

            self.cube[2-i][0][2].sides["right"] = tempbackList[i].sides["back"]
            self.cube[2-i][0][2].sides["top"] = tempbackList[i].sides["top"]

        self.printy()

    def D(self):
        tempfrontList = []
        templeftList = []
        temprightList = []
        tempbackList = []
        for i in range(3):
            tempfront = Pieces(list(self.cube[0][2][i].sides.keys()))
            tempfront.sides = copyDict(self.cube[0][2][i].sides)
            tempfrontList.append(tempfront)
            
            templeft = Pieces(list(self.cube[2-i][2][0].sides.keys()))
            templeft.sides = copyDict(self.cube[2-i][2][0].sides)
            templeftList.append(templeft)
            
            tempright = Pieces(list(self.cube[i][2][2].sides.keys()))
            tempright.sides = copyDict(self.cube[i][2][2].sides)
            temprightList.append(tempright)
            
            tempback = Pieces(list(self.cube[2][2][i].sides.keys()))
            tempback.sides = copyDict(self.cube[2][2][i].sides)
            tempbackList.append(tempback)
        for i in range(3):
            print(templeftList[i].sides)
            self.cube[0][2][i].sides["front"] = temprightList[i].sides["right"]
            self.cube[0][2][i].sides["bottom"] = temprightList[i].sides["bottom"]

            self.cube[2-i][2][0].sides["left"] = tempfrontList[i].sides["front"]
            self.cube[2-i][2][0].sides["bottom"] = tempfrontList[i].sides["bottom"]

            self.cube[2][0][2-i].sides["back"] = templeftList[i].sides["left"]
            self.cube[2][0][2-i].sides["bottom"] = templeftList[i].sides["bottom"]

            self.cube[2-i][0][2].sides["right"] = tempbackList[i].sides["back"]
            self.cube[2-i][0][2].sides["bottom"] = tempbackList[i].sides["bottom"]

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
    if i == "L" or i == "l":
        c.L()
    elif i == "R" or i == "r":
        c.R()
    elif i == "U" or i == "u":
        c.U()
    elif i == "D" or i == "d":
        c.D()

def copyDict(dict1):
    dict2 = {}
    for i in list(dict1.keys()):
        dict2[i] = dict1[i]
    return dict2


c = Cube()
c.generate()
c.printy()
c.cube[1][0][0].sides["left"]
solved = False
while solved == False:
    play(c)
    
