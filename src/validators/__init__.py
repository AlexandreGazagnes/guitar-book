class Validator:
    """ """

    @classmethod
    def tab_website(self, website, authorise_none=False):
        """do validate name of website for df / sql table"""

        # website list
        website_list = [
            "ultimate",
            "ultimate-guitar",
            "ultimateguitar",
            "boiteachansons",
            "boite",
            "bac",
        ]

        # if authorise_none extend website list
        if authorise_none:
            website_list.extend([False, 0, "", None])

        # force None or 0 to be ""
        website = "" if not website else website.lower()

        # validattion
        if website not in website_list:
            raise AttributeError(
                f"website {website} not in website_list {website_list}"
            )

    @classmethod
    def tab_url(self, url, authorise_none=False):
        """do validate url for scraping or requests"""

        # validato
        if ("ultimate" not in url) and ("boite" not in url):
            raise AttributeError(f"website {url} error ")

    @classmethod
    def tab_url_pattern(self, url):
        """do valdiate specific pattern for scraping or tab download"""

        # case boite a chanson
        if "boite" in url:
            condition = "partition"
            if not condition in url:
                raise AttributeError(
                    f"url {url} not has not valid pattern {condition} not in url"
                )

        # case ultimate
        if "ultimate" in url:
            condition = "tabs"
            if not condition in url:
                raise AttributeError(
                    f"url {url} not has not valid pattern {condition} not in url"
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
