import matplotlib.pyplot as plt
for j in range(5):
    g=str(j+1)
    with open ("00"+g+".dat",'r') as f:
        s=f.read().split('\n')
        x=[]
        y=[]
        for i in range(int(s[0])):
            x.append(float(s[i+1].split()[0]))
            y.append(float(s[i+1].split()[1]))
        plt.plot(x,y,marker='o',linestyle='')
        plt.savefig(g+".png")
        plt.show()