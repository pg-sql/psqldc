# SPDX-License-Identifier: BSD-3-Clause


class StylesheetException(Exception):
    """Exception raised when error on parsing XML file"""

    def __init__(self, message):
        self.message = message
