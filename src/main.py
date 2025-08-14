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
    os.path.expandvars(r"%LOCALAPPDATA%\IconCache.db"),
]

# Arguments
if args.edge: paths.append(os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cache"))
if args.chrome: paths.append(os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache"))
if args.firefox: paths.extend(utils.get_firefox_cache_path())
if args.wupdate:
    paths.append(os.path.expandvars(r"%windir%\SoftwareDistribution\Download"))
    paths.append(os.path.expandvars(r"%windir%\System32\catroot2"))

for path in paths:
    utils.remove(path)