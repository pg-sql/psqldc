# SPDX-License-Identifier: BSD-3-Clause
import os
from lxml import etree

ROOT_FOLDER = os.path.join(os.path.dirname(__file__), '..')
DC_FOLDER = os.path.join(ROOT_FOLDER, 'tests', 'dcfiles')
RNG_FILE = os.path.join(ROOT_FOLDER, 'src', 'psqldc', 'data', 'changelog.rng')


def validate_file(dc_file=None):
    FILENAME = os.path.join(DC_FOLDER, dc_file)
    if not os.path.exists(FILENAME):
        raise ValueError("dc file must exists")

    if not os.path.exists(RNG_FILE):
        raise ValueError("RNG file not found")

    doc = etree.parse(FILENAME)
    rng = etree.parse(RNG_FILE)
    xml = etree.RelaxNG(rng)
    xml.assertValid(doc)
