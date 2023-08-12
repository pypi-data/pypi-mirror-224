import abc
from enum import Enum


class CommonOSS(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def upload(self, path, oss):
        pass

    @abc.abstractmethod
    def config(self):
        pass


class OSSType(Enum):
    TENCENT = "tencent"
    ALI = "ali"


if __name__ == '__main__':
    pass
