#!/usr/bin/python
# encoding=utf-8

import os
import yaml


class Config:
    """当前项目配置"""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    project_root_dir = ""
    template_dir = os.path.join(root_dir, "templates")
    reports_path = os.path.join(root_dir, "reports")

class GenerateConfig:
    """脚手架创建的项目初始配置"""
    ...

def pitrix_config():
    """
    pitrix配置
    :return:
    """
    config_path = os.path.join(Config.project_root_dir, "resources", "pitrix.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)

def fixture_paths():
    """
    fixture路径，1、项目下的fixtures；2、pitrix 下的fixture；
    :return:
    """
    _fixtures_dir = os.path.join(Config.project_root_dir, "fixtures")
    paths = []
    # 项目下的fixtures
    for root, _, files in os.walk(_fixtures_dir):
        for file in files:
            if file.startswith("fixture_") and file.endswith(".py"):
                full_path = os.path.join(root, file)
                import_path = full_path.replace(_fixtures_dir, "").replace("\\", ".")
                import_path = import_path.replace("/", ".").replace(".py", "")
                paths.append("fixtures" + import_path)
    # pitrix 下的fixture
    paths.append("pitrix.fixture")
    return paths