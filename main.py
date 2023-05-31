# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
def get_iter(c:complex, thresh:int =4, max_steps:int =25) -> int:
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z=z*z +c
        i+=1
    return i

def plotter(n, thresh, max_steps=25):
    mx = 2.48 / (n-1)
    my = 2.26 / (n-1)
    mapper = lambda x,y: (mx*x - 2, my*y - 1.13)
    img=np.full((n,n), 255)
    for x in range(n):
        for y in range(n):
            it = get_iter(complex(*mapper(x,y)), thresh=thresh, max_steps=max_steps)
            img[y][x] = 255 - it
    return img

filenames = []
for i in range(1, 500, 1):
    n=1000
    img = plotter(n, thresh=i/100, max_steps=50)
    plt.imshow(img)
    plt.axis("off")
    plt.savefig(fr"\imgs\img{i}.png")
    # plt.show()


import imageio
# with imageio.get_writer('movie.gif', mode='I') as writer:
#     for filename in filenames:
#         image = imageio.imread(filename)
#         writer.append_data(image)
with imageio.get_writer('movie.gif', mode='I') as writer:
    for i in range(1, 500, 1):
        try:
            image = imageio.imread(fr"imgs\img{i}.png")
            writer.append_data(image)
        except:
            continue


