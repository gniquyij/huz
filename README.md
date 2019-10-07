# huz 

huz \[hʌts] is an open source listening habit tracking tool designed to record/track/analyze your sound listening.

## Installation

### 1. Get huz
```
git clone https://github.com/vjyq/huz.git
```

### 2. Config your info
1. Put your collections in `./src` [^1], or your could update `HUZ_SRC_PATH` in `./settings.py` with your collection path.
2. In `settings.py`, update `<ip-address>` with your IP address.
3. (in venv/docker container) run `bash init.sh`

[^1] Here i use a clip of 'A-1 \[Rei I]' by 鷺巣詩郎 as the sample track. if any copywriting issues, i would appreciate it if you could contact me.

### 3. Init

2 init ways: venv and Docker. You could move on with either of them.

#### venv 
Dependencies: Python 3.7.1+
```
# Install python requirements
cd huz
pip install -r requirements.txt

# Install database
brew install postgresql   # 11.3
createuser huzer with superuser
createdb huz

# Install audio solution
brew install ffmpeg
```

#### Docker
Dependencies: Docker 2.0.0.3+
```
cd huz
bash docker-compose.sh
```

## Getting started
```
psql -h <ip-address> huz huzer
```

## TODO
- [ ] sample release in ./src
- [ ] add log
- [ ] add ut
- [ ] docker image to hub


## Author
yuqing.ji@outlook.com
