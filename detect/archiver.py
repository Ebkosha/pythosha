import zipfile
import os
import shutil

a = input('Введите путь к файлу:').split('\\')
b = '\\'.join(a)
print(os.getcwd())
shutil.move(b, os.getcwd())
# b = input('Введите путь к новому архиву:')

# jungle_zip = zipfile.ZipFile(b[1:-1], 'w')
# jungle_zip.write(a[1:-1], compress_type=zipfile.ZIP_DEFLATED)
 
# jungle_zip.close()