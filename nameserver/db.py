import leveldb
import snowflake
import pickle
import bcrypt
import sys
import os
import time
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import User, Group, File, DataServer
from utils.settings import DFS_SETTINGS

nameserver_data_dir = DFS_SETTINGS['NAMESERVER']['DATA_DIR']

# 数据库路径
db_path = f'{nameserver_data_dir}/nameserver.db'

# 创建数据库文件的父目录，如果它不存在的话
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# 初始化数据库
db = leveldb.LevelDB(db_path, create_if_missing=True)


def create_user(uid, gid, username, password, groups):
    # 检查非空
    if uid == None or gid == None or username == None or password == None or groups == None:
        raise ValueError('uid, gid, username, password, groups cannot be None')

    key_prefix = "UID:"
    key = pickle.dumps(f'{key_prefix}{uid}')
    try:
        user = pickle.loads(db.Get(key))
        if user != None:
            raise ValueError(f'User {uid} already exists')
    except KeyError:
        pass

    # 对密码进行加密
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User(uid, gid, username, password, groups)

    db.Put(key, pickle.dumps(user))

    return True


def get_user(uid):
    if uid == None:
        raise ValueError('uid cannot be None')

    key_prefix = "UID:"
    key = pickle.dumps(f'{key_prefix}{uid}')

    try:
        user = pickle.loads(db.Get(key))
    except KeyError:
        return None

    return user


def delete_user(uid):
    if uid == None:
        raise ValueError('uid cannot be None')

    if uid == 0:
        raise ValueError('Cannot delete root user')

    key_prefix = "UID:"
    key = pickle.dumps(f'{key_prefix}{uid}')
    db.Delete(key)


def update_user(uid, gid, username, password, groups):
    key_prefix = "UID:"
    key = pickle.dumps(f'{key_prefix}{uid}')
    user = get_user(uid)

    if user == None:
        raise ValueError(f'User {uid} does not exist')

    if gid != None:
        user.gid = gid

    if username != None:
        user.username = username

    if password != None:
        user.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    if groups != None:
        user.groups = groups

    db.Put(key, pickle.dumps(user))

    return True


# 设置username与uid的映射
def create_username_uid_mapping(uid):
    if uid == None:
        raise ValueError('uid cannot be None')

    # 查询uid是否已经存在
    user = get_user(uid)
    if user == None:
        raise ValueError(f'Uid {uid} does not exist')

    key = pickle.dumps(f'USERNAME:{user.username}')
    db.Put(key, pickle.dumps(uid))


def create_file(name, size, owner, groups, mode, location):
    if name == None or size == None or owner == None or groups == None or mode == None or location == None:
        raise RuntimeError(
            'name, size, owner, groups, mode, location cannot be None')

    if size < 0:
        raise ValueError('size must be greater than 0')
    elif size > 1024 * 1024 * 1024 * 10:
        raise ValueError('size must be less than 10GB')

    if mode != 0 and mode != 1:
        raise ValueError('mode must be 0 or 1')

    if len(groups) == 0:
        raise ValueError('groups cannot be empty')

    if len(location) < 0:
        raise ValueError('location length must be greater than 0')

    if len(name) == 0 or len(name) > 255:
        raise ValueError('filename length must be between 1 and 255')

    fid = snowflake.generate_id()
    if mode == 0:
        permission = '666'
    elif mode == 1:
        permission = '777'

    ctime = time.time()
    mtime = time.time()
    file = File(fid, name, size, owner, groups,
                permission, ctime, mtime, location)
    key = pickle.dumps(f'FID:{fid}')
    db.Put(key, pickle.dumps(file))


def delete_file(fid):
    if fid == None:
        raise ValueError('fid cannot be None')

    key = pickle.dumps(f'FID:{fid}')
    db.Delete(key)


def get_file(fid):
    if fid == None:
        raise ValueError('fid cannot be None')

    key = pickle.dumps(f'FID:{fid}')
    try:
        file = pickle.loads(db.Get(key))
    except KeyError:
        return None
    return file


def update_file(fid, name, size, owner, groups, permission, ctime, mtime, location):
    if fid == None:
        raise ValueError('fid cannot be None')

    key = pickle.dumps(f'FID:{fid}')
    file = get_file(fid)

    if file == None:
        raise ValueError(f'File {fid} does not exist')

    if name != None and 0 < len(name) <= 255:
        file.name = name

    if size != None and 0 < size <= 1024 * 1024 * 1024 * 10:
        file.size = size

    if owner != None:
        file.owner = owner

    if groups != None and len(groups) > 0:
        file.groups = groups

    if permission != None and len(permission) != 3:
        file.permission = permission

    if ctime != None and ctime > 0:
        file.ctime = ctime

    if mtime != None and mtime > 0:
        file.mtime = mtime

    if location > 0:
        file.location = location

    db.Put(key, pickle.dumps(file))

    return True


def get_data_server(did):
    if did == None:
        raise ValueError('did cannot be None')

    key = pickle.dumps(f'DID:{did}')
    try:
        server = pickle.loads(db.Get(key))
    except KeyError:
        return None
    return server

# 上线数据服务器时，需要将数据服务器的信息写入到数据库中


def create_data_server(did, ip, port):
    if did == None or ip == None or port == None:
        raise ValueError('name, ip, port cannot be None')

    if did < 0:
        raise ValueError('did must be greater than 0')

    # 必须匹配localhost或者ip地址
    regex = re.compile(r'^(localhost|[0-9]+(?:\.[0-9]+){3})$')
    if not regex.match(ip):
        raise ValueError('ip must be localhost or ip address')

    if port < 0 or port > 65535:
        raise ValueError('port must be between 0 and 65535')

    server = get_data_server(did)
    if server != None:
        raise ValueError(f'Data server {did} already exists')
    else:
        server = DataServer(did, ip, port)
        key = pickle.dumps(f'DID:{did}')
        db.Put(key, pickle.dumps(server))


# 系统初始化时，创建root用户
if not get_user(0):
    create_user(0, 0, 'root', 'root', [0])
    create_username_uid_mapping(0)

