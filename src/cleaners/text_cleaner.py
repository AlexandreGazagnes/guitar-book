from src.validators import Validator


class TextCleaner:
    """Text Cleaner

    methods :
        - chords : clean a str chords ie [Am] => Am]
        - tab_website : clean a tab website ie bac => boiteachansons
    """

    @classmethod
    def chords(
        self,
        chords: str,
        with_validation: bool = True,
    ) -> str:
        """from str chords, clean to obtain a proper str chords

        positional arguments:
            - chords: str : the chords to clean ie Am, Gm7, E7

        optional arguments:
            - with_validation: bool : if True, will validate the chords before cleaning it
        """

        # validator
        if with_validation:
            Validator.chords(chords)

        # do clean
        chords = chords.strip().lower()
        chords = chords.replace("[", "").replace("]", "")

        # special case
        if "love" in chords:
            return None
        if "refrain" in chords:
            return None

        return chords

    @classmethod
    def tab_website(
        self,
        website: str,
        with_validation: bool = True,
        authorise_none: bool = False,
    ) -> str:
        """clean the tab website such as ultimate-guitar, boiteachansons, ...

        positional arguments:
            - website: str : the website to clean ie ultimate-guitar, boiteachansons, ...

        optional arguments:
            - with_validation: bool : if True, will validate the website before cleaning it
            - authorise_none: bool : if True, will authorise None as a website
        """

        # validator
        if with_validation:
            Validator.tab_website(website, authorise_none=authorise_none)

        # if not possible none => raise error
        if (not authorise_none) and (not website):
            raise AttributeError(
                f"website should not be empty : {website} authorise_none {authorise_none}"
            )

        # do clean 1st
        website = website if website else ""
        website = website.strip().lower()

        # # ???
        # if not isinstance(website, str):
        #     raise AttributeError(
        #         f"website should be a string not {website} => type {type(website)}"
        #     )

        # do clean 2nd
        if "ultimate" in website:
            return "ultimate-guitar"
        if ("boite" in website) or (website == "bac"):
            return "boiteachansons"

        return website
