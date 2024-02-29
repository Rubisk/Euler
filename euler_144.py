import sys
import math

def slope_of_ellipse(x, y):
	return -4 * x / y

def points_to_line(x1, y1, x2, y2):
	slope = (y2 - y1) / (x2 - x1)
	start = y1 - slope * x1
	return start, slope

def get_next(x1, y1, slope):
	start = y1 - slope * x1
	ellipse_slope = slope_of_ellipse(x1, y1)
	new_slope = -math.tan(2 * math.atan(1 / ellipse_slope) - math.atan(-slope))
	dx = -(8 * x + 2 * y1 * new_slope) / (new_slope ** 2 + 4)
	new_x = x1 + dx
	new_y = y1 + dx * new_slope
	return new_x, new_y, new_slope


if __name__ == "__main__":
	x, y = float(sys.argv[-2]), float(sys.argv[-1])

	bounces = 0
	_, slope = points_to_line(0.0, 10.1, x, y)
	
	while not (-0.01 < x < 0.01 and y > 0):
		x, y, slope = get_next(x, y, slope)
		bounces += 1
	print("laser reflected {} times".format(bounces))