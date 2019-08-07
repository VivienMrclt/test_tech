"""
    addition
"""
import random

from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram
import numpy as np


class PeerQ4(Peer):

    def send_data_to_backend(self):
        """
            Question 4: implement this method
        """
        res = np.zeros(6001)
        for val in self.peer_pool.values():
            val = int(val * 10)
            res[val] += 1
        return res

def find_value_of_index(array, index):
    cumul = array[0]
    i = 0
    while (cumul < index):
        i+=1
        cumul += array[i]
    return i


class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 4: implement this method
        """
        data = np.sum(self.backend_database, axis=0)

        size = np.sum(data)

        k = int(2 * np.power(size, 1/3))

        bins = [i * 600 / k for i in range(k+1)]
        counts = []

        i = 0
        for val, count in enumerate(data[:-1]):
            if val/10 < bins[i]:
                counts[-1] += count
            else:
                counts.append(count)
                i+=1

        plot_histogram((counts, bins))


if __name__ == "__main__":

    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()
    #
    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
