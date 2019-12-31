import matplotlib.pyplot as plt

from die import Die

die = Die()

results = [die.roll() for i in range(100)]

frequencies = [results.count(value) for value in range(1,die.num_sides + 1)]

x_label = [str(x) for x in range(1,die.num_sides+1)]
#展示结果
plt.bar(x_label,frequencies,color="blue")
plt.title("Square Number",fontsize=24)

plt.show()