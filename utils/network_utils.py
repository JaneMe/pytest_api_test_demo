"""
网络连接工具类，用于处理SSL和网络连接问题
"""
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import urllib3
import ssl


class NetworkConfig:
    """网络配置类"""
    
    @staticmethod
    def create_session_with_retry(
        max_retries=3,
        backoff_factor=1,
        timeout=30,
        verify_ssl=True,
        disable_warnings=False
    ):
        """
        创建带有重试机制的requests session
        
        Args:
            max_retries: 最大重试次数
            backoff_factor: 重试间隔倍数
            timeout: 请求超时时间
            verify_ssl: 是否验证SSL证书
            disable_warnings: 是否禁用SSL警告
        """
        session = requests.Session()
        
        # 配置重试策略
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS", "POST", "PUT", "DELETE"]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # SSL配置
        session.verify = verify_ssl
        session.timeout = timeout
        
        # 禁用SSL警告（仅用于测试环境）
        if disable_warnings:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        return session
    
    @staticmethod
    def test_connection(url, session=None):
        """
        测试网络连接
        
        Args:
            url: 测试URL
            session: requests session对象
            
        Returns:
            dict: 连接测试结果
        """
        if session is None:
            session = NetworkConfig.create_session_with_retry()
        
        try:
            response = session.get(url, timeout=10)
            return {
                "success": True,
                "status_code": response.status_code,
                "message": "Connection successful"
            }
        except requests.exceptions.SSLError as e:
            return {
                "success": False,
                "error_type": "SSL_ERROR",
                "message": f"SSL Error: {str(e)}"
            }
        except requests.exceptions.ConnectionError as e:
            return {
                "success": False,
                "error_type": "CONNECTION_ERROR", 
                "message": f"Connection Error: {str(e)}"
            }
        except requests.exceptions.Timeout as e:
            return {
                "success": False,
                "error_type": "TIMEOUT_ERROR",
                "message": f"Timeout Error: {str(e)}"
            }
        except Exception as e:
            return {
                "success": False,
                "error_type": "UNKNOWN_ERROR",
                "message": f"Unknown Error: {str(e)}"
            }


# 预定义的网络配置
NETWORK_CONFIGS = {
    "default": {
        "verify_ssl": True,
        "timeout": 30,
        "max_retries": 3
    },
    "lenient": {
        "verify_ssl": False,
        "timeout": 60,
        "max_retries": 5,
        "disable_warnings": True
    },
    "strict": {
        "verify_ssl": True,
        "timeout": 15,
        "max_retries": 1
    }
}
