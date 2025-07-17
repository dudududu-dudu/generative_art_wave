def setup():
    global w, s, t
    size(500, 300)
    w = width
    s = 5  # grid间隔
    t = 0
    background(0)
    stroke(0)
    colorMode(HSB, 360, 100, 100, 100)
    noFill()
    
def draw():
    global t
    t += 0.01
    background(0)
    h = 215 + 15 * sin(t * 2)
    stroke(h, 80, 100, 100)
    
    for y in range(0, w, s):  # 0~width, step 5px
        for x in range(0, w, s):
            # 三角の頂点:
            p1 = a(x, y)
            # p2 = (x, y)
            p2 = p1
            p3 = a(x + s, y + s)
            # print p2
            
            triangle(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])

    
def a(x, y):
    e = w / 2.0 - y
    d = noise(t + x / 190.0) / 8.0 + \
        noise(x / 30.0, y / 40.0 - t * 5) / 8.0 + \
        e * 0.002

    new_x = x
    new_y = new_y = y / (6 + d * 9 + t * 0.2) - d * 90 + 100

    return (new_x, new_y)
