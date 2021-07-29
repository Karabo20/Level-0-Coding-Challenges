# Task 0.5
def triangle(side1, side2, side3):
    semi_p = 0.5 * (side1 + side2 + side3)                                    
    area = (semi_p * (semi_p - side1)*(semi_p - side2)*(semi_p - side3)) ** 0.5
    return area
