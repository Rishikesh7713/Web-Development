import matplotlib.pylab as plt
player_names=["Ronaldo","Sergio Ramos","Jack","Alexander Arnold","Vini jr"]
player_goals=[957,17,31,51,122]

def linechart():
    plt.plot(player_names,player_goals,marker="o",ms=20,mec="r")
    plt.title("Player's Goals")
    plt.xlabel("Player Names")
    plt.ylabel("Player's Goals")
    plt.show()
linechart()

def bar_chart():
    plt.bar(player_names,player_goals)
    plt.title("Player's Goals")
    plt.xlabel("Player Names")
    plt.ylabel("Player's Goals")
    plt.show()
bar_chart()