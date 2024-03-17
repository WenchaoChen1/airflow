# 基于 Python 3.7 的 Airflow 镜像
FROM apache/airflow:2.2.0-python3.7
USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
           gcc \
           gcc-multilib \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# 将自定义 DAG 文件复制到 Airflow DAG 目录
USER airflow
COPY --chown=airflow:root dag-code /opt/airflow/dags
# 如果有其他依赖，可以在这里安装它们
# 例如：
# RUN pip install <dependency>

# 如果有其他文件需要复制，也可以在这里进行复制

## 设置 Airflow 的环境变量，以允许调试
#ENV AIRFLOW__CORE__LOAD_EXAMPLES=True

# 启动 Airflow 服务
CMD ["airflow", "webserver"]