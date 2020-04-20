# SPDX-License-Identifier: BSD-3-Clause

import argparse
import sys
import logging
from . import xml
from .exception import StylesheetException

logger = logging.getLogger(__name__)

description = """PostgreSQL database changelog"""
usage = """psql-dc <command> [<args>]

The most commonly user psql-dc commands are:
    validate    Validate the database changelog xml file

"""


class Commands(object):

    def __init__(self):
        """Initilize parser for command line"""
        parser = argparse.ArgumentParser(
                description=description,
                usage=usage
        )

        parser.add_argument('command', help='Subcommand to run')
        # parser.add_argument('--log', dest='loglevel', default='INFO')
        args = parser.parse_args(sys.argv[1:2])

        logging.basicConfig(
            level='DEBUG',
            format='%(asctime)s  %(name)-12s %(levelname)-6s: %(message)s'
        )

        if not hasattr(self, args.command):
            logger.error('Unrecognized command "%s"' % args.command)
            parser.print_help()
            sys.exit(1)
        getattr(self, args.command)()

    def validate(self):
        """Validate XML file with RelaxNG"""
        parser = argparse.ArgumentParser(
            description='Validate ChangeLog file with Relax NG')
        parser.add_argument('-f', '--filename', dest='filename',
                            default='dbChangeLog.xml')
        args = parser.parse_args(sys.argv[2:])
        logger.debug("Validate .....")
        try:
            xml.validation(args.filename)
        except StylesheetException as e:
            logger.error(e.message)
        logger.info('Done')
