from turtle import *

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

alphabet = {
	't': [[(0, 100), (80,100)], [(40, 0), (40,100)]]	
}

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
	return sum(list(xss), [])

def translate_letter(letter, delta):
	def translator(tup):
		(x, y) = tup
		(dx, dy) = delta
		return (x + dx, y+dy)

	return map_letter(translator, letter)

def main():
	draw_string("teodor")
	draw_letter(safe_lookup_char('t'))

	done()
	
if __name__ == '__main__':
	main()
