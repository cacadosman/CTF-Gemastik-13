from PIL import Image

def calcSize(size, offset):
	sizes = []
	for x,y in zip(size, offset):
		sizes.append((x[0]+y[0],x[1]+y[1]))
	return max(sizes)

x = open('offset').read().split('\n')[:-1]
y = open('dimension').read().split('\n')[:-1]
offs = map(lambda _ : map(int, _.split()), x)
size = map(lambda _ : map(int, _.split('x')), y)

dimension = calcSize(size, offs)
image 	  = Image.new('RGB',dimension)

for num, offset in enumerate(offs):
	name = 'x'.join(map(str, size[0]))
	if num != 0:		
		path = 'files/{}({})'.format(name, num)
	else:
		path = 'files/{}'.format(name)
	
	img = Image.open(path)
	image.paste(img, offset)

image.save('flag.jpg')