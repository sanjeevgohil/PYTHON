import matplotlib.pyplot as plt
fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

lang = ["C", "C++", "JAVA", "Python", "PHP"]
stud = [23, 17, 35, 29, 12]

ax.bar(lang, stud)
plt.show()