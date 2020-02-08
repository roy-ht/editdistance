# -*- coding: utf-8 -*-

import unicodedata
import unittest

from hypothesis import given, strategies as st

from textdistance import Levenshtein


REFERENCE = Levenshtein().distance  # as a test oracle


MIN_LENGTH = 0
MAX_LENGTH = 16


class TestEditDistance(unittest.TestCase):
    @given(
        str0=st.text(
            alphabet=st.characters(
                min_codepoint=0,
                max_codepoint=127),
            min_size=MIN_LENGTH,
            max_size=MAX_LENGTH),
        str1=st.text(
            alphabet=st.characters(
                min_codepoint=0,
                max_codepoint=127),
            min_size=MIN_LENGTH,
            max_size=MAX_LENGTH))
    def test_ascii_codes(self, str0, str1):
        norm_str0 = unicodedata.normalize('NFKC', str0)
        norm_str1 = unicodedata.normalize('NFKC', str1)

        import editdistance
        assert REFERENCE(norm_str0, norm_str1) == \
            editdistance.eval(norm_str0, norm_str1)

    @given(
        str0=st.text(
            alphabet=st.characters(
                min_codepoint=12354,   # あ
                max_codepoint=12435),  # ん
            min_size=MIN_LENGTH,
            max_size=MAX_LENGTH),
        str1=st.text(
            alphabet=st.characters(
                min_codepoint=12354,
                max_codepoint=12435),
            min_size=MIN_LENGTH,
            max_size=MAX_LENGTH))
    def test_japanese_hiraganas(self, str0, str1):
        norm_str0 = unicodedata.normalize('NFKC', str0)
        norm_str1 = unicodedata.normalize('NFKC', str1)

        import editdistance
        assert REFERENCE(norm_str0, norm_str1) == \
            editdistance.eval(norm_str0, norm_str1)

    @given(
        str0=st.text(
            alphabet=st.characters(
                min_codepoint=12450,   # ア
                max_codepoint=12531),  # ン
            min_size=MIN_LENGTH,
            max_size=MAX_LENGTH),
        str1=st.text(
            alphabet=st.characters(
                min_codepoint=12450,
                max_codepoint=12531),
            min_size=MIN_LENGTH,
            max_size=MAX_LENGTH))
    def test_japanese_katakanas(self, str0, str1):
        norm_str0 = unicodedata.normalize('NFKC', str0)
        norm_str1 = unicodedata.normalize('NFKC', str1)

        import editdistance
        assert REFERENCE(norm_str0, norm_str1) == \
            editdistance.eval(norm_str0, norm_str1)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
