from random import randint
import numpy as np
import matplotlib.pyplot as plt

"""
    custom addition
"""
import matplotlib.pyplot as plt


def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted number that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use
    """
    counts = np.zeros(len(bins) - 1)
    for val in data:
        k=0
        while val > bins[k + 1]:
            k+=1
        counts[k]+=1

    return (counts, bins)


def plot_histogram(bins_count):
    """
        Quesion 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommand using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    plt.hist(bins_count[1][:-1], bins_count[1], weights=bins_count[0], density=True)
    plt.show()


if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    print(compute_histogram_bins(data=data, bins=bins))
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
