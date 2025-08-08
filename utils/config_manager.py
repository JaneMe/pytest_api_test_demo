"""
配置管理模块
用于管理不同环境的配置文件、请求数据和响应数据
"""
import json
import os
from typing import Dict, Any


class ConfigManager:
    """配置管理器"""
    
    def __init__(self, project_root: str = None):
        """
        初始化配置管理器
        
        Args:
            project_root: 项目根目录路径，如果不提供则自动检测
        """
        if project_root:
            self.project_root = project_root
        else:
            # 自动检测项目根目录（从当前文件位置向上查找）
            current_file = os.path.abspath(__file__)
            # 从utils目录向上一级到项目根目录
            self.project_root = os.path.dirname(os.path.dirname(current_file))
    
    def get_env(self) -> str:
        """获取当前环境名称"""
        return os.getenv('ENV', 'test')
    
    def load_config(self, env: str = None) -> Dict[str, Any]:
        """
        加载指定环境的配置文件
        
        Args:
            env: 环境名称，如果不提供则使用当前环境
            
        Returns:
            配置字典
        """
        if env is None:
            env = self.get_env()
        
        config_file = f'{self.project_root}/config/{env}_config.json'
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"配置文件不存在: {config_file}")
        except json.JSONDecodeError as e:
            raise ValueError(f"配置文件格式错误: {config_file}, 错误: {e}")
    
    def load_request_data(self, env: str = None) -> Dict[str, Any]:
        """
        加载指定环境的请求数据
        
        Args:
            env: 环境名称，如果不提供则使用当前环境
            
        Returns:
            请求数据字典
        """
        if env is None:
            env = self.get_env()
        
        data_file = f'{self.project_root}/data/{env}_request_data.json'
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"请求数据文件不存在: {data_file}")
        except json.JSONDecodeError as e:
            raise ValueError(f"请求数据文件格式错误: {data_file}, 错误: {e}")
    
    def load_response_data(self, env: str = None) -> Dict[str, Any]:
        """
        加载指定环境的响应数据
        
        Args:
            env: 环境名称，如果不提供则使用当前环境
            
        Returns:
            响应数据字典
        """
        if env is None:
            env = self.get_env()
        
        data_file = f'{self.project_root}/data/{env}_response_data.json'
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"响应数据文件不存在: {data_file}")
        except json.JSONDecodeError as e:
            raise ValueError(f"响应数据文件格式错误: {data_file}, 错误: {e}")
    
    def get_all_data(self, env: str = None) -> Dict[str, Dict[str, Any]]:
        """
        一次性加载所有数据（配置、请求数据、响应数据）
        
        Args:
            env: 环境名称，如果不提供则使用当前环境
            
        Returns:
            包含所有数据的字典
        """
        if env is None:
            env = self.get_env()
        
        return {
            'config': self.load_config(env),
            'request_data': self.load_request_data(env),
            'response_data': self.load_response_data(env)
        }
    
    def get_config_path(self, filename: str) -> str:
        """获取配置文件的完整路径"""
        return os.path.join(self.project_root, 'config', filename)
    
    def get_data_path(self, filename: str) -> str:
        """获取数据文件的完整路径"""
        return os.path.join(self.project_root, 'data', filename)


# 创建全局实例
config_manager = ConfigManager() 