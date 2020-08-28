import os.path as op

import pytest


@pytest.fixture(scope="session")
def testdata():
    """
    Load data from dataset into global variables.
    """
    assets_folder = op.abspath(
        op.join(
            op.dirname(__file__),
            op.pardir,
            "assets"
        )
    )
    test_info = {
        "assets": assets_folder
    }
    return test_info
