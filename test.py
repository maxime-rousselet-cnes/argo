"""
To test the package. To be called by pytest test.py.
"""

from argo import BASE_URL, BASINS, FS

TEST_FOLDER = "/2000/01"


def test_find_argo_files():
    """
    Verifies the NOAA arborescence is reachable.
    """

    remote_root = f"{BASE_URL}/{BASINS[0]}"

    try:

        FS.find(path=remote_root + TEST_FOLDER)

    except OSError:

        assert False
