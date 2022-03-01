# PDFを結合する

## How to use
結合したいpdfファイルを一つのフォルダにまとめる。
その後、引数にそのフォルダのパスを指定し、コマンドラインから`pdf_merge.py`を実行すればよい。

つまり
```
cd hoge/pdf_merge

python pdf_merge.py [ファイルパス]
```

結合されたpdfファイルは、フォルダ内に新たに作られるサブフォルダ`result`内に`merged.pdf`として出力される。