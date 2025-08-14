import os
import utils
import glob
from cli import get_args

args = get_args()

# These are default paths, with some specific arguments we can introduce new paths like Chrome cache.
paths = [
    r"C:\Windows\Prefetch",
    r"C:\Windows\SoftwareDistribution",
    r"C:\Windows\Temp",
    os.path.expandvars(r"%userprofile%\AppData\Local\Temp"),
]

if args.chrome: paths.append(os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache"))

if args.firefox:
    paths.extend(utils.get_firefox_cache_path())

for path in paths:
    utils.remove(path)