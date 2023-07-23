from PIL import Image
from prio_helpers import is_edge, get_priority, change_prio
import argparse


parser = argparse.ArgumentParser(description="Script to add priority to edge of the dutch PlaceNL canvas",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("image_path", help="Path to image")
parser.add_argument("prio_path", help="Path to priority image")
parser.add_argument("-o", "--output", help="Path too store output image, if None is given, the image is shown")
parser.add_argument("-l", "--lowerprio", help="Lower priority in none edge pixels using a checkboard pattern (half will be lowered)", action="store_true")

args = parser.parse_args()

image = Image.open(args.image_path, mode="r")
prio = Image.open(args.prio_path, mode="r")

image_width, image_height = image.size
prio_width, prio_height = prio.size

if image_width != prio_width or image_height != prio_height:
    raise Exception("Image and Prio image are not the same size")

enhanced_prio = Image.new(mode="RGBA", size=(image_width, image_height))

for x in range(image_width):
    for y in range(image_height):
        red, green, blue, alpha = prio.getpixel((x, y))
        
        if(is_edge(image, x, y)): 
            # We detected the edge, we should enhance it's priority
            
            change_prio(prio, enhanced_prio, x, y, 10_000)

        else:
            if not args.lowerprio:
                enhanced_prio.putpixel((x, y), prio.getpixel((x, y)))
            else: 
                lower_prio = False
                if x % 2 == 0:
                    if y % 2 == 0:
                        lower_prio = True
                else: 
                    if y % 2 == 1:
                        lower_prio = True
                
                if lower_prio:
                    change_prio(prio, enhanced_prio, x, y, -10_000)
                else:
                    enhanced_prio.putpixel((x, y), prio.getpixel((x, y)))

                
if args.output == None:
    enhanced_prio.show()
else: 
    enhanced_prio.save(args.output)






