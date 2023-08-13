from src.validators import Validator


class TextCleaner:
    """ """

    @classmethod
    def chords(self, chords, with_validation=True):
        """ """

        Validator.chords(chords)

        chords = chords.strip().lower()
        chords = chords.replace("[", "").replace("]", "")

        if "love" in chords:
            return None
        if "refrain" in chords:
            return None

        return chords

    @classmethod
    def webiste(self, website, with_validation=True, authorise_none=False):
        """ """

        if with_validation:
            Validator.website(website, authorise_none=authorise_none)

        if (not authorise_none) and (not website):
            raise AttributeError(
                f"website should not be empty : {website} authorise_none {authorise_none}"
            )

        website = website if website else ""
        website = website.strip().lower()

        # if not isinstance(website, str):
        #     raise AttributeError(
        #         f"website should be a string not {website} => type {type(website)}"
        #     )

        if "ultimate" in website:
            return "ultimate-guitar"
        if ("boite" in website) or (website == "bac"):
            return "boiteachansons"

        return website
