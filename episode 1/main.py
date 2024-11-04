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
with open ("002.dat",'r') as f:
    s=f.read().split('\n')
    x=[]
    y=[]
    for i in range(int(s[0])):
        x.append(float(s[i+1].split()[0]))
        y.append(float(s[i+1].split()[1]))
    plt.plot(x,y,marker='o',linestyle='')
    plt.savefig("2.png")
    plt.show()
with open ("003.dat",'r') as f:
    s=f.read().split('\n')
    x=[]
    y=[]
    for i in range(int(s[0])):
        x.append(float(s[i+1].split()[0]))
        y.append(float(s[i+1].split()[1]))
    plt.plot(x,y,marker='o',linestyle='')
    plt.savefig("3.png")
    plt.show()
with open ("004.dat",'r') as f:
    s=f.read().split('\n')
    x=[]
    y=[]
    for i in range(int(s[0])):
        x.append(float(s[i+1].split()[0]))
        y.append(float(s[i+1].split()[1]))
    plt.plot(x,y,marker='o',linestyle='')
    plt.savefig("4.png")
    plt.show()
with open ("005.dat",'r') as f:
    s=f.read().split('\n')
    x=[]
    y=[]
    for i in range(int(s[0])):
        x.append(float(s[i+1].split()[0]))
        y.append(float(s[i+1].split()[1]))
    plt.plot(x,y,marker='o',linestyle='')
    plt.savefig("5.png")
    plt.show()