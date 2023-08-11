def hello():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n', default=None, help='Your name.')
    args = parser.parse_args()
    print('Hello, World!')
    print(f'Hello, {args.name}!')


def show():
    import sys, os, glob
    from PySide6.QtWidgets import QApplication
    from mtmimgviewer.logic_main_window import Interface_mainWindow
    from mtmtool.io import read_yaml
    from mtmtool.log import create_stream_logger
    import argparse
    # 创建logger
    logger = create_stream_logger("imgviewer")
    # 从命令行读取参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', default="config.yaml", help='Config file path.')
    args = parser.parse_args()
    # 读取配置文件
    if not os.path.exists(args.config):
        logger.error(f"Config file {args.config} not exists.")
        return
    else:
        config = read_yaml(args.config)


    PIC_SIZE = config["Pic"]["Size"]

    if "List" in config["Pic"]:
        pic_lists = [glob.glob(i) for i in config["Pic"]["List"]]
    elif "ListFileName" in config["Pic"]:
        with open(config["Pic"]["ListFileName"], 'r') as f:
            pic_lists = f.readlines()
        pic_lists = [i.rstrip().split(",") for i in pic_lists]
        pic_lists = list(zip(*pic_lists))

    app = QApplication(sys.argv)
    mainWindow = Interface_mainWindow(pic_lists)
    mainWindow.__init_interface__(config["Struct"])
    mainWindow.func_update_pic(config["InitIndex"])  # 设置显示的图片索引
    mainWindow.resize(PIC_SIZE * len(pic_lists) + 50, PIC_SIZE + 50)  # 设置窗口大小
    mainWindow.show()
    app.exec()
