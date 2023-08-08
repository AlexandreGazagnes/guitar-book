import pytest

from src.chords import Chords


REPR_LIST = [
    ("C", "C"),
    ("Dm", "Dm"),
    ("E7", "E7"),
    ("F4", "F4"),
    ("A(aug)", "A(aug)"),
    ("Amaj7", "Amaj7"),
    ("Bbm7", "Bbm7"),
    ("C#m7/G", "C#m7/G"),
    ("Dm6/G", "Dm6/G"),
]

TRANSPOSE_SIMPLE_UP = [
    # None
    ("C", 1, "C#", None),
    ("C", 2, "D", None),
    ("C", 3, "D#", None),
    ("C", 4, "E", None),
    ("C", 5, "F", None),
    ("C", 6, "F#", None),
    ("C", 7, "G", None),
    ("C", 8, "G#", None),
    ("C", 9, "A", None),
    ("C", 10, "A#", None),
    ("C", 11, "B", None),
    ("C", 12, "C", None),
    ("C", 13, "C#", None),
    ("C", 14, "D", None),
    # #
    ("C", 1, "C#", "#"),
    ("C", 2, "D", "#"),
    ("C", 3, "D#", "#"),
    ("C", 4, "E", "#"),
    ("C", 5, "F", "#"),
    ("C", 6, "F#", "#"),
    ("C", 7, "G", "#"),
    ("C", 8, "G#", "#"),
    ("C", 9, "A", "#"),
    ("C", 10, "A#", "#"),
    ("C", 11, "B", "#"),
    ("C", 12, "C", "#"),
    ("C", 13, "C#", "#"),
    ("C", 14, "D", "#"),
    # b
    ("C", 1, "Db", "b"),
    ("C", 2, "D", "b"),
    ("C", 3, "Eb", "b"),
    ("C", 4, "E", "b"),
    ("C", 5, "F", "b"),
    ("C", 6, "Gb", "b"),
    ("C", 7, "G", "b"),
    ("C", 8, "Ab", "b"),
    ("C", 9, "A", "b"),
    ("C", 10, "Bb", "b"),
    ("C", 11, "B", "b"),
    ("C", 12, "C", "b"),
    ("C", 13, "Db", "b"),
    ("C", 14, "D", "b"),
]

TRANSPOSE_SIMPLE_DOWN = [
    # None
    ("C", -1, "B", None),
    ("C", -2, "Bb", None),
    ("C", -3, "A", None),
    ("C", -4, "Ab", None),
    ("C", -5, "G", None),
    ("C", -6, "Gb", None),
    ("C", -7, "F", None),
    ("C", -8, "E", None),
    ("C", -9, "Eb", None),
    ("C", -10, "D", None),
    ("C", -11, "Db", None),
    ("C", -12, "C", None),
    ("C", -13, "B", None),
    ("C", -14, "Bb", None),
    # #
    ("C", -1, "B", "#"),
    ("C", -2, "A#", "#"),
    ("C", -3, "A", "#"),
    ("C", -4, "G#", "#"),
    ("C", -5, "G", "#"),
    ("C", -6, "F#", "#"),
    ("C", -7, "F", "#"),
    ("C", -8, "E", "#"),
    ("C", -9, "D#", "#"),
    ("C", -10, "D", "#"),
    ("C", -11, "C#", "#"),
    ("C", -12, "C", "#"),
    ("C", -13, "B", "#"),
    ("C", -14, "A#", "#"),
    # b
    ("C", -1, "B", "b"),
    ("C", -2, "Bb", "b"),
    ("C", -3, "A", "b"),
    ("C", -4, "Ab", "b"),
    ("C", -5, "G", "b"),
    ("C", -6, "Gb", "b"),
    ("C", -7, "F", "b"),
    ("C", -8, "E", "b"),
    ("C", -9, "Eb", "b"),
    ("C", -10, "D", "b"),
    ("C", -11, "Db", "b"),
    ("C", -12, "C", "b"),
    ("C", -13, "B", "b"),
    ("C", -14, "Bb", "b"),
]


TRANSPOSE_COMPLEX_UP = [
    # None
    ("Cm", 1, "C#m", None),
    ("C7", 2, "D7", None),
    ("C(aug)", 3, "D#(aug)", None),
    ("C", 4, "E", None),
    ("Gmaj7", 5, "Cmaj7", None),
    ("Am6", 6, "D#m6", None),
    ("C/G", 2, "D/A", None),
    # ("C", 8, "G#", None),
    # ("C", 9, "A", None),
    # ("C", 10, "A#", None),
    # ("C", 11, "B", None),
    # ("C", 12, "C", None),
    # ("C", 13, "C#", None),
    # ("C", 14, "D", None),
    # # #
    # ("C", 1, "C#", "#"),
    # ("C", 2, "D", "#"),
    # ("C", 3, "D#", "#"),
    # ("C", 4, "E", "#"),
    # ("C", 5, "F", "#"),
    # ("C", 6, "F#", "#"),
    # ("C", 7, "G", "#"),
    # ("C", 8, "G#", "#"),
    # ("C", 9, "A", "#"),
    # ("C", 10, "A#", "#"),
    # ("C", 11, "B", "#"),
    # ("C", 12, "C", "#"),
    # ("C", 13, "C#", "#"),
    # ("C", 14, "D", "#"),
    # # b
    # ("C", 1, "Db", "b"),
    # ("C", 2, "D", "b"),
    # ("C", 3, "Eb", "b"),
    # ("C", 4, "E", "b"),
    # ("C", 5, "F", "b"),
    # ("C", 6, "Gb", "b"),
    # ("C", 7, "G", "b"),
    # ("C", 8, "Ab", "b"),
    # ("C", 9, "A", "b"),
    # ("C", 10, "Bb", "b"),
    # ("C", 11, "B", "b"),
    # ("C", 12, "C", "b"),
    # ("C", 13, "Db", "b"),
    # ("C", 14, "D", "b"),
]


def _test_transpose(origin, trans, dest, preference):
    """ """

    chord = Chords(origin, preference=preference)
    print(chord.__dict__)
    chord.transpose(trans)
    print(chord.__dict__)
    assert chord.__repr__() == dest


class TestChords:
    """ """

    def test_init(self):
        """ """

        chord = Chords("C")

    @pytest.mark.parametrize("base,dest", REPR_LIST)
    def test_repr(self, base, dest):
        """ """

        chord = Chords(base)
        assert chord.__repr__() == dest

    @pytest.mark.parametrize("origin,trans,dest,preference", TRANSPOSE_SIMPLE_UP)
    def test_transpose_simple_up(self, origin, trans, dest, preference):
        """ """

        _test_transpose(origin, trans, dest, preference)

    @pytest.mark.parametrize("origin,trans,dest,preference", TRANSPOSE_SIMPLE_DOWN)
    def test_transpose_simple_down(self, origin, trans, dest, preference):
        """ """

        _test_transpose(origin, trans, dest, preference)

    @pytest.mark.parametrize("origin,trans,dest,preference", TRANSPOSE_COMPLEX_UP)
    def test_transpose_complex_up(self, origin, trans, dest, preference):
        """ """

        _test_transpose(origin, trans, dest, preference)

    # @pytest.mark.parametrize("origin,trans,dest,preference", TRANSPOSE_SIMPLE_DOWN)
    # def test_transpose_simple_down(self, origin, trans, dest, preference):
    #     """ """

    #     _test_transpose(origin, trans, dest, preference)
