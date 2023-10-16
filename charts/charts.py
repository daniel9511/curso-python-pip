import matplotlib as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200,32,120]

    fig, ax = plt.subplosts()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()




