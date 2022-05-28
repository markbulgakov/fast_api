import unittest

from app.global_vars import KEYWORDS
from app.tests.global_test_vars import TEST_TEXTS_OCCURRENCES
from app.utils import count_occurrences


class TestUtilsUnittests(unittest.TestCase):
    """ Unittests for utils functions """

    def test_count_occurrences__validate_return_value_type(self):
        """ Validate, that count_occurrences returns dictionary """
        for text, _ in TEST_TEXTS_OCCURRENCES:  # TODO: use @pytest.mark.parametrize instead of loop
            # Validate that result is a dictionary
            self.assertTrue(isinstance(count_occurrences(text=text), dict))

    def test_count_occurrences__validate_return_value(self):
        """ Validate, count_occurrences return value """
        for text, expected_occurrences in TEST_TEXTS_OCCURRENCES:  # TODO: use @pytest.mark.parametrize instead of loop
            occurrences = count_occurrences(text=text)
            # Validate result and expectation values
            self.assertEqual(occurrences, expected_occurrences)

            # Validate, that only exact keywords appear in the result
            for keyword in occurrences:
                self.assertTrue(keyword in KEYWORDS)
