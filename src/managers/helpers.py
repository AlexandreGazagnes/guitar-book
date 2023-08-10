class HelperManager:
    """ """

    @classmethod
    def _sample(self, df, n_sample=10):
        """sample random n"""

        logging.debug("__sample")
        if (n_sample == -1) or (not n_sample):
            return df

        df = df.copy()
        df = df.sample(n_sample)

        return df

    @classmethod
    def _finder_url_manager(self, i: str) -> str:
        """helper function to decore a  UrlFinder.song_tab(i) call"""

        try:
            ans = UrlFinder.song.robust_tab(i)
        except Exception as e:
            logging.error(f"{e} => {i} ")
            return ""

        if not ans["status"] == 200:
            ans = (
                f"{ans['status']} - {ans['comment']} - {ans['_query']} - {ans['time']}"
            )
            logging.error(ans)
            return ""

        return ans["url_list"][0]

    @classmethod
    def _prepare(self, df, key):
        """ """

        cols = ["id", key]
        _df = df.loc[:, cols]
        _df.columns = ["id", "key"]
        li = _df.to_dict(orient="records")
        li

        return li

    @classmethod
    def _update_save(self, li, dest_key, fn):
        """ """

        df = Loader.base(website="", nan_url="", top=None)

        for dd in li:
            try:
                k, v = dd["id"], dd["key"]
                df.loc[df["id"] == int(k), dest_key] = v

            except Exception as e:
                raise e

        df.to_csv(fn, index=False)

        return df
