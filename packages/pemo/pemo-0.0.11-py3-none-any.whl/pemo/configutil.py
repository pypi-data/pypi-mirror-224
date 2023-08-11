import json
import os

def read_config():
    cur_dir = os.path.split(os.path.realpath(__file__))[0]
    with open(os.path.join(cur_dir, "resources/config.json"), "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def write_config(config):
    json_str = json.dumps(config)
    cur_dir = os.path.split(os.path.realpath(__file__))[0]
    with open(os.path.join(cur_dir, "resources/config.json"), "w", encoding="utf-8") as f:
        f.write(json_str)


def default_oss():
    config = read_config()
    return config['default']


def read_oss_config(oss):
    config = read_config()
    return config[oss]


def match_config(oss):
    config = read_config()
    if oss in config.keys():
        return True
    return False

if __name__=='__main__':
     print(match_config('tencent'))