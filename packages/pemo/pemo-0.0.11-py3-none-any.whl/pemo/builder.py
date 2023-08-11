from .tencent import TencentOSS
from .commonoss import OSSType
from .configutil import *

oss_instance = {
    OSSType.TENCENT.value: TencentOSS()
}


def build_oss(oss):
    if oss is None:
        oss = default_oss()
    return oss_instance[oss]


def config_info(oss, all):
    if all:
        return read_config()

    if match_config(oss):
        return read_oss_config(oss)

    return "🔥🔥🔥没有发现该类型的配置信息!!!"


def set_config(oss, oss_info):
    config = read_config()
    config[oss] = oss_info
    write_config(config)
    return "🥳🥳🥳🥳配置成功"


def clear_config(oss, all):
    config = read_config()
    if all:
        if OSSType.TENCENT.value in config.keys():
            del config[OSSType.TENCENT.value]
        if OSSType.ALI.value in config.keys():
            del config[OSSType.ALI.value]
        config['default'] = OSSType.TENCENT.value
    else:
        ## 校验是否与默认参数重合
        if config['default'] == oss:
            return "😈😈😈😈️️请更改默认存储后再执行此命令！！"
        ## 校验存储配置是否存在
        if oss not in config.keys():
            return "😈😈😈😈️️无此类型的存储配置"

        del config[oss]

    write_config(config)
    return "🥳🥳🥳🥳️配置成功"


def set_default(oss):
    config = read_config()
    if OSSType.TENCENT.value != oss and oss not in config.keys():
        return "😈😈😈😈️无此类型的存储配置,不能指定默认值"
    config['default'] = oss
    write_config(config)
    return "🥳🥳🥳🥳️配置成功"


if __name__ == '__main__':
    print(type(OSSType.TENCENT))
    pass
