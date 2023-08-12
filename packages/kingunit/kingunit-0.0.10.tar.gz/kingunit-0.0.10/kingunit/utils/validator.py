import json


def CheckJson(json_str: str):
    """
    校验json格式
    """
    try:
        json.loads(json_str)
        return True
    except:
        return False