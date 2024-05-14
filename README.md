# 100knocks_python
Pythonの学習記録です。

参考
- [公式Python チュートリアル](https://docs.python.org/ja/3/tutorial/index.html)
- [Chainer チュートリアル Python 入門](https://tutorials.chainer.org/ja/tutorial.html)
- [どっとインストール　Python入門](https://dotinstall.com/lessons/basic_python_grammar)
  - 無料会員登録が必要。動画で学習できるため、動きが理解しやすい

## 課題

- [Chainer チュートリアル Python 入門](https://tutorials.chainer.org/ja/tutorial.html)
  - ./ChainerTutorial
- [言語処理100本ノック](https://nlp100.github.io/ja/)
  - ./nlp100/

## 環境
Windows11 Home ＋ DockerDesktop ＋ VScode

## GitHubの設定
- トークンの払い出し
  - ユーザ名とパスワードではgit push出来ないため
  - 右上ユーザアイコン -> Settings -> Developer Settings -> Personal access tokens -> tokens (classic) -> Generate new token -> Generate new token (classic)
- メールアドレスの非表示
  - git push時のメールアドレスも非公開にしたいため
  - 右上ユーザアイコン -> Settings -> Emails
    - 以下2つにチェックを入れる
      - Keep my email addresses private
      - Block command line pushes that expose my email
- メールアドレスの設定
  - 右上ユーザアイコン -> Settings -> Emails
    - Primary email address に記載されている【数字】+【アカウント名】@users.noreply.github.comを入力する
    - ![Primary_email_address](./assets/Primary_email_address.png)


```
$ git config --global --list
user.name=【アカウント名】
user.email=【数字】+【アカウント名】@users.noreply.github.com
```

## Push時の注意点
パスワードの入力を求められた際、トークンを入力すること

```
$ git push origin main
Username for 'https://github.com': 【アカウント名】
Password for 'https://XXXXXX@github.com': 【トークン】（パスワードではない）
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (5/5), 358 bytes | 358.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/XXXXXX/100knocks_c.git
   b2c36f0..e375f59  main -> main
$
```

## トラブルシューティング


## その他

### コンテナイメージについて
[マイクロソフト公式のVScode Devcontainer向けイメージ](https://hub.docker.com/_/microsoft-vscode-devcontainers)

### 言語別gitignoreのテンプレート
[GitHubのgitignoreテンプレート](https://github.com/github/gitignore)

### コミットメッセージのサンプル
[はてな匿名ダイアリーより](https://anond.hatelabo.jp/20160725092419)
