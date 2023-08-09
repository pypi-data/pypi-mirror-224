import unittest
import numpy as np

from sigmaepsilon.core.testing import SigmaEpsilonTestCase
from sigmaepsilon.plotting.mpl import parallel


class TestParallel(SigmaEpsilonTestCase):

    def test_parallel_plot_1(self):
        colors = np.random.rand(150, 3)
        labels = [str(i) for i in range(10)]
        values = np.random.rand(10, 150)
        parallel(
            values,
            labels=labels,
            padding=0.05,
            lw=0.2,
            colors=colors,
            title="Parallel Plot with Random Data",
            return_figure=False,
            bezier=False
        )
        
    def test_parallel_plot_2(self):
        colors = np.random.rand(150, 3)
        values = {str(i): np.random.rand(150) for i in range(10)}
        parallel(
            values,
            padding=0.05,
            lw=0.2,
            colors=colors,
            title="Parallel Plot with Random Data",
            return_figure=False,
            bezier=False
        )
        
    def test_parallel_plot_3(self):
        colors = np.random.rand(150, 3)
        labels = [str(i) for i in range(10)]
        values = [np.random.rand(150) for _ in range(10)]
        parallel(
            values,
            labels=labels,
            padding=0.05,
            lw=0.2,
            colors=colors,
            title="Parallel Plot with Random Data",
            return_figure=False,
            bezier=False
        )
        
    def test_parallel_plot_4(self):
        colors = np.random.rand(150, 3)
        labels = [str(i) for i in range(10)]
        values = [np.random.rand(150) for _ in range(10)]
        parallel(
            values,
            labels=labels,
            padding=0.05,
            lw=0.2,
            colors=colors,
            title="Parallel Plot with Random Data",
            return_figure=False,
            bezier=True
        )
        
        
if __name__ == "__main__":
    unittest.main()
