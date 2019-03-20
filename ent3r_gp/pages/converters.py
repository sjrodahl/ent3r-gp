class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value


class OneOrTwoDigitMonthConverter:
    regex = '[0-9]{1,2}'

    def to_python(self, value):
        value = int(value)
        if value > 12 or value < 1:
            raise ValueError
        return value

    def to_url(self, value):
        return '%02d' % value