from .parallel import parallel, aligned_parallel
from .d2 import plot_triangles_2d
from .triplot import triplot

__all__ = ["parallel", "aligned_parallel", "plot_triangles_2d", "triplot"]

import importlib.metadata

__pkg_name__ = "sigmaepsilon.plotting.mpl"
__version__ = importlib.metadata.version(__pkg_name__)
__description__ = "Utilities for plotting with matplotlib."