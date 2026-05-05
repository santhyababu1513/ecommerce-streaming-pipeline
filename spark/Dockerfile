FROM apache/spark:3.5.0

WORKDIR /app

USER root
RUN mkdir -p /tmp/.ivy2 && chmod -R 777 /tmp/.ivy2

COPY streaming_job.py .

CMD ["/opt/spark/bin/spark-submit", "--master", "local[*]", "--conf", "spark.jars.ivy=/tmp/.ivy2", "--conf", "spark.hadoop.security.authentication=simple", "--conf", "spark.hadoop.security.authorization=false", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0", "/app/streaming_job.py"]