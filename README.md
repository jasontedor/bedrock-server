# bedrock-server

The purpose of this repository is to provide a Dockerfile for the [Minecraft
Bedrock Server](https://www.minecraft.net/en-us/download/server/bedrock).
Additionally, it provides workflows to automatically:
 - update the Dockerfile when the released version of the Bedrock Server is
   updated
 - rebuild of the Docker image
 - invoke a webhook that can be used to reload the Docker image

These workflows are chained, so that if the released version of the Bedrock
Server is updated, the Dockerfile will be updated, the Docker image rebuilt,
and the webhook invoked. This ensures that a Bedrock Server running off of
ghcr.io/jasontedor/bedrock-server:latest is always up to date.
