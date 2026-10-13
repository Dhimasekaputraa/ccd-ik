import math

def fk(base, length, angles):   #Menghitung posisi tiap joint dari base sampai end effector
    x, y, phi = base[0], base[1], 0.0
    pts = [(x, y)]
    for L, theta in zip(length, angles):
        phi += theta
        x += L * math.cos(phi)
        y += L * math.sin(phi)
        pts.append((x, y))
    return pts

def ccd(base, length, angles, target, max_iter=20, tol=1e-3):   #Mengubah nilai sudut dari joint luar ke dalam
    tx, ty = target
    n = len(angles)

    for it in range(1, max_iter + 1):
        for i in range(n-1, -1, -1):
            pts = fk(base, length, angles)
            px, py = pts[i]     #Koordinat pivot ke joint [i]
            ex, ey = pts[-1]    #Koordinat end effector

            #vector a : pivot ke end effector
            #vector b : pivot ke target
            ax, ay = ex - px, ey - py
            bx, by = tx - px, ty - py

            dot = ax * bx + ay * by
            cross = ax * by - ay * bx

            #Perubahan sudut dan update sudut joint
            angles[i] += math.atan2(cross, dot)
            angles[i] = math.atan2(math.sin(angles[i]), math.cos(angles[i]))

        ex, ey = fk(base, length, angles)[-1]
        if math.hypot(tx - ex, ty -ey) < tol :
            break
    
    return angles