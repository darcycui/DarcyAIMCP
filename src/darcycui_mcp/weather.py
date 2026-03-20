from mcp.server import FastMCP

from darcycui_mcp.https.http_manager import forecast

# from https.http_manager import forecast

# 创建 mcp 对象
mcp = FastMCP("weather")


# 自定义工具(函数)
@mcp.tool("get_forecast")
def get_forecast(city: str) -> str:
    """
    获取天气信息
    :param city: 城市名称
    :return: 天气信息
    """
    # 返回 mock 假数据
    return forecast(city)


# 初始化 MCP 服务
def main():
    try:
        print("darcycui weather MCP Server 运行中...")
        mcp.run(transport="stdio")  # 注意这里本地MCP使用 stdio 协议
        print("darcycui weather MCP Server 结束")
    except Exception as e:
        print(e)
        pass


# 日志记录工具 mcp_logger.py (https://github.com/MarkTechStation/VideoCode/)
# 用来截获mcp client和mcp server之间的通信（仅限于stdio方式） 保存到mcp_io.log日志文件
if __name__ == '__main__':
    main()
