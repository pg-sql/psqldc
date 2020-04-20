# SPDX-License-Identifier: BSD-3-Clause
from pkg_resources import get_distribution, DistributionNotFound
import os

try:
    __version__ = get_distribution('postgresql-dc').version
except DistributionNotFound:  # pragma: no cover
    # package is not installed
    __version__ = '0.0.0'

ROOT_FOLDER = os.path.dirname(__file__)
RNG_FILE = os.path.join(ROOT_FOLDER, 'data', 'changelog.rng')
