import plotly.graph_objects as go

from sigmaepsilon.mesh.utils.topology import unique_topo_data
from sigmaepsilon.mesh.utils.tri import edges_tri
from .d1 import stack_lines_3d


__all__ = ['plot_triangles_2d', 'plot_triangles_3d']


def plot_triangles_2d(points, data=None) -> go.Figure:
    """
    Plots a triangulation with attached field data.
    
    Parameters
    ----------
    points: numpy.ndarray
        2d float array of points.
    data: numpy.ndarray
        1d float array of scalar data over the points.
        
    Returns
    -------
    figure: :class:`plotly.graph_objects.Figure`
        The figure object.
            
    Example
    -------
    >>> from sigmaepsilon.mesh.grid import grid
    >>> from sigmaepsilon.mesh.utils.topology.tr import Q4_to_T3
    >>> from sigmaepsilon.plotting.plotly import plot_triangles_2d
    >>> import numpy as np
    >>> gridparams = {
    >>>     'size' : (1200, 600),
    >>>     'shape' : (30, 15),
    >>>     'eshape' : (2, 2),
    >>>     'origo' : (0, 0),
    >>>     'start' : 0
    >>> }
    >>> coordsQ4, topoQ4 = grid(**gridparams)
    >>> points, triangles = Q4_to_T3(coordsQ4, topoQ4, path='grid')
    >>> plot_triangles_2d(points, np.random.rand(len(points)))
    
    """
    zmin = data.min()
    zmax = data.max()
    fig = go.Figure(data=go.Contour(
        x=points[:, 0],
        y=points[:, 1],
        z=data,
        zmin=zmin, zmax=zmax
    ))
    fig['layout']['xaxis']['showticklabels'] = False
    fig['layout']['yaxis']['scaleanchor'] = 'x'
    fig['layout']['yaxis']['showticklabels'] = False
    fig['layout']['paper_bgcolor']= 'white'
    fig['layout']['plot_bgcolor'] = 'white'
    return fig


def plot_triangles_3d(points, triangles, data=None, 
                      plot_edges=True, edges=None) -> go.Figure:
    """
    Plots a triangulation with attached field data in 3d.
    
    Parameters
    ----------
    points: numpy.ndarray
        2d float array of points.
    data: numpy.ndarray
        1d float array of scalar data over the points.
    plot_edges: bool, Optional
        If True, plots the edges of the mesh. Default is False. 
    edges: numpy.ndarray, Optional
        The edges to plot, only if `plot_edges` is `True`.
    Returns
    -------
    figure: :class:`plotly.graph_objects.Figure`
        The figure object.
    """
    
    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]
    i = triangles[:, 0]
    j = triangles[:, 1]
    k = triangles[:, 2]
    if data is not None:
        fig = go.Figure(data=[
            go.Mesh3d(
                x=x, y=y, z=z,
                i=i, j=j, k=k,
                intensity=data,
                opacity=1,
            )
        ])
    else:
        fig = go.Figure(data=[
            go.Mesh3d(
                x=x, y=y, z=z,
                i=i, j=j, k=k,
                opacity=1,
            )
        ])
    fig.update_layout(
        template="plotly",
        autosize=True,
        # width=720,
        # height=250,
        margin=dict(l=1, r=1, b=1, t=1, pad=0),
        scene=dict(
            aspectmode='data',
            #xaxis = dict(nticks=5, range=[xmin - delta, xmax + delta],),
            #yaxis = dict(nticks=5, range=[ymin - delta, ymax + delta],),
            #zaxis = dict(nticks=5, range=[zmin - delta, zmax + delta],),
        )
    )
    if plot_edges:
        if edges is None:
            edges, _ = unique_topo_data(edges_tri(triangles))
        stack_lines_3d(fig, points, edges)
    return fig
