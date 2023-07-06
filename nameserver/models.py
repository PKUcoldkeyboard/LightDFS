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


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_dir = False
        self.end_of_path = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path, is_dir=False):
        node = self.root
        for part in path:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        node.end_of_path = True
        node.is_dir = is_dir

    def check_dir(self, path):
        node = self.root
        for part in path:
            if part not in node.children:
                return False
            node = node.children[part]
        return node.is_dir

    def delete(self, path):
        return self._delete(self.root, path, 0)

    def _delete(self, node, path, depth):
        if not node:
            return None

        # 如果已经到达路径的最后一个部分
        if depth == len(path):
            # 如果该节点是一个路径的结束
            if node.end_of_path:
                node.end_of_path = False
            # 如果该节点没有子节点，那么可以删除该节点
            return node if node.children else None
        # 如果还没有到达路径的最后一个部分
        else:
            part = path[depth]
            node.children[part] = self._delete(
                node.children.get(part), path, depth + 1)
            # 如果该节点不是一个路径的结束，并且没有子节点，那么可以删除该节点
            if not node.end_of_path and not node.children:
                return None
        return node

    def get_children(self, path):
        node = self.root
        for part in path:
            if part not in node.children:
                return []
            node = node.children[part]
        return list(node.children.keys())
