import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dpi = 100
res = 200

x = np.linspace(-6, 6, res)
y = np.linspace(-6, 6, res)
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(1280/dpi, 720/dpi), dpi=dpi, facecolor='black')
ax = fig.add_axes([0, 0, 1, 1], facecolor='black')

def generate(frame):
    t = frame * 0.02

    f1 = 0.8 + 0.3 * np.sin(t * 0.1)
    f2 = 0.9 + 0.3 * np.cos(t * 0.15)

    warp_x = np.sin(Y * f1 + t * 0.4) + t * 0.5
    warp_y = np.cos(X * f2 - t * 0.3) + t * 0.3

    nx = X * 0.7 + warp_x
    ny = Y * 0.7 + warp_y

    z = np.sin(nx * 1.2 + np.cos(ny * 0.9 + t * 0.2)) * np.cos(ny * 1.3 + np.sin(nx * 0.8 - t * 0.2))
    z += 0.8 * np.sin(nx * 0.6 + t * 0.3) * np.cos(ny * 0.4 - t * 0.1)
    z += 0.5 * np.cos(nx * 1.5 - ny * 1.1 + t * 0.4)

    return z

def update(frame):
    ax.clear()
    ax.set_facecolor('black')

    Z = generate(frame)

    ax.contour(
        X, Y, Z,
        levels=12,
        colors='white',
        linewidths=2.5,
        linestyles='solid',
        antialiased=True
    )

    ax.set_axis_off()
    return []

ani = FuncAnimation(
    fig,
    update,
    frames=None,
    interval=16,
    blit=False,
    cache_frame_data=False
)

plt.show()
