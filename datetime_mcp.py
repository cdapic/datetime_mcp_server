from mcp.server.fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("datetime_mcp_server")
@mcp.tool()
def get_current_time() -> dict:
    """获取当前时间并格式化为 YYYY-MM-DD HH:MM:SS 格式的字典"""
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return {"time": formatted_time}

# 示例调用
if __name__ == "__main__":
    print("Starting MCP server...")   
    mcp.run(transport="stdio")