import sys
import zipfile
import os

def zip_directory(directory_path, zip_file_path):
    try:
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip.write(file_path, os.path.relpath(file_path, directory_path))
        print(f'文件夹已成功压缩为：{zip_file_path}')
    except Exception as e:
        print(f'压缩文件夹出错，异常信息：{e}')
        sys.exit()

if __name__ == '__main__':
    zip_directory('../pemo', '../data.zip')