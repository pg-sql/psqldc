# SPDX-License-Identifier: BSD-3-Clause
from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution('postgresql-dc').version
except DistributionNotFound:  # pragma: no cover
    # package is not installed
    __version__ = '0.0.0'
