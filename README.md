# 日期时间MCP工具
本项目是一个基于 `FastMCP` 框架的工具，用于获取当前时间并将其格式化为 `YYYY-MM-DD HH:MM:SS` 格式。该工具以字典形式返回格式化后的时间。

## 功能概述
`get_current_time` 工具可获取当前系统时间，并将其转换为 `YYYY-MM-DD HH:MM:SS` 格式的字符串，最后将其封装在一个字典中返回。

## 安装依赖
本项目依赖 `mcp` 库，你可以使用以下命令安装相关依赖（假设你已经有对应的 `mcp` 库安装方式）。
由于不清楚 `mcp` 库的具体安装方式，你可能需要根据实际情况进行安装。一般来说，如果你有对应的 `pip` 源，可以尝试：

```bash
pip install mcp
```

## 代码结构

### `datetime_mcp.py`
该文件包含了核心的工具实现和 MCP 服务器的启动代码。

```python
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
```

## 使用方法

### 启动服务器
要启动 MCP 服务器，只需运行 `datetime_mcp.py` 文件：

```bash
python datetime_mcp.py
```

服务器启动后，你可以通过标准输入输出（`stdio`）与服务器进行交互。

### 调用工具
当服务器启动后，你可以通过相应的客户端工具调用 `get_current_time` 工具来获取当前时间。