import unittest

from classification.preprocessing import Preprocessing


class TestPreprocessing(unittest.TestCase):

    preprocessing = Preprocessing()
    test_phrase = "'You have probably never heard of Professor Moriarty?' said he."

    def test_tokenize_phrase(self):
        expected_tokenized = ["'You", "have", "probably", "never", "heard",
                                "of", "Professor", "Moriarty", "?", "'", "said", "he", "."]
        actual_tokenized = self.preprocessing.tokenize(self.test_phrase)

        self.assertEqual(actual_tokenized, expected_tokenized)

    def test_only_lowercased_letters_phrase(self):
        expected_phrase = ["you", "have", "probably", "never", "heard", "of", "professor",
                            "moriarty", "said", "he"]
        actual_phrase = self.preprocessing.only_lowercased_letters(self.test_phrase)

        self.assertEqual(actual_phrase, expected_phrase)

    def test_stop_words_removal(self):
        expected_phrase = "probably never heard professor moriarty said"
        lowercase_phrase = self.preprocessing.only_lowercased_letters(self.test_phrase)
        actual_phrase = self.preprocessing.remove_stopwords(lowercase_phrase)

        self.assertEqual(actual_phrase, expected_phrase)

    def test_lemmas_phrase(self):
        expected_phrase = "probably never hear professor moriarty say"
        tokenized_phrase = self.preprocessing.tokenize(self.test_phrase)

        lowercase_phrase = self.preprocessing.only_lowercased_letters(self.test_phrase)
        important_words = self.preprocessing.remove_stopwords(lowercase_phrase)

        lemmas = self.preprocessing.lemmatize(important_words, tokenized_phrase)

        self.assertEqual(lemmas, expected_phrase)

    def test_fail_if_phrase_is_not_tokenized_correctly(self):
        wrong_tokenized = ["'You have", "probably never heard",
                                "of", "Professor", "Moriarty", "?", "'", "said", "he", "."]
        actual_tokenized = self.preprocessing.tokenize(self.test_phrase)

        self.assertNotEqual(actual_tokenized, wrong_tokenized)

    def test_fail_if_phrase_is_not_lowercased(self):
        wrong_phrase = ["'You", "have", "probably", "never", "heard",
                                "of", "Professor", "Moriarty", "?", "'", "said", "he", "."]
        actual_phrase = self.preprocessing.only_lowercased_letters(self.test_phrase)

        self.assertNotEqual(actual_phrase, wrong_phrase)

    def test_fails_if_stop_words_are_not_removed_correctly(self):
        wrong_phrase = ["'You", "have", "probably", "never", "heard",
                                "of", "Professor", "Moriarty", "?", "'", "said", "he", "."]
        lowercase_phrase = self.preprocessing.only_lowercased_letters(self.test_phrase)
        actual_phrase = self.preprocessing.remove_stopwords(lowercase_phrase)

        self.assertNotEqual(actual_phrase, wrong_phrase)

    def test_fails_if_lemmas_not_done_correctly(self):
        wrong_phrase = ["'You", "have", "probably", "never", "heard",
                                "of", "Professor", "Moriarty", "?", "'", "said", "he", "."]

        tokenized_phrase = self.preprocessing.tokenize(self.test_phrase)

        lowercase_phrase = self.preprocessing.only_lowercased_letters(self.test_phrase)
        important_words = self.preprocessing.remove_stopwords(lowercase_phrase)

        lemmas = self.preprocessing.lemmatize(important_words, tokenized_phrase)

        self.assertNotEqual(lemmas, wrong_phrase)