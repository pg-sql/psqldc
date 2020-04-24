# SPDX-License-Identifier: BSD-3-Clause
import pytest
from lxml import etree
from .utils import validate_file


class TestProperties:

    def test_good_property(self):
        """dc file with name and value attribute"""
        validate_file('0010-good-dc-property.xml')

    def test_properties_wo_name(self):
        """Property element must have a name attribute"""
        with pytest.raises(etree.DocumentInvalid) as e:
            validate_file('0010-dc-property-wo-name.xml')

        assert 'Element property failed to validate attributes, line 4' in str(e.value)  # noqa

    def test_properties_typo_name(self):
        """Property element must have a name attribute"""
        with pytest.raises(etree.DocumentInvalid) as e:
            validate_file('0010-dc-property-typo-name.xml')

        assert 'Element property failed to validate attributes, line 4' in str(e.value)  # noqa
