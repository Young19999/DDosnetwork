# 使用轻量级 Python 基础镜像
FROM python:3.12.8-slim

# 设置工作目录
WORKDIR /app

# 安装必要的工具和依赖
RUN apt-get update && \
    apt-get install -y \
    hping3 \
    httperf \
    slowhttptest \
    && rm -rf /var/lib/apt/lists/*

# 复制脚本到容器
COPY netbot.py /app/netbot.py

# 运行脚本
# CMD ["python3", "netbot.py"]
# CMD ["/bin/bash"]
CMD ["/bin/bash", "-c", "python3 netbot.py"]
