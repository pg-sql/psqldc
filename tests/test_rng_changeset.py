import pytest
from lxml import etree
from .utils import validate_file


class TestChangeSet:

    def test_good_changeset(self):
        """Test good changeSet element"""
        validate_file("0015-good-dc-changeset.xml")

    def test_bad_changeset(self):
        """Type on id attribute"""
        with pytest.raises(etree.DocumentInvalid) as e:
            validate_file("0015-bad-dc-changeset.xml")

        assert 'Element changeSet failed to validate attributes, line 4' in str(e.value)  # noqa

    def test_bad_changeset_wo_author(self):
        """missing id attribute attribute"""
        with pytest.raises(etree.DocumentInvalid) as e:
            validate_file("0015-bad-dc-changeset3.xml")

        assert 'Element changeSet failed to validate attributes, line 4' in str(e.value)  # noqa
