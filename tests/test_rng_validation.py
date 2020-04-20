import pytest
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
