import os


class GlobalConfig(object):
    PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT_DIR, os.path.join("screenshots"))

