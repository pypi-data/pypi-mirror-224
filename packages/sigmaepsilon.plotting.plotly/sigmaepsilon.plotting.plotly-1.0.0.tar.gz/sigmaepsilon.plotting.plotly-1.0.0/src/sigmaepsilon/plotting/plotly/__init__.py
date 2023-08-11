from .d1 import scatter_lines_3d, stack_lines_3d, scatter_points_3d, plot_lines_3d
from .d2 import plot_triangles_2d, plot_triangles_3d

__all__ = [
    "scatter_lines_3d",
    "stack_lines_3d",
    "scatter_points_3d",
    "plot_lines_3d",
    "plot_triangles_2d",
    "plot_triangles_3d",
]

import importlib.metadata

__pkg_name__ = "sigmaepsilon.plotting.plotly"
__version__ = importlib.metadata.version(__pkg_name__)
__description__ = "Utilities for plotting with Plotly."
