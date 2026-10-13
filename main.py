import pyray as rl
from kinematics import fk,ccd
from render_utils import to_screen, to_world, draw_arm

def main():

    # config
    length = [2.0, 1.5, 1.25]
    angles = [0.0, 0.0, 0.0]
    base = [0.0, 0.0]
    
    origin = [400, 320]
    scale = 40

    rl.init_window(800, 640, "CCD Simulation")
    rl.set_target_fps(60)

    while not rl.window_should_close():
        
        #input
        mouse_pos = rl.get_mouse_position()
        target = to_world(mouse_pos.x, mouse_pos.y, origin, scale)

        #update
        ccd(base, length, angles, target, max_iter=20)
        pts = fk(base, length, angles)

        #render
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)

        draw_arm(rl, pts, origin, scale)

        tx, ty = to_screen(target, origin, scale)
        rl.draw_circle_lines(int(tx), int(ty), 8, rl.RED)

        rl.draw_text("Use mouse / touchpad to move the target", 20, 620, 16, rl.LIGHTGRAY)

        rl.end_drawing()
    rl.close_window()

if __name__ == "__main__":
    main()