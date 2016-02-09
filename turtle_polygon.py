from turtle import *
import math

def draw_poly(polygon):
	penup()
	for line in polygon:
		goto(line)
		pendown()
	penup()

def draw_string(s):
	raster = rasterize_string(s)
	draw_letter(raster)

def draw_letter(polygons):
	for poly in polygons:
		draw_poly(poly)

def map_letter(f, letter):
	return map(lambda poly: map(f, poly), letter)

def ellipse(rx, ry, start=0, end=360, x0=0, y0=0):
	for part in range(start, end+1, 10):
		theta = part/360 * 2*math.pi
		x = x0 + rx + rx*math.cos(theta)
		y = y0 + ry + ry*math.sin(theta)
		yield (x,y)

def safe_lookup_char(c):
	if c in alphabet:
		return alphabet[c]
	else:
		return []

def rasterize_string(s):
	x = 0
	y = 0
	dx = 100
	polygons = []

	for c in s:
		letter = translate_letter(safe_lookup_char(c), (x, y))
		x += 100
		for line in letter:
			yield line

def concat(xss):
	for xs in xss:
		for x in xs:
			yield x

def translate_letter(letter, delta):
	def translator(tup):
		(x, y) = tup
		(dx, dy) = delta
		return (x + dx, y+dy)

	return map_letter(translator, letter)

alphabet = {
	't': [[(0, 100), (80,100)], [(40, 0), (40,100)]]	
	, 'e': [[(0,0), (0,100), (80,100)], [(0, 50), (60, 50)], [(0,0), (80, 0)]]
	, 'o': [ellipse(40,50)]
	, 'd': [ellipse(50, 50, start=-90, end=90, x0=-30, y0=0), [(20, 0), (20, 100)]]
	# , 'r': concat([


	# 	])
}

def main():
	draw_string("teodor")

	done()
	
if __name__ == '__main__':
	main()
