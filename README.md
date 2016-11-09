# study-python

「The Python Mega Course: Build 10 Python Applications」の復習用リポジトリです。

## OpenCV

[MacOS Sierra(10.12) に Pyenv で Python3 + openCV3 をインストールする](http://qiita.com/masaori/items/0c78fcd58a6c6bf4f655)

```
$ brew update
$ brew install -v cmake
$ brew tap homebrew/science
$ brew install homebrew/science/opencv3 --with-python3 --HEAD
$ ln -s /usr/local/Cellar/opencv3/HEAD-b2fa82f_4/lib/python3.5/site-packages/cv2.cpython-35m-darwin.so ~/.anyenv/envs/pyenv/versions/3.5.2/lib/python3.5/site-packages/
```

## Jupyter Notebook

起動は下記のコマンドで行う

```
$ jupyter notebook
```

ショートカット

* Shift + Enter で実行
* dd で削除

## Virtualenv

```
$ virtualenv virtual
$ source ./virtual/bin/activate
$ pip install ...
$ pip freeze > requirements.txt
```

下記のようにすればまとめてインストールが可能

```
$ pip install -r requirements.txt
```

## SQLite

````
$ sqlite3 database.db 
SQLite version 3.8.10.2 2015-05-20 18:17:19
Enter ".help" for usage hints.
sqlite> select * from data;
1|test@test.com|100
```
