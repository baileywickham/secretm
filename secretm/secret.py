import yaml
import string
import random
import os
import urllib.request

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

from cryptography.fernet import Fernet

class Model(dict):
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

class Secrets(Model):
    def __init__(self, datafile="secrets"):
        self.datafile : str = datafile
        self.datafile_enc : str = datafile + '.enc'
        self.fernet_key_enc : str = 'key.enc'

        self.gh_user : str = 'baileywickham'
        self.public_key_file : str = None
        self.private_key_file : str = 'private_key'

        self.secrets = {}

        self.addToGitignore()

        if os.path.exists(datafile):
            self.readDatafile()
        elif os.path.exists(self.datafile_enc):
            self.decryptSymKey()
            self.decryptFile()



    def __getitem__(self, key):
        return self.secrets[key]

    def __setitem__(self, key, value):
        self.secrets[key] = value
        self.save()

    def readDatafile(self):
        with open(self.datafile, 'r') as f:
            self.secrets = yaml.load(f, Loader=yaml.FullLoader)


    def save(self) -> None:
        with open(self.datafile, 'w') as f:
            yaml.dump(self.secrets, f)

    def addToGitignore(self) -> None:
        with open(".gitignore", "a+") as f:
            f.seek(0)
            for line in f:
                if self.path == line.strip("\n"):
                    break
            else:
                f.write(self.datafile + '\n')

    def getPublicKey(self) -> str:
        if not self.public_key_binary:
            if self.public_key_file and self.gh_user:
                raise Exception('only one public key may be provided')

            with urllib.request.urlopen(f'https://github.com/{self.gh_user}.keys') as response:
                self.public_key = RSA.importKey(response.readline()) #.decode('utf8').strip()

        return self.public_key

    def getPrivateKey(self) -> str:
        if not self.private_key:
            self.private_key = RSA.importKey(self.private_key_file)
        return self.private_key

    def decryptFernetKey(self):
        private_key = self.getPrivateKey()
        cipher_rsa = PKCS1_OAEP.new(private_key)
        with open(self.private_key_file, 'rb') as f:
            self.fernet_key = cipher_rsa.decrypt(f)
        return self.Fernet(self.fernet_key)



    def decryptFile(self):
        pass

    def getFernetKey(self):
        if self.fernet_key == None:
            self.fernet_key = Fernet.generate_key()
        return self.fernet_key

    def encryptFernetKey(self) -> None:
        keyfile = 'key.enc'
        fernet_key = self.getFernetKey()
        public_key = self.getPublicKey()
        cipher_rsa = PKCS1_OAEP.new(public_key)
        enc_key = cipher_rsa.encrypt(fernet_key)

        with open(keyfile, 'w') as f:
            f.write(enc_key)

    def encryptFile(self):
        key = self.getFernetKey()
        fernet = Fernet(key)

        fernet.encrypt(self.getData())

        if os.path.exists(self.datafile):
            with open(self.datafile, 'r') as f:
                encrpted = fernet.encrypt(f.read)
            with open(self.datafile + '.enc', 'w') as f:
                f.write(encrpted)

