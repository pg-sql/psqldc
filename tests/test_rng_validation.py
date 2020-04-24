# SPDX-License-Identifier: BSD-3-Clause
import pytest
import os
from lxml import etree
from .utils import validate_file


class TestRngValidation:

    def test_empty_xml_files(self):
        """Test and empty XML file"""
        with pytest.raises(etree.XMLSyntaxError):
            validate_file('0000-dc-empty.xml')

    def test_bad_file(self):
        """Test file with bad entry"""
        with pytest.raises(etree.DocumentInvalid) as e:
            validate_file('0001-bad-dc-file.xml')

        assert 'Expecting element databaseChangeLog, got UnknownElement, line 3' in str(e.value)  # noqa

    def test_bad_camel_case(self):
        """databaseChangelog element muste respect camelCase"""
        with pytest.raises(etree.DocumentInvalid) as e:
            validate_file('0002-bad-camel-case.xml')

        assert 'Expecting element databaseChangeLog, got DatabaseChangeLog, line 3' in str(e.value)  # noqa

    def test_good_dc_file(self):
        """Good empty file"""
        validate_file('0003-good-dc-file.xml')
