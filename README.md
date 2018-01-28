## About
Simple commit search utility for Chromium.

## Installation 
Just install requirements to your environment:
```
pip3 install -r requirements.txt 
```

## Howto
1. Find interesting bug id at https://chromereleases.googleblog.com/
2. If it's in Chromium, run console.py, providing bug id and release, for example:
```
python console.py -b 441275 -r 64.0.3282.119

```
3. If it's in v8, specify v8:
```
python console.py -b 782145 -r master -p v8
```
4. Get commit link, use it only for educational purposes.