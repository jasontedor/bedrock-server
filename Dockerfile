FROM ubuntu:22.04

ENV VERSION 1.21.132.3

RUN apt-get update \
  && apt-get install -y unzip curl libcurl4 libssl3 \
  && curl -H 'User-Agent:' -L -O https://www.minecraft.net/bedrockdedicatedserver/bin-linux/bedrock-server-${VERSION}.zip \
  && unzip bedrock-server-${VERSION}.zip -d bedrock-server \
  && rm bedrock-server-${VERSION}.zip

RUN chmod +x /bedrock-server/bedrock_server

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /bedrock-server
ENV LD_LIBRARY_PATH=.
ENTRYPOINT [ "/entrypoint.sh" ]
