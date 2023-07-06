import leveldb
import pickle
import bcrypt
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import User, File, Trie
from utils.settings import DFS_SETTINGS
from utils.snowflake import getId


nameserver_data_dir = DFS_SETTINGS['NAMESERVER']['DATA_DIR']

# 数据库路径
db_path = f'{nameserver_data_dir}/nameserver.db'

# 创建数据库文件的父目录，如果它不存在的话
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# 初始化数据库
db = leveldb.LevelDB(db_path, create_if_missing=True)


def get_user(username):
    key = pickle.dumps(f'USER:{username}')
    try:
        value = db.Get(key)
        return pickle.loads(value)
    except KeyError:
        return None


def register_user(username, password):
    # 判断用户是否存在
    key = pickle.dumps(f'USER:{username}')
    user = get_user(username)
    if user:
        return False, 'User already exists!'
    # 创建用户
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User(username=username, password=password)
    value = pickle.dumps(user)
    try:
        db.Put(key, value)
    except Exception as e:
        return False, "System Error: Register failed!"
    return True, 'Register successfully!'


def login(username, password):
    user = get_user(username)
    if not user:
        return False, 'User not exists!'
    if not bcrypt.checkpw(password.encode(), user.password):
        return False, 'Password is wrong!'
    return True, 'Login successfully!'


def create_file(absolute_path, size, is_dir, ctime, mtime):
    # 判断文件是否存在
    key = pickle.dumps(f'FILE:{absolute_path}')
    try:
        value = db.Get(key)
        return False, 'File already exists!'
    except KeyError:
        pass
    # 创建文件
    file = File(absolute_path=absolute_path, size=size,
                is_dir=is_dir, ctime=ctime, mtime=mtime)
    value = pickle.dumps(file)
    try:
        trie = pickle.loads(db.Get(pickle.dumps('TRIE')))
        trie.insert(absolute_path.split('/'), is_dir)
        db.Put(key, value)
    except KeyError:
        return False, 'System Error: Trie not exists!'
    except Exception as e:
        return False, "System Error: Create file failed!"
    return True, 'Create file successfully!'


def delete_file(absolute_path):
    key = pickle.dumps(f'FILE:{absolute_path}')
    try:
        db.Delete(key)
        trie = pickle.loads(db.Get(pickle.dumps('TRIE')))
        trie.delete(absolute_path.split('/'))
    except KeyError:
        return False, 'System Error: Trie not exists!'
    except Exception as e:
        return False, "System Error: Delete file failed!"
    return True, 'Delete file successfully!'


def update_file(absolute_path, size, is_dir, mtime):
    key = pickle.dumps(f'FILE:{absolute_path}')
    try:
        value = db.Get(key)
    except KeyError:
        return False, 'File not exists!'
    file = pickle.loads(value)
    if size != None and size > 0 or size < 1024 * 1024 * 10:
        file.size = size
    if is_dir != None and is_dir in [True, False]:
        file.is_dir = is_dir
    file.mtime = mtime
    value = pickle.dumps(file)
    try:
        db.Put(key, value)
    except Exception as e:
        return False, "System Error: Update file failed!"
    return True, 'Update file successfully!'


def get_file(absolute_path):
    key = pickle.dumps(f'FILE:{absolute_path}')
    try:
        value = db.Get(key)
        return pickle.loads(value)
    except KeyError:
        return None


def get_trie():
    key = pickle.dumps('TRIE')
    try:
        value = db.Get(key)
        return pickle.loads(value), 'Get trie successfully!'
    except KeyError:
        return None, 'Trie not exists!'


def update_trie(trie):
    key = pickle.dumps('TRIE')
    try:
        db.Put(key, pickle.dumps(trie))
        return True, 'Update trie successfully!'
    except Exception as e:
        return False, "System Error: Update trie failed!"


key = pickle.dumps('TRIE')
try:
    value = db.Get(key)
except KeyError:
    # 创建TRIE树
    trie = Trie()
    db.Put(key, pickle.dumps(trie))
