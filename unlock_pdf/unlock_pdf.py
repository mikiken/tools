import sys, re, pathlib
from pikepdf import Pdf
from getpass import getpass


def unlock_pdf(input_file, output_file):
    path = pathlib.Path(input_file)
    file_name = pathlib.Path(path).name

    # PDFファイル以外をリジェクト
    if path.suffix != ".pdf":
        print("Only PDF file accept.")
        sys.exit()

    print(file_name)
    password = getpass("password:")

    try:
        pdf = Pdf.open(path, password=password)
    except:  # passwordが間違っている場合
        print("failed to open PDF. check password.")
        sys.exit()

    pdf_unlock = Pdf.new()
    pdf_unlock.pages.extend(pdf.pages)

    pdf_unlock.save(output_file)


def main():
    for i in range(1, len(sys.argv)):
        input_file = sys.argv[i].replace("\\", "/")
        output_file = re.sub("\.pdf$", "", input_file) + "_unlocked.pdf"
        unlock_pdf(input_file, output_file)


if __name__ == "__main__":
    main()
