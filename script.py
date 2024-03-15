from PIL import Image, ImageDraw
import math

file1 = open('data.txt', 'r')
lines = file1.readlines()
file1.close()

data = []
for line in lines:
    part = line.split("->")
    ang_dis = part[1].split(":/:")
    angle = float(ang_dis[0].strip())
    distance = float(ang_dis[1].strip())
    data.append((angle, distance))

empty_image = "empty.png"
image = Image.open(empty_image)
draw = ImageDraw.Draw(image)


def polarToCartesian(angle, distance):
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    return x, y

for angle, distance in data:
    x, y = polarToCartesian(angle, distance)
    scale_factor = 500
    draw.point((x + 500, y + 500), fill="red")  

output_image = "lidar_map.png"
image.save(output_image)

