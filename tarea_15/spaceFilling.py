import matplotlib.pyplot as plt


def hilberto(x, y, n, dx, dy):
    if n == 1:
        print(f"{x}, {y}")
        px.append(x)
        py.append(y)
    else:
        n = n // 2
        lg = n
        hilberto(x + dx * lg, y + dx * lg, n, dx, 1 - dy)
        hilberto(x + dy * lg, y + (1 - dy) * lg, n, dx, dy)
        hilberto(x + (1 - dx) * lg, y + (1 - dx) * lg, n, dx, dy)
        hilberto(x + (1 - dy) * lg, y + dy * lg, n, 1 - dx, dy)


def hilbert3D(s, x, y, z, dx, dy, dz, dx2, dy2, dz2, dx3, dy3, dz3):
    if s == 1:
        px.append(x)
        py.append(y)
        pz.append(z)
    else:
        s /= 2
        if dx < 0:
            x -= s * dx
        if dy < 0:
            y -= s * dy
        if dz < 0:
            z -= s * dz
        if dx2 < 0:
            x -= s * dx2
        if dy2 < 0:
            y -= s * dy2
        if dz2 < 0:
            z -= s * dz2
        if dx3 < 0:
            x -= s * dx3
        if dy3 < 0:
            y -= s * dy3
        if dz3 < 0:
            z -= s * dz3
        hilbert3D(s, x, y, z, dx2, dy2, dz2, dx3, dy3, dz3, dx, dy, dz)
        hilbert3D(s, x + s * dx, y + s * dy, z + s * dz, dx3, dy3, dz3, dx, dy, dz, dx2, dy2, dz2)
        hilbert3D(s, x + s * dx + s * dx2, y + s * dy + s * dy2, z + s * dz + s * dz2, dx3, dy3, dz3, dx, dy, dz, dx2,
                  dy2, dz2)
        hilbert3D(s, x + s * dx2, y + s * dy2, z + s * dz2, -dx, -dy, -dz, -dx2, -dy2, -dz2, dx3, dy3, dz3)
        hilbert3D(s, x + s * dx2 + s * dx3, y + s * dy2 + s * dy3, z + s * dz2 + s * dz3, -dx, -dy, -dz, -dx2, -dy2,
                  -dz2, dx3, dy3, dz3)
        hilbert3D(s, x + s * dx + s * dx2 + s * dx3, y + s * dy + s * dy2 + s * dy3, z + s * dz + s * dz2 + s * dz3,
                  -dx3, -dy3, -dz3, dx, dy, dz, -dx2, -dy2, -dz2)
        hilbert3D(s, x + s * dx + s * dx3, y + s * dy + s * dy3, z + s * dz + s * dz3, -dx3, -dy3, -dz3, dx, dy, dz,
                  -dx2, -dy2, -dz2)
        hilbert3D(s, x + s * dx3, y + s * dy3, z + s * dz3, dx2, dy2, dz2, -dx3, -dy3, -dz3, -dx, -dy, -dz)


px = []
py = []
pz = []
# hilberto(0, 0, math.pow(2, 4), 0, 0)
hilbert3D(8, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1)
# plt.plot(px, py, 'o-')
# plt.show()
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='3d')
ax.plot(px, py, pz)
plt.show()
