"""
Test that team pictures are the right shape
"""

from glob import glob
import matplotlib.pyplot as plt
import os


def test_team_image_sizes(testdata):
    """
    Test that team photos are the right size.
    """
    photo_folder = os.path.join(testdata["assets"], "images", "team")
    target_dims = (200, 200)  # in pixels
    target_ratio = 1  # width to height
    # Group photos should not have "-" in the filenames
    patterns = ["*-*.png", "*-*.jpg"]
    files = [glob(os.path.join(photo_folder, p)) for p in patterns]
    files = [item for sublist in files for item in sublist]
    if not len(files):
        raise Exception("No files found in {}".format(photo_folder))

    failures = []
    for f in files:
        fname = os.path.basename(f)
        img = plt.imread(f)
        if (img.shape[0] > target_dims[0]) or (img.shape[1] > target_dims[1]):
            failures.append(fname)

        if (img.shape[0] / img.shape[1]) != target_ratio:
            failures.append(fname)

    if len(failures):
        failures = sorted(list(set(failures)))
        raise Exception('Test failed on {}'.format(', '.join(failures)))


def test_poster_image_sizes(testdata):
    """
    Test that poster pictures are the right size.
    """
    photo_folder = os.path.join(testdata["assets"], "images", "posters")
    max_target_size = 375  # in pixels

    # Group photos should not have "-" in the filenames
    patterns = ["*.png", "*.jpg"]
    files = [glob(os.path.join(photo_folder, p)) for p in patterns]
    files = [item for sublist in files for item in sublist]
    if not len(files):
        raise Exception("No files found in {}".format(photo_folder))

    failures = []
    for f in files:
        fname = os.path.basename(f)
        img = plt.imread(f)
        if max(img.shape) != max_target_size:
            failures.append(fname)

    if len(failures):
        failures = sorted(list(set(failures)))
        raise Exception('Test failed on {}'.format(', '.join(failures)))


def test_project_image_sizes(testdata):
    """
    Test that project photos are the right size.
    """
    photo_folder = os.path.join(testdata["assets"], "images", "projects")
    target_dims = (400, 400)  # in pixels
    target_ratio = 1  # width to height
    # Non-logo images should not have "-" in the filenames
    patterns = ["*-*.png", "*-*.jpg"]
    files = [glob(os.path.join(photo_folder, p)) for p in patterns]
    files = [item for sublist in files for item in sublist]
    if not len(files):
        raise Exception("No files found in {}".format(photo_folder))

    failures = []
    for f in files:
        fname = os.path.basename(f)
        img = plt.imread(f)
        if (img.shape[0] > target_dims[0]) or (img.shape[1] > target_dims[1]):
            failures.append(fname)

        if (img.shape[0] / img.shape[1]) != target_ratio:
            failures.append(fname)

    if len(failures):
        failures = sorted(list(set(failures)))
        raise Exception('Test failed on {}'.format(', '.join(failures)))
