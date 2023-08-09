import os
import platform
import sys
from loguru import logger


class ExtraArgument:
    """命令行附加参数映射"""
    # 是否创建Python虚拟环境
    create_venv = False


def init_parser_scaffold(subparsers):
    """定义参数"""
    sub_parser_scaffold = subparsers.add_parser("startproject", help="创建一个具有模板结构的新项目.")
    sub_parser_scaffold.add_argument("project_name", type=str, nargs="?", help="指定新项目名称.")
    sub_parser_scaffold.add_argument(
        "-venv",
        dest="create_venv",
        action="store_true",
        help="在项目中创建虚拟环境，并安装 pitrix.",
    )
    return sub_parser_scaffold


def create_scaffold(project_name):
    """ 创建项目脚手架"""
    if os.path.isdir(project_name):
        logger.warning(
            f"项目文件夹 {project_name} 已存在，请指定新的项目名称."
        )
        return 1
    elif os.path.isfile(project_name):
        logger.warning(
            f"工程名称 {project_name} 与已存在的文件冲突，请指定一个新的文件."
        )
        return 1

    print(f"创建新项目: {project_name}")
    print(f"项目根目录: {os.path.join(os.getcwd(), project_name)}\n")

    def create_folder(path):
        os.makedirs(path)
        msg = f"创建文件夹: {path}"
        print(msg)

    def create_file(path, file_content=""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(file_content)
        msg = f"创建文件:   {path}"
        print(msg)

    create_folder(project_name)

    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template")

    print(f"模版路径:{template_path}")

    for root, dirs, files in os.walk(template_path):
        relative_path = root.replace(template_path, "").lstrip("\\").lstrip("/")
        if dirs:
            print(relative_path)
            for dir_ in dirs:
                create_folder(os.path.join(project_name, relative_path, dir_))
        if files:
            for file in files:
                with open(os.path.join(root, file), encoding="utf-8") as f:
                    create_file(os.path.join(project_name, relative_path, file.rstrip(".template")), f.read())

    if ExtraArgument.create_venv:
        # 创建Python虚拟环境
        os.chdir(project_name)
        print("\n创建虚拟环境")
        os.system("python -m venv .venv")
        print("创建虚拟环境: .venv")

        # 在Python虚拟环境中安装tep
        print("安装 pitrix")
        if platform.system().lower() == 'windows':
            os.chdir(".venv")
            os.chdir("Scripts")
            os.system("pip install pitrix")
        elif platform.system().lower() == 'linux':
            os.chdir(".venv")
            os.chdir("bin")
            os.system("pip install pitrix")
        elif platform.system().lower() == 'darwin':
            os.chdir(".venv")
            os.chdir("bin")
            os.system("pip install pitrix")
        else:
            raise ValueError("暂不支持此平台")



def main_scaffold(args):
    # 项目脚手架处理程序入口
    ExtraArgument.create_venv = args.create_venv
    sys.exit(create_scaffold(args.project_name))


if __name__ == '__main__':
    create_scaffold("demo")
