import uuid

import click

from .builder import *


@click.group()
def cli():
    pass


@click.command()
@click.argument('op', type=click.Choice(['list', 'set', 'clear', 'set-default']))
@click.option("--oss-type", "-t", help="指定存储类型", type=click.Choice(['tencent', 'ali']))
@click.option("--all", "-A", is_flag=True)
def config(op, oss_type, all):
    ## 查询配置所有配置
    if 'list' == op:
        click.echo(config_info(oss_type, all))

    ## 添加配置
    elif 'set' == op:
        if oss_type is None:
            click.echo("🚫🚫请指定存储类型, 使用-t\\--oss-type参数")
            return
        common = build_oss(oss_type)
        res = common.config()
        click.echo(set_config(oss_type, res))

    ## 清空配置
    elif 'clear' == op:
        click.echo(clear_config(oss_type, all))

    elif 'set-default' == op:
        click.echo(set_default(oss_type))


@click.command()
@click.option("--path", "-p", help="文件路径")
@click.option("--oss-type", "-t", help="指定存储类型", type=click.Choice(['tencent', 'ali']))
def upload(path, oss_type):
    common = build_oss(oss_type)
    common.execute(path)


cli.add_command(upload)
cli.add_command(config)

if __name__ == '__main__':
    cli()
