from math import hypot, atan2, acos, sin, cos, pi, degrees, radians

def optim_coord(clear_resul: list, R: int):
    wi_bst = 0
    coor_bst = (0,0)
    clear_resul.sort()
    for xi, yi, wi, in clear_resul:
        mas_coor_bas = []
        if wi > wi_bst:
            wi_bst = wi
            coor_bst = (xi, yi)
        for xj, yj, wj in clear_resul:
            if (xi == xj and yi == yj):
                continue
            d = hypot(xj-xi, yj-yi)
            if d > 2*R:
                continue
            ugol_phii = atan2(yj - yi, xj - xi) # расположение базы относительное
            a_dip = acos(d/(2*R)) # половина растояния
            diap_1 = degrees((ugol_phii - a_dip))
            diap_2 = degrees((ugol_phii + a_dip))
            for i in (0.0, 360.0):
                mas_coor_bas.append((diap_1 + i, 0, wj))
                mas_coor_bas.append((diap_2 + i, 1, -wj))
        mas_coor_bas.sort()
        suum = 0
        for a, _, ww in mas_coor_bas:
            suum += ww
            if wi + suum > wi_bst:
                wi_bst = wi + suum
                coor_bst = (xi + (R*cos(radians(a))), yi + (R*sin(radians(a))))
    x_t, y_t = coor_bst
    return x_t, y_t

def neravenstvo(R: int, x_t: float, y_t: float, clear_resul: list):
    W = 0            
    for x, y, w, in clear_resul:
        if ((x_t - x)**2 + (y_t - y)**2) <= pow(R,2) + 1e-7:
            W += w
    return W 