from src.scraper_util_avliu import example
from src.scraper_util_avliu import util


# Recognize that testing this way cannot test whether requirements are valid,
# e.g. cannot test whether "boto-3" is the correct name to put in the pyproject.toml
example.test()

