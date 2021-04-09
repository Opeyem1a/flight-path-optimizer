import math
import string

import dill

import matplotlib.pyplot as plt
import numpy as np
from plots.plot_data import *


def plot_line(best_alg: bool, vary: string):
    is_v = vary == 'v'
    rng = seq_vary_v if is_v else seq_vary_e
    if not vary == 'v' and not vary == 'e':
        return None

    x = [*rng]
    y = []
    y2 = []

    if not is_v and not best_alg:
        # O(V^2 * b^2), where V = const_num_airports, but basically O(E^2)
        y = [0.00001 * (b**2) for b in x]
        plt.plot(x, y, label='Predicted - O(b^2 * V^2)')

    if is_v and not best_alg:
        b = const_num_flights
        b2 = b ** 2  # i.e. b^2
        y = [0.00000000007 * (V ** 2) * b2 for V in x]
        plt.plot(x, y, label='Predicted - O(b^2 * V^2)')

    if is_v and best_alg:
        b = const_num_flights
        for V in rng:
            y.append(0.000000002 * b * (V ** 2))
            y2.append(0.00000002 * b * V * math.log(V))
        plt.plot(x, y, label='Predicted - O(bV^2)')
        plt.plot(x, y2, label='Predicted - O(bVlog(V))')

    if not is_v and best_alg:
        V = const_num_airports
        for b in rng:
            y.append(0.000000005 * b * (V**2))
            y2.append(0.00000012 * b * V * math.log(V))
        plt.plot(x, y, label='Predicted - O(bV^2)')
        plt.plot(x, y2, label='Predicted - O(bVlog(V))')


def plot_runtime(best_alg: bool, vary: string):
    run_type = 'best' if best_alg else 'worst'
    dest_file_name = f'{dest_directory}vary_{vary}_{run_type.lower()}_data.pkl'
    is_v = vary == 'v'
    rng = seq_vary_v if is_v else seq_vary_e

    if not vary == 'v' and not vary == 'e':
        return None

    with open(dest_file_name, 'rb') as f:
        times = dill.load(f)

    x = [*rng]
    y = []

    for time in times:
        y.append(0 - time)  # TODO: will be positive in the real run, so no need to flip the signs

    x_label = 'V (number of airports)' if is_v else 'b (max number of outgoing flights)'
    line_label = 'Better Algorithm' if best_alg else 'Worse Algorithm'
    plt.plot(x, y, label=line_label)
    plt.title('Algorithm Runtimes')
    plt.xlabel(x_label)
    plt.ylabel('t (execution time in seconds)')


def plot_v(best_alg: bool):
    plot_runtime(best_alg, 'v')
    plot_line(best_alg, 'v')
    plt.legend()
    plt.show()


def plot_e(best_alg: bool):
    plot_runtime(best_alg, 'e')
    plot_line(best_alg, 'e')
    plt.legend()
    plt.show()


# Comment one of these out at a time for each of the 2 plots
plot_v(True)
plot_v(False)
plot_e(True)
plot_e(False)
