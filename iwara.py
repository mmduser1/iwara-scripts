import os
import shutil

from os.path import isfile

from os.path import isdir

# 動画を保存してあるディレクトリを指定する
basepath = 'F:\\MMD\\動画\\Iwara'

a = os.listdir(basepath)

FileList = []
for filename in os.listdir(basepath):
    if os.path.isfile(basepath + '\\' + filename):
        FileList.append(filename)

# print(FileList)

for i, filename in enumerate(FileList):
    # ファイル名に入っている「 - 」から左にある文字列を投稿者名兼ディレクトリ名とする
    username = FileList[i].split(" - ")[0]
    print(username)
    if username.find('neko .') != -1:
        username = username.replace('neko .', 'neko ．')

    if os.path.isdir(basepath + '\\' + username):
        print('フォルダがあります')
    else:
        print('フォルダがありません')
        os.mkdir(basepath + '\\' + username)
        print('フォルダを作りました')

    if not os.path.isfile(basepath + '\\' + username + '\\' + FileList[i]):
        print("ファイルがありません")
        print("上書きの心配はありません")
        shutil.move(basepath + '\\' + FileList[i], basepath + '\\' + username + '\\' + FileList[i])
        print("移動しました")
    else:
        print("ファイルがあります")
