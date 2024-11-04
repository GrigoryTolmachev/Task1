import matplotlib.pyplot as plt
with open ("001.dat",'r') as f:
    s=f.read().split('\n')
    x=[]
    y=[]
    for i in range(int(s[0])):
        x.append(float(s[i+1].split()[0]))
        y.append(float(s[i+1].split()[1]))
    plt.plot(x,y,marker='o',linestyle='')
    plt.savefig("1.png")
    plt.show()