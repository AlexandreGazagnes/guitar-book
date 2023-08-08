"""
chord class
"""


class Chord:
    """Chord class"""

    EQUIVALENCES = {"C#": "Db", "D#": "Eb", "F#": "Gb", "G#": "Ab", "A#": "Bb"}

    CLEAN = {"E#": "F", "B#": "C", "Fb": "E", "Cb": "B"}

    CORRESPONDING = {"C#": "Db", "D#": "Eb", "F#": "Gb", "G#": "Ab", "A#": "Bb"}

    VALUES = {
        "C": 0,
        "C#": 1,
        "Db": 1,
        "D": 2,
        "D#": 3,
        "E": 4,
        "F": 5,
        "F#": 6,
        "G": 7,
        "G#": 8,
        "A": 9,
        "A#": 10,
        "B": 11,
    }

    def __init__(self, txt, preference=None) -> None:
        """ """

        self.source_txt = txt
        self.current_txt = txt
        self.preference = preference

        self.bass = ""
        self.seventh = ""
        self.fancy = ""
        self.nature = ""
        self.alter = ""
        self.tone = ""

        self.transposed = 0
        # self.value = -1

        self._eval()

    @property
    def REVERSED_VALUES(self):
        return {v: k for k, v in self.VALUES.items()}

    @property
    def REVERSVED_CORRESPONDING(self):
        """ """
        return {v: k for k, v in self.CORRESPONDING.items()}

    @property
    def REVERSED_EQUIVALENCES(self):
        """ """

        return {v: k for k, v in self.EQUIVALENCES.items()}

    def _eval_bass(self):
        """ """

        if "7/4" in self.current_txt:
            self.fancy = "7/4"
            self.current_txt = self.current_txt.split("7/4")[0]
        elif "/" in self.current_txt:
            self.current_txt, self.bass = self.current_txt.split("/")
        # else:
        #     self.bass = ""
        #     self.current_txt = self.current_txt

    def _eval_seventh(self):
        """ """

        if (
            self.current_txt.endswith("maj7")
            or self.current_txt.endswith("7M")
            or self.current_txt.endswith("M7")
        ):
            self.seventh = "maj7"
            self.current_txt = self.current_txt.split("maj7")[0]
            self.current_txt = self.current_txt.split("M7")[0]
            self.current_txt = self.current_txt.split("7M")[0]

        elif self.current_txt.endswith("7"):
            self.seventh = "7"
            self.current_txt = self.current_txt.split("7")[0]
        # else:
        #     self.seventh = ""
        #     self.current_txt = self.current_txt

    def _eval_fancy(self):
        """ """

        li = ["2", "4", "6", "9", "11", "13", "sus4", "sus2", "(aug)", "(dim)", "add9"]

        for cand in li:
            if self.current_txt.endswith(cand):
                self.fancy = cand
                self.current_txt = self.current_txt.split(cand)[0]
                break
        # self.cand = ""
        # self.current_txt = self.current_txt

    def _eval_nature(self):
        """ """

        if self.current_txt.endswith("m"):
            self.nature = "m"
            self.current_txt = self.current_txt.split("m")[0]

    def _eval_alter(self):
        """ """

        if self.current_txt.endswith("#"):
            self.alter = "#"
            self.current_txt = self.current_txt.split("#")[0]
        elif self.current_txt.endswith("b"):
            self.alter = "b"
            self.current_txt = self.current_txt.split("b")[0]

    def _eval_tone(self):
        """ """

        if not len(self.current_txt) == 1:
            raise AttributeError(
                f"Chord must be one letter long after treatment. fonud {self.current_txt}"
            )
        self.tone = self.current_txt[0]

    def _value(self, interval=1):
        """ """

        value = self.current_txt[0]

        self.value = self.VALUES[value]

        if self.alter == "#":
            self.value += interval
        elif self.alter == "b":
            self.value -= interval

    def _eval(self):
        """ """

        self._eval_bass()
        self._eval_seventh()
        self._eval_fancy()
        self._eval_nature()
        self._eval_alter()
        self._eval_tone()
        # self._value()

    def _transpose_tone(self, interval, preference=None):
        pass

    def _transpose_bass(self, interval, preference=None):
        pass

    def transpose(self, interval, preference=None):
        """ """

        # int intervale
        interval = int(interval)

        # sub preference
        preference = preference if preference else self.preference
        if not preference:
            preference = "#" if interval > 0 else "b"

        # zip tone alter A, C#, Bb
        tone_alter = self.tone + self.alter

        # clean tone_alter
        tone_alter = self.CLEAN[tone_alter] if tone_alter in self.CLEAN else tone_alter

        # from tone alter to value
        value = self.VALUES[tone_alter]

        # update value
        value += interval
        value = value % 12

        # from value to tone_alter
        tone_alter = self.REVERSED_VALUES[value]

        # clean tone_alter
        tone_alter = self.CLEAN[tone_alter] if tone_alter in self.CLEAN else tone_alter

        # manage preference
        if preference != "#":
            tone_alter = self.EQUIVALENCES.get(tone_alter, tone_alter)
        else:
            tone_alter = self.REVERSED_EQUIVALENCES.get(tone_alter, tone_alter)

        # unzip tone alter
        self.tone = tone_alter[0]
        self.alter = tone_alter[1] if len(tone_alter) == 2 else ""

        self.transposed += interval

    def __repr__(self) -> str:
        """ """

        repr = f"{self.tone}{self.alter}{self.nature}{self.fancy}{self.seventh}"
        if self.bass:
            repr += f"/{self.bass}"

        return repr
