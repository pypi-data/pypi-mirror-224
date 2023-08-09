# SPDX-FileCopyrightText: Copyright 2016, Siavash Ameli <sameli@berkeley.edu>
# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileType: SOURCE
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the license found in the LICENSE.txt file in the root directory
# of this source tree.


# ======
# Import
# ======

import numpy
from .._plots._plot_utilities import plt, matplotlib, colors       # noqa: F401

__all__ = ['shifted_colormap']


# ================
# Shifted Colormap
# ================

def shifted_colormap(
        cmap,
        start=0,
        midpoint=0.5,
        stop=1.0,
        name='shiftedcmap'):
    '''
    Function to offset the "center" of a colormap. Useful for data with a
    negative min and positive max and you want the middle of the
    colormap's dynamic range to be at zero

    Input
    -----

     cmap:
        The matplotlib colormap to be altered

     start:
        Offset from lowest point in the colormap's range. Defaults to 0.0
        (no lower ofset). Should be between 0.0 and `midpoint`.

     midpoint:
        The new center of the colormap. Defaults to 0.5 (no shift). Should
        be between 0.0 and 1.0. In general, this should be
        1 - vmax/(vmax + abs(vmin)). For example if your data range from
        -15.0 to +5.0 and you want the center of the colormap at 0.0,
        `midpoint` should be set to  1 - 5/(5 + 15)) or 0.75

     stop:
        Offset from highets point in the colormap's range. Defaults to 1.0
        (no upper ofset). Should be between `midpoint` and 1.0.
    '''

    cdict = {
        'red': [],
        'green': [],
        'blue': [],
        'alpha': []
    }

    # regular index to compute the colors
    reg_index = numpy.linspace(start, stop, 257)

    # shifted index to match the data
    shift_index = numpy.hstack([
        numpy.linspace(0.0, midpoint, 128, endpoint=False),
        numpy.linspace(midpoint, 1.0, 129, endpoint=True)
    ])

    for ri, si in zip(reg_index, shift_index):
        r, g, b, a = cmap(ri)

        cdict['red'].append((si, r, r))
        cdict['green'].append((si, g, g))
        cdict['blue'].append((si, b, b))
        cdict['alpha'].append((si, a, a))

    newcmap = matplotlib.colors.LinearSegmentedColormap(name, cdict)
    # plt.register_cmap(cmap=newcmap)

    return newcmap
