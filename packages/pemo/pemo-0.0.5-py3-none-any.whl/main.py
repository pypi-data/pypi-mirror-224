import uuid

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os
import click


# 生成连接客户端
def get_client():
    # 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
    secret_id = 'AKIDvriUDtY2ITY2iIo9IGJDUm5WfPBxd6Oc'
    secret_key = 'HRe0FMPNH4hBWTLEEHQXa4Uq9OZhkeSD'
    region = 'ap-shanghai'
    token = None
    scheme = 'https'
    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
    client = CosS3Client(config)
    return client

def uploadFileAndResp(path):
    filename = os.path.basename(path)
    client = get_client()
    key = str(uuid.uuid1())
    response = client.upload_file(
        Bucket='pytrans-1306270785',
        Key=key,
        LocalFilePath=path,
        EnableMD5=False,
        progress_callback=None
    )
    url = client.get_presigned_download_url(
        Bucket='pytrans-1306270785',
        Key=key,
        Params={
            'response-content-disposition': f'attachment; filename={filename}'  # 下载时保存为指定的文件
            # 除了 response-content-disposition，还支持 response-cache-control、response-content-encoding、response-content-language、
            # response-content-type、response-expires 等请求参数，详见下载对象 API，https://cloud.tencent.com/document/product/436/7753
        },
        Expired=120  # 120秒后过期，过期时间请根据自身场景定义
    )
    print(url)

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def config(name):
    if 'list' == name:
        click.echo(name)



@click.command()
@click.option("--path", help="文件路径")
def upload(path):
    uploadFileAndResp(path)

cli.add_command(upload)
cli.add_command(config)

if __name__=='__main__':
     cli()







