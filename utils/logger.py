import logging

def configure_logger(log_to_console=True, log_to_file=False, log_file_path="server.log"):
    # 配置日志记录器
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # 创建日志处理器
    handlers = []

    # 配置控制台处理器
    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        handlers.append(console_handler)

    # 配置文件处理器
    if log_to_file:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.INFO)
        handlers.append(file_handler)

    # 配置日志格式
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    for handler in handlers:
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
