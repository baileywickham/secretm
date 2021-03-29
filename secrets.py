import yaml
import os

class Model(dict):
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

class Secrets(Model):
    def __init__(self, path="secrets"):
        self.path = path
        self.f = None
        self.d = {}

        with open(".gitignore", "a+") as f:
            f.seek(0)
            for line in f:
                if path == line.strip("\n"):
                    break
            else:
                f.write(path + '\n')

        if os.path.exists(path):
            self.f = self.open(path)
            self.d = yaml.load(self.f, Loader=yaml.FullLoader)

    def save(self):
        yaml.dump(self.d, self.f)

    def __getitem__(self, key):
        return self.d[key]

    def __setitem__(self, key, value):
        if not self.f:
            self.f = self.open_r(self.path)
        self.d[key] = value
        self.save()


    def open_r(self, path):
        f = open(path, "a+")
        f.seek(0)
        return f
