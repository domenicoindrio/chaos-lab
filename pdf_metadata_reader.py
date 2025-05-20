import argparse
from PyPDF2 import PdfReader
# Simple pdf metadata reader (and printer)


def read_pdf_metadata(file_path):
    try:
        reader = PdfReader(file_path)
        meta = reader.metadata

        if meta:
            print("-" * 15)
            print("Metadata found:")
            print("-" * 15)
            
        for key, value in meta.items():
            if key:
                print(f"{key:<18} {str(value or 'N/A'):<20}")
        print(f"{'/PDF Version':<18} {reader.pdf_header:<20}")
        print("-" * 15)
    except FileNotFoundError:
        print(f"[!] File not found")
    except Exception as e:
        print(f"[!] Something went wrong: {e}")


def parser():
    parser = argparse.ArgumentParser(description="PDF Metadata reader")
    parser.add_argument("file", type=str, help="PDF File")
    return parser.parse_args()

def main():
    args = parser()
    read_pdf_metadata(args.file)

if __name__ == "__main__":
    main()