# DateTime MCP Tool

This project is a tool based on the `FastMCP` framework designed to retrieve the current time and format it into the `YYYY-MM-DD HH:MM:SS` format. The tool returns the formatted time in a dictionary structure.

## Function Overview

The `get_current_time` tool fetches the current system time, converts it into a string formatted as `YYYY-MM-DD HH:MM:SS`, and encapsulates it within a dictionary for return.

## Installation Dependencies

This project relies on the `mcp` library. You can use the following command to install the relevant dependencies (assuming you already have the corresponding installation method for the `mcp` library). Since the specific installation method for the `mcp` library is unclear, you may need to install it according to the actual situation. Generally, if you have the corresponding `pip` source, you can try:

```bash
pip install mcp
```

## Code Structure

### `datetime_mcp.py`

This file contains the core tool implementation and the startup code for the MCP server.

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

## Usage

### Start the Server

To start the MCP server, simply run the `datetime_mcp.py` file:

```bash
python datetime_mcp.py
```

After the server starts, you can interact with it through standard input and output (`stdio`).

### Invoke the Tool

Once the server is running, you can use the corresponding client tool to invoke the `get_current_time` tool and retrieve the current time.