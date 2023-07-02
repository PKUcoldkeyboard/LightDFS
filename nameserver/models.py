# 定义leveldb中存储的对象

class User(object):
    def __init__(self, uid, gid, username, password, groups):
        self.uid = uid
        self.gid = gid
        self.username = username
        self.password = password
        self.groups = groups

    def __repr__(self):
        return f'<User uid={self.uid} gid={self.gid} username={self.username} password={self.password} groups={self.groups}>'


class Group(object):
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name

    def __repr__(self):
        return f'<Group gid={self.gid} name={self.name}>'


class File(object):
    def __init__(self, fid, name, size, owner, groups, mode, permission, location, ctime, mtime):
        self.fid = fid
        # 带绝对路径的文件名
        self.name = name
        self.size = size
        self.owner = owner
        self.groups = groups
        # mode: 0-文件，1-目录
        self.mode = mode
        self.permission = permission
        # 存储在哪些数据服务器上
        self.location = location
        self.ctime = ctime
        self.mtime = mtime

    def __repr__(self):
        return f'<File fid={self.fid} name={self.name} size={self.size} owner={self.owner} group={self.group} mode={self.mode} permission={self.permission} ctime={self.ctime} mtime={self.mtime}>'


class DataServer(object):
    def __init__(self, did, host, port):
        self.did = did
        self.host = host
        self.port = port

    def __repr__(self):
        return f'<DataServer did={self.did} host={self.host} port={self.port}>'
