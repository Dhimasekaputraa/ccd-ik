def to_screen(p, origin, scale):    #Koordinat matematika ke layar
    return(origin[0] + p[0] * scale, origin[1] - p[1] * scale)

def to_world(sx, sy, origin, scale):    #Koordinat layar ke matematika
    return ((sx - origin[0]) / scale, (origin[1] - sy) / scale)

def draw_arm(rl, pts, origin, scale):
    sp = [to_screen(p, origin, scale) for p in pts]

    #lengan
    for a, b in zip(sp, sp[1:]):
        rl.draw_line_ex(a, b, 8, rl.VIOLET)
    
    #joint
    for p in sp[:-1]:
        rl.draw_circle(int(p[0]), int(p[1]), 6, rl.DARKGRAY)
    
    #end effector
    rl.draw_circle(int(sp[-1][0]), int(sp[-1][1]), 5, rl.GREEN)