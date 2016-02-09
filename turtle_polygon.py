from turtle import *
import math

def draw_poly(polygon):
	penup()
	for line in polygon:
		goto(line)
		pendown()
	penup()

def draw_letter(polygons):
	for poly in polygons:
		draw_poly(poly)

def map_letter(f, letter):
	return map(lambda poly: map(f, poly), letter)

def ellipse(rx, ry, start=0, end=360, x0=0, y0=0):
	ps = []
	for part in range(start, end+1, 10):
		theta = part/360 * 2*math.pi
		x = x0 + rx*math.cos(theta)
		y = y0 + ry*math.sin(theta)
		ps.append((x,y))
	return ps

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
	, 'o': [ellipse(40,50, x0=40, y0=50)]
	, 'd': [ellipse(50, 50, start=-90, end=90, x0=0, y0=50), [(0, 0), (0, 100)]]
	, 'r': [[(0,0), (0,100)], ellipse(40, 20, -90, 90, 0, 80), [(0, 60), (50, 0)]]
	, ' ': []
	, 'k': [[(0,0), (0,100)], [(80,100), (0, 50), (80,0)]]
	, 'u': [[(0,100), (0,50)], ellipse(40, 50, -180, 0, 40, 50), [(80,50), (80,100)]]
	, 'l': [[(0,100), (0,0), (80,0)]]
}

def main():
	def scale(tup):
		factor = .2
		x, y = tup
		return (factor*x, factor*y)
	raster = map_letter(scale, rasterize_string("teodor er kul"))

	draw_letter(raster)

	done()
	
if __name__ == '__main__':
	main()
