class point(object):
    """point class"""
class rectangle(object):
    """rectangle class"""
def create_rectangle(x, y, w, h):
    pnt = point()
    pnt.x = x
    pnt.y = y
    rect = rectangle()
    rect.w = w
    rect.h = h
    rect.corner = pnt
    return rect

def str_rectangle(rect):
    return "(%d, %d, %d, %d)" % (rect.corner.x, rect.corner.y, rect.w, rect.h)

def shift_rectangle(rect, dx, dy):
    rect.corner.x = rect.corner.x + dx
    rect.corner.y = rect.corner.y + dy

def offset_rectangle(rect, dx, dy):
    x = rect.corner.x + dx
    y = rect.corner.y + dy
    return create_rectangle(x, y, rect.w, rect.h)
