from typing import List

from pydantic import BaseModel

from darcycui_mcp.https.response.BaseResult import BaseResult


class Realtime(BaseModel):
    """实时天气数据"""
    temperature: str  # 温度
    humidity: str  # 湿度
    info: str  # 天气现象
    wid: str  # 天气现象代码
    direct: str  # 风向
    power: str  # 风力
    aqi: str  # 空气质量指数


class FutureWeather(BaseModel):
    """未来天气预报数据"""
    date: str  # 日期
    temperature: str  # 温度范围
    weather: str  # 天气现象
    wid: dict  # 天气现象代码（白天/夜间）
    direct: str  # 风向


class WeatherInfo(BaseModel):
    """天气信息主类"""
    city: str  # 城市名称
    realtime: Realtime  # 实时天气数据
    future: List[FutureWeather]  # 未来天气预报列表

    @classmethod
    def from_json(cls, data: dict) -> "WeatherInfo":
        """
        从 JSON 字典创建 WeatherInfo 实例
        :param data: JSON 字典数据
        :return: WeatherInfo 实例
        """
        return cls(
            city=data.get("city", ""),
            realtime=Realtime(**data.get("realtime", {})),
            future=[FutureWeather(**item) for item in data.get("future", [])]
        )
class WeatherResponse(BaseResult[WeatherInfo]):
    """天气信息响应类"""