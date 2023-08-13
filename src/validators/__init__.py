class Validator:
    """ """

    @classmethod
    def tab_website(self, website, authorise_none=False):
        """ """

        website_list = [
            "ultimate",
            "ultimate-guitar",
            "ultimateguitar",
            "boiteachansons",
            "boite",
            "bac",
        ]

        if authorise_none:
            website_list.extend([False, 0, "", None])

        website = "" if website is None else website.lower()

        if not website in website_list:
            raise AttributeError(
                f"website {website} not in website_list {website_list}"
            )

    @classmethod
    def chords(self, chords):
        """ """

        if not chords:
            raise AttributeError(
                f"chords should not be empty : {chords} type {type(chords)}"
            )

        if not isinstance(chords, str):
            raise AttributeError(
                f"chords should be a string not {chords} => type {type(chords)}"
            )
