import hashlib

def hash_face_feature(feature):
    """
    对人脸特征进行哈希处理
    :param feature: 人脸特征
    :return: 哈希后的特征
    """
    # 将特征转换为字节类型
    feature_bytes = bytes(feature)
    # 创建一个 sha256 哈希对象
    hash_object = hashlib.sha256(feature_bytes)
    # 获取哈希值的十六进制表示
    hash_hex = hash_object.hexdigest()
    return hash_hex