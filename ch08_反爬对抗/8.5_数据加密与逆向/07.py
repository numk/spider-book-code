# 对应：第8章 反爬对抗
# 小节：8.5 数据加密与逆向
# 条目：8.5.2 常见加密算法
# 清单：07
# 说明：摘自书稿示例，未改写。

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt(data: str, key: bytes) -> str:
    """AES CBC 模式加密，返回 Base64 字符串"""
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    # 将 IV 和密文拼接后做 Base64 编码（这是很多网站的常见做法）
    return base64.b64encode(iv + encrypted).decode('utf-8')

def aes_decrypt(encrypted_b64: str, key: bytes) -> str:
    """AES CBC 模式解密"""
    raw = base64.b64decode(encrypted_b64)
    iv = raw[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size)
    return decrypted.decode('utf-8')

# 演示
key = b'1234567890abcdef'  # 16 字节密钥（从 JS 中提取）
plaintext = '{"user_id": 12345, "timestamp": 1704067200}'

encrypted = aes_encrypt(plaintext, key)
print(f"加密结果：{encrypted}")

decrypted = aes_decrypt(encrypted, key)
print(f"解密结果：{decrypted}")
