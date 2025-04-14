from server import mcp

import tools.csv_tools
import tools.parquet_tools

# เปิดเซิร์ฟเวอร์เมื่อสคริปต์นี้ถูกเรียกใช้งานโดยตรง
if __name__ == "__main__":
    mcp.run()