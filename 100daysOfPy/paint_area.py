import math

test_h = int(input("Height "))
test_w = int(input("Width "))
coverage = 5


def paint_calc(height, width, cover):
    print(f"You'll need {math.ceil((height * width) / cover)} cans of paint")


paint_calc(height = test_h, width = test_w, cover = coverage)