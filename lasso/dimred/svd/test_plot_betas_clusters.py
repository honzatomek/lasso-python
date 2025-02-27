import hashlib
from unittest import TestCase

import numpy as np
from lasso.dimred.svd.plot_beta_clusters import plot_clusters_js


def hash_str(data: str) -> str:
    """hashes a string"""

    hasher1 = hashlib.sha256()
    hasher1.update(data.encode("utf-8"))
    return hasher1.hexdigest()


class TestBetaViz(TestCase):
    def test_plot_clusters_js(self):
        """Veryfies correct output .html file"""

        betas = [np.array([[1, 1, 1], [1, 2, 3]])]
        ids = np.array([["sample0", "sample1"]])

        html_page_str = plot_clusters_js(
            betas, ids, "", mark_timestamp=False, filename="testpage", write=False, show_res=False
        )

        self.assertIsInstance(html_page_str, str)
        if isinstance(html_page_str, str):
            html_page_hash = hash_str(html_page_str)

            desired_hash = "53f32e658079dfe8b9f24d7b8ff05a1d253abab77185203e408bfd942c837eeb"
            self.assertEqual(html_page_hash, desired_hash)
