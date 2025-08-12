import os
import shutil
import glob

def rmdir(path):
    if not os.path.exists(path):
        return
    for item in glob.glob(os.path.join(path, "*")):
        try:
            if os.path.isfile(item) or os.path.islink(item):
                os.unlink(item)
            elif os.path.isdir(item):
                shutil.rmtree(item, ignore_errors=True)
        except Exception:
            pass

def get_firefox_cache_path():
    base = os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles")
    if not os.path.exists(base):
        return []

    profiles = glob.glob(os.path.join(base, "*.default-release"))
    if not profiles:
        profiles = glob.glob(os.path.join(base, "*.default"))  # fallback

    return [os.path.join(p, "cache2") for p in profiles if os.path.isdir(p)]
