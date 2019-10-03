# huz 

\[hʌts]

a tool to track your tracks.

## usage

### init

(better to create a python 3.7.1 venv for huz)

```
# get huz 
git clone https://github.com/vjyq/huz.git

# install py requirements
cd huz
pip install -r requirements.txt

# install db
brew install postgresql
createuser vjyq with superuser
createdb huz

# install audio solution
brew install ffmpeg
```

### setup your track db

1. put your track(s) in one folder [^1]
2. update HUZ_SRC_PATH in `./settings.py` with the folder path
3. (in venv) run `bash init.sh`

once done, run the following cmd to find your db. enjoy.

```
psql -h 127.0.0.1 huz vjyq
```

[^1] here i use a clip of 'A-1 \[Rei I]' by 鷺巣詩郎 as the sample track. if any copywriting issues, i would appreciate it if you could contact me.  

## TODO
- [ ] sample release in ./src
 
## author

yuqing.ji@outlook.com
