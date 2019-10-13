# huz 

<img src='https://github.com/vjyq/huz/blob/master/huz-logo-v3.png?raw=true'>

huz \[hʌts] is an open source listening habit tracking tool designed to record/track/analyze your listening.

## Installation

### 1. Get huz
```
git clone https://github.com/vjyq/huz.git
```

### 2. Config your info
- Put your collections in `./src`[^1], or your could update `HUZ_SRC_PATH` in `./settings.py` with your collection path.
- In `./settings.py`, update `<ip-address>` with your IP address.

[^1] Here i use a clip of 'A-1 \[Rei I]' by 鷺巣詩郎 as the sample track. If any copywriting issues, i would appreciate it if you could contact me at yuqing.ji@outlook.com.

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

# Init
bash init.sh
```

#### Docker
Dependencies: Docker 2.0.0.3+
```
# Config docker-compose
# In ./docker-compose.yml, update <huz-path> with the absolute path of huz in your local.

# Init
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
