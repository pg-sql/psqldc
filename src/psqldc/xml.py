# SPDX-License-Identifier: BSD-3-Clause

import os
import logging
from lxml import etree
from .exception import StylesheetException
from . import RNG_FILE

logger = logging.getLogger(__name__)


def validation(xml_file):
    """Palidate the XML with the Relax NG stylesheet"""
    if not os.path.exists(RNG_FILE):
        raise StylesheetException("RNG file not found")
    logger.debug('RND file exists and found')

    FILENAME = os.path.expanduser(xml_file)
    if not os.path.exists(FILENAME):
        raise StylesheetException("ChangeLog file not found")
    logger.debug('ChangeLog found: %s' % FILENAME)

    doc = etree.parse(FILENAME)
    rng = etree.parse(RNG_FILE)
    xml = etree.RelaxNG(rng)
    try:
        xml.assertValid(doc)
        logger.debug('Doc validation OK')
    except etree.DocumentInvalid as e:
        logger.debug('Doc validation FAIL')
        raise StylesheetException(e.args[0])
