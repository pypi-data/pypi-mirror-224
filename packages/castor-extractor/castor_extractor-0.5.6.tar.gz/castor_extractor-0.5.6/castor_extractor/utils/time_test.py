from datetime import date, datetime

from source.packages.extractor.castor_extractor.utils import at_midnight


def test__at_midnight():
    assert at_midnight(date(1989, 2, 2)) == datetime(1989, 2, 2, 0, 0, 0)
