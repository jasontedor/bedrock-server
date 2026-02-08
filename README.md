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

## Custom add-ons

You can load custom behavior packs and resource packs by mounting a
`/custom-addons` volume. The entrypoint script symlinks each pack directory
into the server's `behavior_packs/` or `resource_packs/` folder at startup,
so vanilla packs are preserved.

### Expected directory structure

```
/path/to/addons/
├── behavior_packs/
│   └── my_behavior_pack/
│       └── manifest.json
└── resource_packs/
    └── my_resource_pack/
        └── manifest.json
```

### Example

```sh
docker run -d \
  -v /path/to/addons:/custom-addons:ro \
  -v /path/to/world:/bedrock-server/worlds \
  ghcr.io/jasontedor/bedrock-server:latest
```

### Activating packs in your world

After mounting your packs, activate them by editing the JSON files inside your
world directory:

- `worlds/<world-name>/world_behavior_packs.json`
- `worlds/<world-name>/world_resource_packs.json`

Each file is a JSON array of objects with `pack_id` and `version` fields
matching the values in your pack's `manifest.json`.
