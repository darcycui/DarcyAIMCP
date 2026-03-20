# 定义泛型类型变量
from pydantic import BaseModel
from typing import TypeVar, Generic, Any

T = TypeVar('T')


class BaseResult(BaseModel, Generic[T]):
    """
    HTTP Response 基类 - 泛型类
    """
    reason: str = "查询成功"
    result: T  # 泛型字段，类型由子类决定
    error_code: int = 0

    @classmethod
    def success(cls, result: Any = None, message: str = "查询成功") -> "BaseResult":
        """
        创建成功响应
        :param result: 返回数据
        :param message: 成功消息
        :return: BaseResult 实例
        """
        return cls(
            reason=message,
            result=result,
            error_code=0
        )

    @classmethod
    def error(cls, error_code: int = 1, message: str = "查询失败") -> "BaseResult":
        """
        创建错误响应
        :param error_code: 错误码
        :param message: 错误消息
        :return: BaseResult 实例
        """
        return cls(
            reason=message,
            result=None,
            error_code=error_code
        )