from pygame import Color

DEBUG = False

def input2Color(c):
    if (type(c) == int) and (0 <= c) and (255 >= c):
        return Color(c, c, c)
    elif (type(c) == str):
        return Color(c)

def ASSERT(statement):
    if DEBUG:
        assert statement

def PRINT(statement, **kwargs):
    if DEBUG:
        print(statement, end=kwargs.get("end", "\n"))