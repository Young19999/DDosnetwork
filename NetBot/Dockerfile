# 使用轻量级 Python 基础镜像
FROM python:3.12.8-slim

# 设置工作目录
WORKDIR /app

# 复制脚本到容器
COPY netbot.py /app/netbot.py

# 运行脚本
CMD ["python", "netbot.py"]
