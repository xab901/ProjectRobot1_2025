import hashlib

def hash_face_feature(feature):
    """
    Hashes a face feature vector using SHA-256.

    :param feature: The face feature vector (list or array of numbers).
    :return: A hexadecimal string representing the hashed feature.
    """
    # Convert the feature vector to a bytes object
    feature_bytes = bytes(feature)

    # Create a SHA-256 hash object
    hash_object = hashlib.sha256(feature_bytes)

    # Get the hexadecimal digest of the hash
    hash_hex = hash_object.hexdigest()

    return hash_hex
