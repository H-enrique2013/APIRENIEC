FROM python:3.10.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    openjdk-17-jdk \
    procps && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3.3.6
ENV SPARK_HOME=/opt/spark
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$JAVA_HOME/bin:$SPARK_HOME/bin:$HADOOP_HOME/bin

RUN curl -fSL https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz -o spark.tgz && \
    tar -xzf spark.tgz -C /opt/ && \
    mv /opt/spark-$SPARK_VERSION-bin-hadoop3 $SPARK_HOME && \
    rm spark.tgz

RUN curl -fSL https://downloads.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz -o hadoop.tar.gz && \
    tar -xzf hadoop.tar.gz -C /opt/ && \
    mv /opt/hadoop-$HADOOP_VERSION /opt/hadoop && \
    rm hadoop.tar.gz

RUN chmod +x $SPARK_HOME/bin/* && chmod +x $HADOOP_HOME/bin/*

RUN pip install --upgrade pip
RUN pip install --no-cache-dir gunicorn

RUN useradd -ms /bin/sh appuser

WORKDIR /app

COPY . .
COPY requirements.txt .

RUN pip install --no-cache-dir --timeout=120 -r requirements.txt

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["bash", "/app/start.sh"]