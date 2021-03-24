import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from votes import wide as df


def make_plot():
    df = pd.read_csv('uk-election-results.csv')
    fig, ax = plt.subplots()
    # The x-values of the bars.
    years = df['year']
    x = np.arange(len(years))

    # The width of the bars (1 = the whole width of the 'year group')
    width = 0.15

    # Create the bar charts!
    ax.bar(x - 3 * width / 2, df['conservative'], width, label='Conservative', color='#0343df')
    ax.bar(x - width / 2, df['labour'], width, label='Labour', color='#e50000')
    ax.bar(x + width / 2, df['liberal'], width, label='Liberal', color='#ffff14')
    ax.bar(x + 3 * width / 2, df['others'], width, label='Others', color='#929591')
    # Notice that features like labels and titles are added in separate steps
    ax.set_ylabel('Seats')
    ax.set_title('UK election results')

    ax.set_xticks(x)  # This ensures we have one tick per year, otherwise we get fewer
    ax.set_xticklabels(years.astype(str).values, rotation='vertical')

    ax.legend()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_plot()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
