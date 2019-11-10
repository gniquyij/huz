# huz 

<img src='https://github.com/vjyq/huz/blob/master/huz-logo-v4.png?raw=true'>

huz \[hʌts] is an open source listening habit tracking tool designed to record/track/analyze your listening.

## Installation

### 1. Get huz
```
git clone https://github.com/vjyq/huz.git
```

### 2. Config your info

- Put your collections in `./src`[^1], or your could update `HUZ_SRC_PATH` in `./settings.py` with your collection path.

[^1] Here i use a clip of 'A-1 \[Rei I]' by 鷺巣詩郎 as the sample track. If any copywriting issues, i would appreciate it if you could contact me at yuqing.ji@outlook.com.

### 3. Init

2 init ways: Docker (recommended) or venv. You could move on with either.

#### Docker

Dependencies: Docker 2.0.0.3+
```
# Config docker-compose
# In ./docker-compose.yml, update <huz-path> with the absolute path of huz in your local.

# Init
cd huz
bash docker-compose.sh
```

#### venv 

Dependencies: Python 3.7.1+

**Install python requirements**
```
cd huz
pip install -r requirements.txt
```
**Install database**
```
brew install postgresql   # 11.3
createuser huzer with superuser
createdb huz
```
update db config `<huz-path>/settings.py`   # \<huz-path> is the absolute path of huz in your local
```
# HUZ_PSQL_HOST = '172.17.0.1'
HUZ_PSQL_HOST = '0.0.0.0'
```

**Install audio solution**
```
brew install ffmpeg
```
**Install frontend**
```
brew install grafana
```
update grafana ini `/usr/local/opt/grafana/share/grafana/conf/defaults.ini`:
```
# provisioning = conf/provisioning
provisioning = <huz-path>/grafana
```
update UI template `<huz-path>/grafana/dashboards/dashboard.yml`
```
# path: /etc/grafana/provisioning/dashboards
path: <huz-path>/grafana/dashboards
```
update data template `<huz-path>/grafana/dashboards/template.json`
```
# url: 172.17.0.1:5432
url: 0.0.0.0:5432
```
```
brew services start grafana
```

**Init**
```
cd ./bin
bash init.sh
```

## Getting started

http://127.0.0.1:3000

or just enter the database:
```
psql -h <your-IP-address> -p 5432 huz huzer
```

## Author
yuqing.ji@outlook.com
