from parse import parse
import unittest


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('soup_sample/wiki/Stone_Age', [13, 10, 12, 40]),
            ('soup_sample/wiki/Brain', [19, 5, 25, 11]),
            ('soup_sample/wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('soup_sample/wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('soup_sample/wiki/Spectrogram', [1, 2, 4, 7]),)
        for path, expected in test_cases:
            with self.subTest(path = path, expected = expected):
                self.assertEqual(parse(path), expected)

if __name__ == '__main__':
    print(parse('/home/ivan/PYTHON/PYTHON_COURSE/Creating_Web_services_in_Python/WEEK_2_Beautiful_Soup_и_работа_с_API/praktichieskoie-zadaniie-po-beautiful-soup/soup_sample/wiki/Spectrogram'))
    # correct = {
    #     'Stone_Age': [13, 10, 12, 40],
    #     'Brain': [19, 5, 25, 11],
    #     'Artificial_intelligence': [8, 19, 13, 198],
    #     'Python_(programming_language)': [2, 5, 17, 41],
    # }
    # start = 'Stone_Age'
    # end = 'Python_(programming_language)'
    # path = './wiki/'
    #
    # print('parse result:', parse(start, end, path))
    # print('correct result', correct)
