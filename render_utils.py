import math

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

def draw_debug_info(rl, pts, lengths, angles, target, origin, scale, it, dist, max_iter, tol):
    # Accessible area
    total_length = sum(lengths)
    rl.draw_circle_lines(origin[0], origin[1], total_length * scale, rl.LIGHTGRAY)

    # Debug overlay
    x_pos = 20
    status = "CONVERGENT" if dist < tol else ("OUT OF REACH" if sum(lengths) < math.hypot(*target) else "MAX ITER")
    color_status = rl.GREEN if status == "CONVERGENT" else rl.ORANGE

    rl.draw_text(f"-- DEBUG MODE --", x_pos, 20, 18, rl.VIOLET)
    rl.draw_text(f"Status: {status}", x_pos, 45, 16, color_status)
    rl.draw_text(f"Iteration: {it} / {max_iter}", x_pos, 65, 16, rl.DARKGRAY)
    rl.draw_text(f"Dist Error: {dist:.4f} (Tol: {tol})", x_pos, 85, 16, rl.DARKGRAY)

    # Tampilkan Sudut setiap joint
    rl.draw_text("Joint angles:", x_pos, 115, 16, rl.DARKGRAY)
    for idx, ang in enumerate(angles):
        deg = math.degrees(ang)
        rl.draw_text(f"- Joint {idx+1}: {deg:.1f} deg", x_pos, 135 + (idx * 20), 15, rl.DARKGRAY)