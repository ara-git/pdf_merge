# PDFを結合するコード

from pathlib import Path
import PyPDF2
import os
import sys

# 引数を受け取る（作業ディレクトリ）
path = sys.argv[1]


def pdf_merge(path):
    # ディレクトリの変更
    os.chdir(path)
    # 出力先を設定
    if not os.path.exists("result"):
        os.mkdir("result")
    # フォルダ内のPDFファイル一覧

    pdf_dir = Path(path)
    pdf_files = sorted(pdf_dir.glob("*.pdf"))

    print(pdf_files)
    # pdfをくっつける
    merger = PyPDF2.PdfFileMerger()
    for pdf_file in pdf_files:
        merger.append(str(pdf_file))

    # pdfを出力する。
    merger.write("result/merged.pdf")
    merger.close()


if __name__ == "__main__":
    pdf_merge(path)
