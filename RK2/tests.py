import unittest
from main import Language, Library, LanguageLibrary, task_e1, task_e2, task_e3

class TestProgram(unittest.TestCase):
    def setUp(self):
        self.languages = [
            Language(1, 'Python', 'medium'),
            Language(2, 'C++', 'medium'),
            Language(3, 'C', 'easy'),
            Language(4, 'Swift', 'hard'),
            Language(5, 'JavaScript', 'medium'),
            Language(6, 'Java', 'medium'),
            Language(7, 'C#', 'medium'),
        ]

        self.libs = [
            Library(1, 'requests', 2, 100),
            Library(2, 'system', 2, 200),
            Library(3, 'numbers', 6, 250),
            Library(4, 'math', 1, 150),
            Library(5, 'menu', 1, 100),
            Library(6, 'play', 6, 50),
            Library(7, 'reject', 5, 250),
            Library(8, 'formuli', 3, 150),
            Library(9, 'picture', 4, 100),
            Library(10, 'css', 7, 200),
        ]

        self.language_libs = [
            LanguageLibrary(1, 4),
            LanguageLibrary(1, 5),
            LanguageLibrary(2, 1),
            LanguageLibrary(2, 2),
            LanguageLibrary(3, 8),
            LanguageLibrary(4, 9),
            LanguageLibrary(5, 7),
            LanguageLibrary(6, 6),
            LanguageLibrary(6, 3),
            LanguageLibrary(7, 10),
        ]

    def test_task_e1(self):
        expected_result = [('C++', 'medium', 'requests', 100),
                           ('C++', 'medium', 'system', 200),
                           ('Java', 'medium', 'play', 50),
                           ('C#', 'medium', 'css', 200)]
        
        result = task_e1(self.languages, self.libs)
        self.assertEqual(result, expected_result)

    def test_task_e2(self):
        one_to_many = task_e1(self.languages, self.libs)
        expected_result = [('Java', 100.0),
                           ('C++', 75.0),
                           ('C#', 62.5),
                           ('Python', 62.5),
                           ('JavaScript', 62.5),
                           ('C', 50.0),
                           ('Swift', 0.0)]
        
        result = task_e2(self.languages, self.libs, one_to_many)
        self.assertEqual(result, expected_result)

    def test_task_e3(self):
        expected_result = [('math', 'JavaScript'),
                           ('menu', 'JavaScript'),
                           ('play', 'Java'),
                           ('reject', 'JavaScript'),
                           ('css', 'C#')]
        
        result = task_e3(self.languages, self.libs, self.language_libs)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()