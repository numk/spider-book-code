# 对应：第8章 反爬对抗
# 小节：8.5 数据加密与逆向
# 条目：8.5.2 常见加密算法
# 清单：09
# 说明：摘自书稿示例，未改写。

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

# 从 JS 代码中提取到的公钥（PEM 格式）
teaching_key = RSA.generate(2048)
public_key_pem = teaching_key.public_key().export_key().decode("ascii")

def rsa_encrypt(data: str, public_key_pem: str) -> str:
    """RSA 加密，返回 Base64 编码的密文"""
    key = RSA.import_key(public_key_pem)
    cipher = PKCS1_v1_5.new(key)
    encrypted = cipher.encrypt(data.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

# 使用示例
password = 'my_password_123'
encrypted_password = rsa_encrypt(password, public_key_pem)
print(f"加密后的密码：{encrypted_password}")
