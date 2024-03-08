import os
import img2pdf
from PIL import Image

pdf_FileName = "./png/output.pdf"  # 出力するPDFの名前
img_Folder = "./png/"              # 画像フォルダ
extension = ".png"                 # 拡張子


def find_max_numbered_file(directory):
    max_number = float("-inf")  # 初期値を負の無限大に設定

    # 指定されたディレクトリ内のファイルのリストを取得
    files = os.listdir(directory)

    for file in files:
        try:
            # ファイル名から数字の部分を抽出して整数に変換
            number = int(os.path.splitext(file)[0])
            max_number = max(max_number, number)
        except ValueError:
            # 数字に変換できない場合は無視
            continue

    return max_number


def main():
    with open(pdf_FileName, "wb") as f:
        # 画像フォルダの中にあるPNGを取得し配列に追加、バイナリ形式でファイルに書き込む
        f.write(
            img2pdf.convert(
                [
                    Image.open(png_Folder + str(j) + extension).filename
                    for j in range(1, find_max_numbered_file(png_Folder) + 1)
                ]
            )
        )


if __name__ == "__main__":
    main()
