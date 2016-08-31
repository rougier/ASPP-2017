import numpy as np
import matplotlib.pyplot as plt


x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])


def fit(x):
    return 3 + 0.5*x


fig = plt.figure(figsize=(10,8))
fig.patch.set_facecolor('white')

xfit = np.array([np.amin(x), np.amax(x)])

ax = plt.subplot(221)
plt.plot(xfit, fit(xfit), '.75', lw=1, zorder=-10)
plt.scatter(x, y1, s=50, edgecolor="k", facecolor="w", linewidth=2, zorder=10)
plt.xlim(2,20), plt.xticks(np.arange(4,20,2))
plt.ylim(2,14), plt.yticks(np.arange(4,14,2))
plt.title('What we expect...', loc='left', color='r', fontsize=16)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 1))
ax.spines['bottom'].set_color('0.5')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 1))
ax.spines['left'].set_color('0.5')
[t.set_color('0.5') for t in ax.xaxis.get_ticklines()]
[t.set_color('0.5') for t in ax.xaxis.get_ticklabels()]
[t.set_color('0.5') for t in ax.yaxis.get_ticklines()]
[t.set_color('0.5') for t in ax.yaxis.get_ticklabels()]


ax = plt.subplot(222)
plt.plot(xfit, fit(xfit), '.75', lw=1, zorder=-10)
plt.scatter(x, y2, s=50, edgecolor="k", facecolor="w", linewidth=2, zorder=10)
plt.xlim(2,20), plt.xticks(np.arange(4,20,2))
plt.ylim(2,14), plt.yticks(np.arange(4,14,2))
plt.title('The non-linear case', loc='left', color='r', fontsize=16)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 1))
ax.spines['bottom'].set_color('0.5')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 1))
ax.spines['left'].set_color('0.5')
[t.set_color('0.5') for t in ax.xaxis.get_ticklines()]
[t.set_color('0.5') for t in ax.xaxis.get_ticklabels()]
[t.set_color('0.5') for t in ax.yaxis.get_ticklines()]
[t.set_color('0.5') for t in ax.yaxis.get_ticklabels()]


ax = plt.subplot(223)
plt.plot(xfit, fit(xfit), '.75', lw=1, zorder=-10)
plt.scatter(x, y3, s=50, edgecolor="k", facecolor="w", linewidth=2, zorder=10)
plt.xlim(2,20), plt.xticks(np.arange(4,20,2))
plt.ylim(2,14), plt.yticks(np.arange(4,14,2))
plt.title('The Y outlier case', loc='left', color='r', fontsize=16)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 1))
ax.spines['bottom'].set_color('0.5')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 1))
ax.spines['left'].set_color('0.5')
[t.set_color('0.5') for t in ax.xaxis.get_ticklines()]
[t.set_color('0.5') for t in ax.xaxis.get_ticklabels()]
[t.set_color('0.5') for t in ax.yaxis.get_ticklines()]
[t.set_color('0.5') for t in ax.yaxis.get_ticklabels()]


ax = plt.subplot(224)
xfit = np.array([np.amin(x4), np.amax(x4)])
plt.plot(xfit, fit(xfit), '.75', lw=1, zorder=-10)
plt.scatter(x4, y4, s=50, edgecolor="k", facecolor="w", linewidth=2, zorder=10)
plt.xlim(2,20), plt.xticks(np.arange(4,20,2))
plt.ylim(2,14), plt.yticks(np.arange(4,14,2))
plt.title('The X outlier case', loc='left', color='r', fontsize=16)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 1))
ax.spines['bottom'].set_color('0.5')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 1))
ax.spines['left'].set_color('0.5')
[t.set_color('0.5') for t in ax.xaxis.get_ticklines()]
[t.set_color('0.5') for t in ax.xaxis.get_ticklabels()]
[t.set_color('0.5') for t in ax.yaxis.get_ticklines()]
[t.set_color('0.5') for t in ax.yaxis.get_ticklabels()]


plt.tight_layout()
plt.savefig("anscombe.pdf")
plt.show()
