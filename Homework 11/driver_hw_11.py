import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.6
N_experiments = 100000
N_bins = 100


def main(n_meas):
    raw_exponential = (np.random.exponential(LAMBDA, (N_experiments, n_meas)))
    mean_per_experiment = np.sum(raw_exponential, -1) / n_meas
    plt.hist(mean_per_experiment, bins=N_bins, density=True)
    plt.xlabel(f'Average over {n_meas} measurements')
    plt.ylabel(f'Probability density of average')
    plt.savefig(f'./outputs/average_over_{n_meas}_measurements.png')
    plt.show()


if __name__ == '__main__':
    main(40)
