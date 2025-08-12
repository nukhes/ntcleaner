# ntcleaner
**ntcleaner** is a lightweight cli tool to clean Windows temporary folders and cache.

## Features
- Clears Google Chrome cache  
- Clears Firefox cache (supports multiple profiles)  
- Cleans Windows temp folders (Prefetch, Temp, etc.)

## Usage
Run the executable with the desired options:
```bash
ntcleaner.exe [-chrome] [-firefox]
```

## Build
To build this binary ensure you are using Windows and have [Python](https://www.python.org/).
```bash
git clone --depth 1 https://github.com/nukhes/ntcleaner.git
cd ntcleaner
build.cmd
```
