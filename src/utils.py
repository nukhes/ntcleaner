import os
import shutil
import glob

def remove(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        try:
            os.unlink(path)
        except Exception:
            pass
    elif os.path.isdir(path):
        try:
            shutil.rmtree(path, ignore_errors=True)
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
