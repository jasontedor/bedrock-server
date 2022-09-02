FROM ubuntu:18.04

ENV VERSION 1.19.22.01

RUN apt-get update \
  && apt-get install -y unzip curl libcurl4 libssl1.0.0 \
  && curl -L -O https://minecraft.azureedge.net/bin-linux/bedrock-server-${VERSION}.zip \
  && unzip bedrock-server-${VERSION}.zip -d bedrock-server \
  && rm bedrock-server-${VERSION}.zip

RUN chmod +x /bedrock-server/bedrock_server

WORKDIR /bedrock-server
ENV LD_LIBRARY_PATH=.
CMD [ "/bedrock-server/bedrock_server" ]
