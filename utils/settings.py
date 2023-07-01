# LightDFS settings for the project

DFS_SETTINGS = {
    "NAMESERVER": {
        "HOST": "localhost",
        "PORT": 9000,
        "DATA_DIR": "/tmp/lightdfs/nameserver",
    },
    "DATASERVER": {
        "HOST": "localhost",
        "PORT": 10070,
        "DATA_DIR": "/tmp/lightdfs/dataserver",
    },
    "CLIENT": {
        "HOST": "localhost",
        "PORT": 9090,
        "DATA_DIR": "/tmp/lightdfs/client",
    },
    "LOG_CONFIG": {
        "LOG_DIR": "/tmp/lightdfs/logs",
        "LOG_LEVEL": "INFO",
    },
    "ROOT": "/",
}
