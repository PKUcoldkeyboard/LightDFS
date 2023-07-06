import logging


def configure_logger(log_to_console=True, log_to_file=False, log_file_path="server.log", level="INFO"):
    # 配置日志记录器
    logger = logging.getLogger(__name__)
    level_dict = {
        'INFO': logging.INFO,
        'DEBUG': logging.DEBUG,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL,
        'NOTSET': logging.NOTSET,
        'FATAL': logging.FATAL,
    }
    logger.setLevel(level_dict[level])

    # 创建日志处理器
    handlers = []

    # 配置控制台处理器
    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level_dict[level])
        handlers.append(console_handler)

    # 配置文件处理器
    if log_to_file:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(level_dict[level])
        handlers.append(file_handler)

    # 配置日志格式
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    for handler in handlers:
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
