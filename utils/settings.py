# LightDFS settings for the project
import os

DFS_SETTINGS = {
    "NAMESERVER": {
        "HOST": "localhost",
        "PORT": int(os.getenv("NAMESERVER_PORT", 9000)),
        "DATA_DIR": "/tmp/lightdfs/nameserver",
    },
    "DATASERVER": {
        "HOST": "localhost",
        "PORT": int(os.getenv("DATASERVER_PORT", 10070)),
        "DATA_DIR": "/tmp/lightdfs/dataserver",
    },
    "CLIENT": {
        "HOST": "localhost",
        "PORT": int(os.getenv("CLIENT_PORT", 9070)),
        "DATA_DIR": "/tmp/lightdfs/client",
    },
    "LOG_CONFIG": {
        "LOG_DIR": "/tmp/lightdfs/logs",
        "LOG_LEVEL": "INFO",
        "LOG_TO_CONSOLE": True,
        "LOG_TO_FILE": True,
    },
    "ROOT": "/",
    "JWT_SECRET": "LIGHTDFS",
}
