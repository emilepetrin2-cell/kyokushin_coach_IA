import numpy as np
def calculer_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    v = a - b
    u = c - b
    scalaire = np.dot(v, u)
    euclide1 = np.linalg.norm(u)
    euclide2 = np.linalg.norm(v)
    if euclide1 == 0 or euclide2 == 0:
        return 0.0
    cosinus = (scalaire / (euclide1 * euclide2))
    angle_clip = np.clip(cosinus, -1, 1)
    angle_arcos = np.arccos(angle_clip)
    angle = float(np.degrees(angle_arcos))
    return angle
