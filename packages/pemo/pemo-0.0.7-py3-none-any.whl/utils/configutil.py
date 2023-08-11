import json


def read_config():
    with open('config.json') as f:
        data = json.load(f)

    return data


def write_config(config):
    json_str = json.dumps(config)
    with open("config.json", "w") as f:
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