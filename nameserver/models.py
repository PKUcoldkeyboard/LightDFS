# 定义leveldb中存储的对象

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User username={self.username} password={self.password}>'


class File(object):
    def __init__(self, absolute_path, size, is_dir, ctime, mtime):
        self.absolute_path = absolute_path
        self.size = size
        self.is_dir = is_dir
        self.ctime = ctime
        self.mtime = mtime

    def __repr__(self):
        return f'<File absolute_path={self.absolute_path} size={self.size} is_dir={self.is_dir} ctime={self.ctime} mtime={self.mtime}>'


class DataServer(object):
    def __init__(self, did, host, port):
        self.did = did
        self.host = host
        self.port = port

    def __repr__(self):
        return f'<DataServer did={self.did} host={self.host} port={self.port}>'
