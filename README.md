## Python_Environment_Sharing_-_Setup
プロジェクトの開発環境を他のメンバーと共有したり、別のPCで正確に再現したりするための手順をまとめています。

## Python環境の共有で必要となる情報は2つ
・Pythonのversion
・ライブラリの情報
　－何が入っているのか
  ーライブラリのversion

## Pythonのversionの確認方法
コマンドプロンプトで環境に入り以下を実行
python -V

## ライブラリ情報
コマンドプロンプトで環境に入り以下を実行
pip freeze > requirements.txt
カレントディレクトリにrequirements.txtが生成される。こちらに内容が記載されている。


## ソースコードの紹介
・export_env.py
　pythonのversionとライブラリをテキストファイルで出力するコード
・restore_env.py
　export_env.pyで出力されたデータを読み取りライブラリのインストールを実施するコード
