from PIL import Image

priority_max = 0xFFFFFF

def is_edge(check_image, x, y):
    
    current_color = check_image.getpixel((x, y))

    # If a pixel contains no data, we don't mark it as important
    if current_color == (0, 0, 0, 0): 
        return False

    # If a pixel is on the edge of the image, it's considered a edge
    if x == 0 or y == 0 or x == check_image.width - 1 or y == check_image.height - 1:
        return True
    
    # Get all the neighbouring pixel
    right_neighbour_color = check_image.getpixel((x + 1, y))
    left_neighbour_color = check_image.getpixel((x - 1, y))
    top_neighbour_color = check_image.getpixel((x, y - 1))
    bottom_neighbour_color = check_image.getpixel((x, y + 1))

    # Check to see if all neighbours are the same color
    if(current_color != right_neighbour_color or current_color != left_neighbour_color or current_color != top_neighbour_color or current_color != bottom_neighbour_color): 
        return True

    return False


# Priority is determined by the red, green and blue value, the red is most significant, the blue the least, a value is generated using bit shifting
# This is the same as in PlaceNL's userscript getPriority function https://github.com/PlaceNL/Userscript/blob/master/src/util/orderUtil.js
def get_priority(red, green, blue, alpha):

    if(alpha == 0):
        return 0
    
    priority = red << 16 | green << 8 | blue

    return priority

def change_prio(old_prio: Image, new_prio: Image, x: int, y: int, change: int):
    r, g, b, a = old_prio.getpixel((x, y))

    # We determine the priority value
    priority = get_priority(r, g, b, a)

    if(priority > 0):
        # Only if priority > 0 we change it
        priority += change
    
    if(priority > priority_max):
        priority = priority_max
    
    if(priority < 0):
        priority = 0

    new_r = (priority >> 16) & 0xFF
    new_g = (priority >> 8) & 0xFF
    new_b = priority & 0xFF

    new_prio.putpixel((x, y), (new_r, new_g, new_b, a))

