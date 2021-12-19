import pyAesCrypt
import os
import shutil
from pathlib import Path

class AESCrypt:
    def __init__(self, bufferSize=512 * 1024):
        self.bufferSize = bufferSize

    def encrypt(self, path, password, remove_src=True):
        try:
            if os.path.isdir(path):
                for file in os.listdir(path):
                    self.encrypt(os.path.join(path, file), password)
            else:
                pyAesCrypt.encryptFile(
                    str(path), f"{path}.aes", str(password), self.bufferSize)
                if remove_src:
                    os.remove(path)
            return f"{path}.aes"
        except ValueError as e:
            print(e)

    def decrypt(self, path, password, remove_src=True):
        try:
            if os.path.isdir(path):
                for file in os.listdir(path):
                    self.decrypt(os.path.join(path, file), password)
            else:
                pyAesCrypt.decryptFile(str(path), os.path.splitext(path)[
                                       0], str(password), self.bufferSize)
                if remove_src:
                    os.remove(path)
        except ValueError as e:
            print(e)



class FileSystem:
    file_name_index = 0

    def normalize_file_name(self, outdir, filename):
        path = Path(Path.cwd(), outdir, filename)
        if not path.exists():
            self.file_name_index = 0
            return filename
        self.file_name_index = self.file_name_index + 1
        tmp = "{}({}){}".format(path.stem, self.file_name_index, path.suffix)
        return self.normalize_file_name(outdir, tmp)

    def upload(self, file, outdir, password=None):
        path = os.path.join(os.getcwd(), outdir, file.name.replace(" ", "_"))
        if not os.path.exists(os.path.join(os.getcwd(), outdir)):
            print('folder created')
            os.makedirs(os.path.join(os.getcwd(), outdir))
        fs = FileSystemStorage()
        abs_name = fs.save(path, file)
        data = {}
        data['size'] = round(fs.size(abs_name) * 0.000977)
        if password:
            abs_name = AESCrypt().encrypt(abs_name, password)
        splited_path = abs_name.split('/')
        data['name'] = splited_path[-1]
        # data['path'] = abs_name
        data['url'] = "/".join(splited_path[splited_path.index('media'):])
        return data

    def encode(self, path, password):
        return AESCrypt().encrypt(path, password)

    def decode(self, path, password, delet=False):
        AESCrypt().decrypt(path, password, remove_src=delet)
        return os.path.splitext(path)[0]