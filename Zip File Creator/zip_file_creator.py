import os
import zipfile
import lzma


def compress_file(input_file, output_file):
    with open(input_file, "rb") as file:
        data = file.read()
        compressed_data = lzma.compress(data)

    with open(output_file, "wb") as file:
        file.write(compressed_data)


def create_zip(input_files, output_zip):
    with zipfile.ZipFile(output_zip, "w") as zipf:
        for file in input_files:
            if os.path.exists(file):
                compress_file(file, f"{file}.zip")
                zipf.write(f"{file}.zip", os.path.basename(f"{file}.zip"))
                os.remove(f"{file}.zip")
            else:
                print(f"File not found: {file}")


if __name__ == "__main__":
    input_files = [
        r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\Zip File Creator\Files\main.cpp",
        r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\Zip File Creator\Files\Rys1_2.png",
        r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\Zip File Creator\Files\Rys2_2.png"
    ]
    while True:
        file_path = input("Enter file path (or q to finish): ")
        if file_path.lower() == 'q':
            break
        input_files.append(file_path)

    if not input_files:
        print("No files provided.")
    else:
        output_zip = input("Enter the output zip file name: ")
        create_zip(input_files, output_zip)
        print(f"Zip file {output_zip} created")
