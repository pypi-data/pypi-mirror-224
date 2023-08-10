# from minio import Minio
# import urllib3
# client = Minio(
#     "s4.dextro.link",
#     access_key="TDZvIzVD04gw4vTE",
#     secret_key="jVZbtOgNVCIjOe6tABp2jG2sFM8y98km",
#     http_client=urllib3.ProxyManager(
#         "http://127.0.0.1:9000",
#         timeout=urllib3.Timeout.DEFAULT_TIMEOUT,
#         cert_reqs="CERT_REQUIRED",
#         retries=urllib3.Retry(
#             total=5,
#             backoff_factor=0.2,
#             status_forcelist=[500, 502, 503, 504]
#         )
#     )
# )

# x = client.get_object(
#     "bucket002",
#     "vh-checker-1.0-SNAPSHOT.jar"
# )

# print(str(x.headers['etag']))

# def check_etag(local_file):

import os

http_proxy = os.getenv('http_proxy')
print(http_proxy)
print(http_proxy==None)
