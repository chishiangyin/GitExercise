#Ising Model
import numpy as np
import matplotlib.pyplot as plt

def initial_state(N):
    """生成一个N x N的随机自旋格点"""
    return np.random.choice([-1, 1], size=(N, N))

def delta_energy(grid, x, y, J=1):
    """计算在位置(x, y)翻转自旋的能量变化"""
    s = grid[x, y]
    neighbors = grid[(x+1)%N, y] + grid[x-1, y] + grid[x, (y+1)%N] + grid[x, y-1]
    return 2 * J * s * neighbors

def metropolis_step(grid, beta):
    """执行一个Metropolis更新步骤"""
    N = grid.shape[0]
    for _ in range(N**2):  # 每次迭代N^2次保证每个自旋都有机会更新
        x, y = np.random.randint(N), np.random.randint(N)
        dE = delta_energy(grid, x, y)
        if dE <= 0 or np.random.rand() < np.exp(-dE * beta):
            grid[x, y] *= -1

def magnetization(grid):
    """计算网格的磁化强度"""
    return np.sum(grid) / grid.size  # 去掉绝对值以考虑磁化的方向

# 模拟参数
N = 30
temperatures = np.linspace(0, 5, 10)  # 温度范围从0到5，共100个数据点
magnetizations = []
steps_eq = 30  # 增加等待系统平衡的步骤数
steps_meas = 3  # 增加测量磁化强度的步骤数

# 模拟过程
for T in temperatures:
    grid = initial_state(N)
    beta = 1.0 / T if T > 0 else float('inf')  # 温度为0时beta设为无穷大
    for _ in range(steps_eq):
        metropolis_step(grid, beta)
    mag = 0
    for _ in range(steps_meas):
        metropolis_step(grid, beta)
        mag += magnetization(grid)
    magnetizations.append(mag / steps_meas)

# 绘制结果
plt.scatter(temperatures, magnetizations, color='blue')
plt.xlabel('Temperature (T)')
plt.ylabel('Magnetization (M)')
plt.title('Magnetization vs. Temperature for a 2D Ising Model')
plt.show()