import matplotlib.pyplot as plt
with open ("frames.dat.txt",'r') as f:
    s=f.read().split('\n')

    for i in range (6):
        x=[]
        y=[]
        print(s[2*i])
        for a in range(101):
            x.append(float(s[2*i].split()[a]))
            print(a)
        for a in range(101):
            y.append(float(s[2*i+1].split()[a]))
        qw=str(i+1)
        print(qw)
        plt.plot(x,y)
        plt.ylim(-15,15)
        plt.grid()
        plt.savefig(qw+".png")
        plt.show()