import pprint
import copy
import random

class Cube(object):
    colors = {"top": "  R  ", "back": "  G  ", "front": "  B  ", "right": "  W  ", "bottom": "  P  ", "left": "  Y  "}
    def __init__(self):
        self.cube = [[[[] for k in range(3)] for j in range(3)] for i in range(3)]
    def printy(self):

        colorCodes = {"  G  ": "\x1b[6;37;42m", "  R  ":"\x1b[6;37;41m", "  Y  ":"\x1b[0;37;43m", "  B  ": "\x1b[6;37;44m", "  P  ": "\x1b[6;37;45m", "  W  ": "\x1b[6;30;47m"}

        #top
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(colorCodes[self.cube[2][0][i].sides["top"]] + self.cube[2][0][i].sides["top"] + "\x1b[0m", end = "\t")
        print("")
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(colorCodes[self.cube[1][0][i].sides["top"]] + self.cube[1][0][i].sides["top"] + "\x1b[0m", end = "\t")
        print("")
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(colorCodes[self.cube[0][0][i].sides["top"]] + self.cube[0][0][i].sides["top"] + "\x1b[0m", end = "\t")
        print("\n")

        #left
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[2-k][0][0].sides["left"]] + self.cube[2-k][0][0].sides["left"] + "\x1b[0m", end = "\t")
        print(" ", end = "")
        #front
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[0][0][k].sides["front"]] + self.cube[0][0][k].sides["front"] + "\x1b[0m", end = "\t")
        print(" ", end = "")
        #right
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[k][0][2].sides["right"]] + self.cube[k][0][2].sides["right"] + "\x1b[0m", end = "\t")
        print(" ", end = "")
        #back
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[2][0][2-k].sides["back"]] + self.cube[2][0][2-k].sides["back"] + "\x1b[0m", end = "\t")
        print("")
        #left
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[2-k][1][0].sides["left"]] + self.cube[2-k][1][0].sides["left"] + "\x1b[0m", end = "\t")
        print(" ", end = "")
        #front
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[0][1][k].sides["front"]] + self.cube[0][1][k].sides["front"] + "\x1b[0m", end = "\t")
        print(" ", end = "")
        #right
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[k][1][2].sides["right"]] + self.cube[k][1][2].sides["right"] + "\x1b[0m", end = "\t")
        print(" ", end = "")
        #back
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[2][1][2-k].sides["back"]] + self.cube[2][1][2-k].sides["back"] + "\x1b[0m", end = "\t")
        print("")
        #left
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[2-k][2][0].sides["left"]] + self.cube[2-k][2][0].sides["left"] + "\x1b[0m", end = "\t")
        print(" ", end = "")
        #front
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[0][2][k].sides["front"]] + self.cube[0][2][k].sides["front"] + "\x1b[0m", end = "\t")
        print(" ", end = "")
        #right
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[k][2][2].sides["right"]] + self.cube[k][2][2].sides["right"] + "\x1b[0m", end = "\t")
        print(" ", end = "")
        #back
        for k in range(len(self.cube[0])):
            print(colorCodes[self.cube[2][2][2-k].sides["back"]] + self.cube[2][2][2-k].sides["back"] + "\x1b[0m", end = "\t")
        print("\n")


        #bottom
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(colorCodes[self.cube[0][2][i].sides["bottom"]] + self.cube[0][2][i].sides["bottom"] + "\x1b[0m", end = "\t")
        print("")
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(colorCodes[self.cube[0][2][i].sides["bottom"]] + self.cube[0][2][i].sides["bottom"] + "\x1b[0m", end = "\t")
        print("")
        print("\t\t", end = "\t ")
        for i in range(len(self.cube[0])):
            print(colorCodes[self.cube[2][2][i].sides["bottom"]] + self.cube[2][2][i].sides["bottom"] + "\x1b[0m", end = "\t")
        print("")

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

    def isSolved(self, s):
        for i in range(len(self.cube)):
            for j in range(len(self.cube[0])):
                for k in range(len(self.cube[0][0])):
                    if(self.cube[i][j][k].sides["top"] != s.cube[i][j][k].sides["top"]): return False
                    elif(self.cube[i][j][k].sides["bottom"] != s.cube[i][j][k].sides["bottom"]): return False
                    elif(self.cube[i][j][k].sides["right"] != s.cube[i][j][k].sides["right"]): return False
                    elif(self.cube[i][j][k].sides["left"] != s.cube[i][j][k].sides["left"]): return False
                    elif(self.cube[i][j][k].sides["front"] != s.cube[i][j][k].sides["front"]): return False
                    elif(self.cube[i][j][k].sides["back"] != s.cube[i][j][k].sides["back"]): return False
        return True


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

        return self


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

        return self

    def U(self):
        tempfrontList = []
        templeftList = []
        temprightList = []
        tempbackList = []
        for i in range(3):
            tempfront = Pieces(list(self.cube[0][0][i].sides.keys()))
            tempfront.sides = copyDict(self.cube[0][0][i].sides)
            tempfrontList.append(tempfront)

            templeft = Pieces(list(self.cube[i][0][0].sides.keys()))
            templeft.sides = copyDict(self.cube[i][0][0].sides)
            templeftList.append(templeft)

            tempright = Pieces(list(self.cube[i][0][2].sides.keys()))
            tempright.sides = copyDict(self.cube[i][0][2].sides)
            temprightList.append(tempright)

            tempback = Pieces(list(self.cube[2][0][i].sides.keys()))
            tempback.sides = copyDict(self.cube[2][0][i].sides)
            tempbackList.append(tempback)
        for i in range(3):
            self.cube[0][0][i].sides["front"] = temprightList[i].sides["right"]
            self.cube[0][0][i].sides["top"] = temprightList[i].sides["top"]

            self.cube[2-i][0][0].sides["left"] = tempfrontList[i].sides["front"]
            self.cube[2-i][0][0].sides["top"] = tempfrontList[i].sides["top"]

            self.cube[2][0][i].sides["back"] = templeftList[i].sides["left"]
            self.cube[2][0][i].sides["top"] = templeftList[i].sides["top"]

            self.cube[2-i][0][2].sides["right"] = tempbackList[i].sides["back"]
            self.cube[2-i][0][2].sides["top"] = tempbackList[i].sides["top"]

        return self

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

            tempright = Pieces(list(self.cube[2-i][2][2].sides.keys()))
            tempright.sides = copyDict(self.cube[2-i][2][2].sides)
            temprightList.append(tempright)

            tempback = Pieces(list(self.cube[2][2][i].sides.keys()))
            tempback.sides = copyDict(self.cube[2][2][i].sides)
            tempbackList.append(tempback)
        for i in range(3):
            self.cube[0][2][i].sides["front"] = templeftList[i].sides["left"]
            self.cube[0][2][i].sides["bottom"] = templeftList[i].sides["bottom"]

            self.cube[i][2][0].sides["left"] = tempbackList[i].sides["back"]
            self.cube[i][2][0].sides["bottom"] = tempbackList[i].sides["bottom"]

            self.cube[2][2][i].sides["back"] = temprightList[i].sides["right"]
            self.cube[2][2][i].sides["bottom"] = temprightList[i].sides["bottom"]

            self.cube[i][2][2].sides["right"] = tempfrontList[i].sides["front"]
            self.cube[i][2][2].sides["bottom"] = tempfrontList[i].sides["bottom"]

        return self

    def F(self):
        tempbottomList = []
        templeftList = []
        temprightList = []
        temptopList = []
        for i in range(3):
            temptop = Pieces(list(self.cube[0][0][i].sides.keys()))
            temptop.sides = copyDict(self.cube[0][0][i].sides)
            temptopList.append(temptop)

            templeft = Pieces(list(self.cube[0][2-i][0].sides.keys()))
            templeft.sides = copyDict(self.cube[0][2-i][0].sides)
            templeftList.append(templeft)

            tempright = Pieces(list(self.cube[0][i][2].sides.keys()))
            tempright.sides = copyDict(self.cube[0][i][2].sides)
            temprightList.append(tempright)

            tempbottom = Pieces(list(self.cube[0][2][2-i].sides.keys()))
            tempbottom.sides = copyDict(self.cube[0][2][2-i].sides)
            tempbottomList.append(tempbottom)
        for i in range(3):
            self.cube[0][i][2].sides["right"] = temptopList[i].sides["top"]
            self.cube[0][i][2].sides["front"] = temptopList[i].sides["front"]

            self.cube[0][0][i].sides["top"] = templeftList[i].sides["left"]
            self.cube[0][0][i].sides["front"] = templeftList[i].sides["front"]

            self.cube[0][2-i][0].sides["left"] = tempbottomList[i].sides["bottom"]
            self.cube[0][2-i][0].sides["front"] = tempbottomList[i].sides["front"]

            self.cube[0][2][2-i].sides["bottom"] = temprightList[i].sides["right"]
            self.cube[0][2][2-i].sides["front"] = temprightList[i].sides["front"]

        return self

    def B(self):
        tempbottomList = []
        templeftList = []
        temprightList = []
        temptopList = []
        for i in range(3):
            temptop = Pieces(list(self.cube[2][0][i].sides.keys()))
            temptop.sides = copyDict(self.cube[2][0][i].sides)
            temptopList.append(temptop)

            templeft = Pieces(list(self.cube[2][2-i][0].sides.keys()))
            templeft.sides = copyDict(self.cube[2][2-i][0].sides)
            templeftList.append(templeft)

            tempright = Pieces(list(self.cube[2][i][2].sides.keys()))
            tempright.sides = copyDict(self.cube[2][i][2].sides)
            temprightList.append(tempright)

            tempbottom = Pieces(list(self.cube[2][2][i].sides.keys()))
            tempbottom.sides = copyDict(self.cube[2][2][i].sides)
            tempbottomList.append(tempbottom)
        for i in range(3):
            self.cube[2][2-i][2].sides["right"] = tempbottomList[i].sides["bottom"]
            self.cube[2][2-i][2].sides["back"] = tempbottomList[i].sides["back"]

            self.cube[2][0][i].sides["top"] = temprightList[i].sides["right"]
            self.cube[2][0][i].sides["back"] = temprightList[i].sides["back"]

            self.cube[2][2-i][0].sides["left"] = temptopList[i].sides["top"]
            self.cube[2][2-i][0].sides["back"] = temptopList[i].sides["back"]

            self.cube[2][2][2-i].sides["bottom"] = templeftList[i].sides["left"]
            self.cube[2][2][2-i].sides["back"] = templeftList[i].sides["back"]

        return self

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
        c = c.L()
    elif i == "L'" or i == "l'":
        for i in range(3):
            c = c.L()
    elif i == "R" or i == "r":
        c = c.R()
    elif i == "R'" or i == "r'":
        for i in range(3):
            c = c.R()
    elif i == "U" or i == "u":
        c = c.U()
    elif i == "U'" or i == "u'":
        for i in range(3):
            c = c.U()
    elif i == "D" or i == "d":
        c = c.D()
    elif i == "D'" or i == "d'":
        for i in range(3):
            c = c.D()
    elif i == "F" or i == "f":
        c = c.F()
    elif i == "F'" or i == "f'":
        for i in range(3):
            c = c.F()
    elif i == "B" or i == "b":
        c = c.B()
    elif i == "B'" or i == "b'":
        for i in range(3):
            c = c.B()
    elif i == "Q" or i == "q":
        return 1
    else:
        print("Please enter a valid command.")
    c.printy()
    return 0


def copyDict(dict1):
    dict2 = {}
    for i in list(dict1.keys()):
        dict2[i] = dict1[i]
    return dict2

def scramble(c):
    random.seed()
    moves = [c.R, c.B, c.F, c.U, c.D, c.L]
    for i in range(80):
        moves[random.randint(0, 5)]()


print("\n" + '\x1b[6;30;42m' + "WELCOME TO RUBIKS.CUBE ! ! !" + '\x1b[0m')
print("\n\nUse your keyboard to move the pieces (\'B\', \'U\', etc.)")
print("\nNOTE: For pretty colors, a Unix-based operating system is required.\n\n")
c = Cube()
s = Cube()
c.generate()
s.generate()
scramble(c)
c.printy()
solved = False
while solved == False:
    play(c)
    if c.isSolved(s):
        print("solved!!!!")
