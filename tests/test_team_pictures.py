"""
Test that team pictures are the right shape
"""

from glob import glob
import os

import cv2


def test_team_image_sizes(testdata):
    """
    Test that team photos are the right size.
    """
    photo_folder = os.path.join(testdata["assets"], "images", "team")
    target_dims = (200, 200)  # in pixels
    # Group photos should not have "-" in the filenames
    patterns = ["*-*.png", "*-*.jpg"]
    files = [glob(os.path.join(photo_folder, p)) for p in patterns]
    files = [item for sublist in files for item in sublist]
    if not len(files):
        raise Exception("No files found in {}".format(photo_folder))

    failures = []
    for f in files:
        fname = os.path.basename(f)
        img = cv2.imread(f)
        if img.shape[:2] != target_dims:
            failures.append(fname)

    if len(failures):
        failures = sorted(failures)
        raise Exception('Test failed on {}'.format(', '.join(failures)))
