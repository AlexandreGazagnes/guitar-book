"""
manage class html
"""

import unicodedata
from bs4 import BeautifulSoup

classes_to_find = ["pLgnInstrumentale", "pLgnVide", "pLgn", "pLgnSmpl"]


class ManageClass:
    """ """

    @classmethod
    def no_class(cls, item):
        return ""

    @classmethod
    def pLgnInstrumentale(cls, item):
        return ""

    @classmethod
    def pLgnVide(cls, item):
        return ""

    @classmethod
    def pLgn(cls, item):
        span_elements = item.find_all("span", {"data-accord": True})
        for span in span_elements:
            span.string = "[" + span["data-accord"] + "]"

        return unicodedata.normalize("NFKD", item.text)

    @classmethod
    def pLgnSmpl(cls, item):
        return unicodedata.normalize("NFKD", item.text)

    @classmethod
    def _all(cls, item, class_name, verbose=0):
        """ """

        # pLgnInstrumentale
        if class_name == "pLgnInstrumentale":
            if verbose:
                print("pLgnInstrumentale")
            return cls.pLgnInstrumentale(item)

        # pLgnVide
        if class_name == "pLgnVide":
            if verbose:
                print("pLgnVide")
            return cls.pLgnVide(item)

        # pLgn
        if class_name == "pLgn":
            if verbose:
                print("pLgn")
            return cls.pLgn(item)

        # pLgnSmpl
        if class_name == "pLgnSmpl":
            if verbose:
                print("pLgnSmpl")
            return cls.pLgnSmpl(item)

    @classmethod
    def transform(
        cls,
        results,
        classes_to_find: list = ["pLgnInstrumentale", "pLgnVide", "pLgn", "pLgnSmpl"],
        limit: int = 100,
        verbose: int = 1,
    ) -> list:
        """manage the part of the page to get the text"""

        txt_list = []

        if not results:
            raise AttributeError(f"results is empty : {results}")

        div_list = results.find_all("div", class_=classes_to_find)

        for i, div in enumerate(div_list):
            class_name = div.get("class")

            # no class name
            if not class_name:
                if verbose:
                    print("No class name found")
                raise AttributeError("No class name found")

            # expected list
            if not isinstance(class_name, list):
                raise AttributeError("class_name must be a list")

            # class name
            class_name = class_name[0]
            if verbose:
                print(class_name)

            # manage class item
            txt_list.append(cls._all(div, class_name, verbose=verbose))

            # break
            if i >= limit:
                if verbose:
                    print("limit")
                return txt_list

            # return
            if verbose:
                print(i)

        return txt_list

    @classmethod
    def render(
        cls,
        soup,
        classes_to_find=[
            "pLgnInstrumentale",
            "pLgnVide",
            "pLgn",
            "pLgnSmpl",
        ],
        limit=200,
        verbose=0,
    ):
        id_part = "divPartition"
        results = soup.find(id=id_part)

        if not results:
            raise AttributeError(f"results is empty f{results}")

        txt_list = cls.transform(
            results=results,
            classes_to_find=classes_to_find,
            limit=limit,
            verbose=verbose,
        )

        txt_list = [i.strip() for i in txt_list]
        txt = "\n".join(txt_list)
        txt = txt.replace("\n\n", "\n")

        return txt

    @classmethod
    def from_file(
        cls,
        html_file,
        classes_to_find=[
            "pLgnInstrumentale",
            "pLgnVide",
            "pLgn",
            "pLgnSmpl",
        ],
        limit=200,
        verbose=0,
    ):
        with open(html_file, "r") as f:
            html = f.read()

        if len(html) < 100:
            raise AttributeError(f"html file empty {html}")

        msg = "Le titulaire des droits de reproduction graphique"
        if msg in html:
            raise AttributeError("Chanson retirée")

        soup = BeautifulSoup(html, "html.parser")

        txt = cls.render(
            soup,
            classes_to_find=classes_to_find,
            limit=limit,
            verbose=verbose,
        )
        return txt
