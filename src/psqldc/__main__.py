# SPDX-License-Identifier: BSD-3-Clause

from psqldc import cli


try:
    cli.Commands()
except Exception:
    pass
