from abc import ABC
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os
import uuid
from .configutil import match_config, read_oss_config
from .commonoss import CommonOSS, OSSType


class TencentOSS(CommonOSS, ABC):
    secret_id = 'AKIDvriUDtY2ITY2iIo9IGJDUm5WfPBxd6Oc'
    secret_key = 'HRe0FMPNH4hBWTLEEHQXa4Uq9OZhkeSD'
    region = 'ap-shanghai'
    bucket = 'pytrans-1306270785'

    def upload(self, path):
        ## 判断是否设置执行的oss
        if match_config(OSSType.TENCENT):
            self.refresh_config()

        self.execute(path)

    def config(self):
        bucket1 = input("🪣桶名:")
        region1 = input("🌐区域:")
        secret_id1 = input("🆔secret_id:")
        secret_key1 = input("🔑secret_key:")
        res = {'secret_id': secret_id1, 'secret_key': secret_key1, 'region': region1, 'bucket': bucket1}
        return res


    def refresh_config(self):
        config = read_oss_config(OSSType.TENCENT)
        self.secret_id = config['secret_id']
        self.secret_id = config['secret_id']
        self.secret_id = config['secret_id']
        self.secret_id = config['secret_id']

    # 生成连接客户端
    def get_client(self):
        # 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
        token = None
        scheme = 'https'
        config = CosConfig(Region=self.region, SecretId=self.secret_id, SecretKey=self.secret_key, Token=token,
                           Scheme=scheme)
        client = CosS3Client(config)
        return client

    ## 执行
    def execute(self, path):
        filename = os.path.basename(path)
        client = self.get_client()
        key = str(uuid.uuid1())
        response = client.upload_file(
            Bucket=self.bucket,
            Key=key,
            LocalFilePath=path,
            EnableMD5=False,
            progress_callback=None
        )
        url = client.get_presigned_download_url(
            Bucket=self.bucket,
            Key=key,
            Params={
                'response-content-disposition': f'attachment; filename={filename}'  # 下载时保存为指定的文件
                # 除了 response-content-disposition，还支持 response-cache-control、response-content-encoding、response-content-language、
                # response-content-type、response-expires 等请求参数，详见下载对象 API，https://cloud.tencent.com/document/product/436/7753
            },
            Expired=120  # 120秒后过期，过期时间请根据自身场景定义
        )
        print(url)


if __name__ == '__main__':
    pass
