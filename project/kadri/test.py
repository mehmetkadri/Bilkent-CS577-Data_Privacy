# import plt 
import matplotlib.pyplot as plt

a = 0.9133333333333333
b = 0.9333333333333333
c = 0.9366666666666666
d = 0.98

x = ['Original 1 vs Original 2', 'Original 1 vs Salient', 'Original 1 vs Face', 'Salient vs Face']
y = [a, b, c, d]

# make the x axis to be the name of the comparison, 90 degree rotation
plt.xticks(rotation=10)
# change the color of the bar for each comparison
plt.bar(x, y, color=['#F4B678', '#7CC674', '#519DE9', '#B2B0EA'])
plt.show()

