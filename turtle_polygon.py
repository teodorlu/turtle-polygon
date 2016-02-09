from turtle import *

def draw_poly(polygon):
	if len(polygon) < 2:
		return()

	penup()
	goto(polygon[0])
	pendown()
	for i in range(1, len(polygon)):
		goto(polygon[i])
	penup()

def draw_letter(polygons):
	for poly in polygons:
		draw_poly(poly)

def map_letter(f, letter):
	return map(lambda poly: map(f, poly), letter)

alphabet = {
	't': [[(0, 100), (80,100)], [(40, 0), (40,100)]]	
}

def concat(xss):
	return sum(xss, [])

def translate_letter(letter, delta):
	def translator(tup):
		(x, y) = tup
		(dx, dy) = delta
		return (x + dx, y+dy)

	return map_letter(translator, letter)

def main():

	t2 = map_letter(lambda tup: (tup[0]+200, tup[1]), t)
	draw_letter(t)
	draw_letter(t2)

	done()
	
if __name__ == '__main__':
	main()
