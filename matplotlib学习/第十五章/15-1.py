import matplotlib.pyplot as plt

x = list(range(1,5001))
y = [value ** 3 for value in x]

plt.scatter(x,y,c=x,cmap=plt.cm.GnBu,s=4)

plt.title("Square Number",fontsize=24)
plt.xlabel("Values",fontsize=14)
plt.ylabel("Noun of Values",fontsize=14)

plt.tick_params(axis="both",labelsize=14)

plt.show()