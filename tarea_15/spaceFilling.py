import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def hilberto(n, x, y, dx, dy):
    if n == 1:
        px.append(x)
        py.append(y)
    else:
        n = n // 2
        lg = n
        hilberto(n, x + dx * lg, y + dx * lg, dx, 1 - dy)
        hilberto(n, x + dy * lg, y + (1 - dy) * lg, dx, dy)
        hilberto(n, x + (1 - dx) * lg, y + (1 - dx) * lg, dx, dy)
        hilberto(n, x + (1 - dy) * lg, y + dy * lg, 1 - dx, dy)


def hilberto3D(n, x, y, z, dx, dy, dz, dx2, dy2, dz2, dx3, dy3, dz3):
    if n == 1:
        px.append(x)
        py.append(y)
        pz.append(z)
    else:
        n /= 2
        if dx < 0:
            x -= n * dx
        if dy < 0:
            y -= n * dy
        if dz < 0:
            z -= n * dz
        if dx2 < 0:
            x -= n * dx2
        if dy2 < 0:
            y -= n * dy2
        if dz2 < 0:
            z -= n * dz2
        if dx3 < 0:
            x -= n * dx3
        if dy3 < 0:
            y -= n * dy3
        if dz3 < 0:
            z -= n * dz3
        hilberto3D(n, x, y, z, dx2, dy2, dz2, dx3, dy3, dz3, dx, dy, dz)
        hilberto3D(n, x + n * dx, y + n * dy, z + n * dz, dx3, dy3, dz3, dx, dy, dz, dx2, dy2, dz2)
        hilberto3D(n, x + n * dx + n * dx2, y + n * dy + n * dy2, z + n * dz + n * dz2, dx3, dy3, dz3, dx, dy, dz, dx2,
                   dy2, dz2)
        hilberto3D(n, x + n * dx2, y + n * dy2, z + n * dz2, -dx, -dy, -dz, -dx2, -dy2, -dz2, dx3, dy3, dz3)
        hilberto3D(n, x + n * dx2 + n * dx3, y + n * dy2 + n * dy3, z + n * dz2 + n * dz3, -dx, -dy, -dz, -dx2, -dy2,
                   -dz2, dx3, dy3, dz3)
        hilberto3D(n, x + n * dx + n * dx2 + n * dx3, y + n * dy + n * dy2 + n * dy3, z + n * dz + n * dz2 + n * dz3,
                   -dx3, -dy3, -dz3, dx, dy, dz, -dx2, -dy2, -dz2)
        hilberto3D(n, x + n * dx + n * dx3, y + n * dy + n * dy3, z + n * dz + n * dz3, -dx3, -dy3, -dz3, dx, dy, dz,
                   -dx2, -dy2, -dz2)
        hilberto3D(n, x + n * dx3, y + n * dy3, z + n * dz3, dx2, dy2, dz2, -dx3, -dy3, -dz3, -dx, -dy, -dz)


def plotHilbert(n: int):
    px.clear()
    py.clear()
    figure(figsize=(2*n,2*n),dpi=80)
    hilberto(pow(2, n), 0, 0, 0, 0)
    plt.plot(px, py, 'o-')
    plt.axis('off')
    #plt.tight_layout()
    plt.show()


def plotHilbert3D(n: int):
    px.clear()
    py.clear()
    pz.clear()
    hilberto3D(pow(2, n), 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1)
    fig = plt.figure(figsize=(4*n, 4*n))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(px, py, pz, "o-")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    px = []
    py = []
    pz = []
    plotHilbert(3)
