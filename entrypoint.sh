#!/bin/sh

# Symlink custom add-on packs into the server directories.
# If /custom-addons is not mounted, this is a no-op.

for pack_type in behavior_packs resource_packs; do
  src_dir="/custom-addons/${pack_type}"
  dest_dir="/bedrock-server/${pack_type}"
  if [ -d "$src_dir" ]; then
    for pack in "$src_dir"/*/; do
      # skip if the glob matched nothing
      [ -d "$pack" ] || continue
      pack_name="$(basename "$pack")"
      if [ -e "${dest_dir}/${pack_name}" ]; then
        echo "WARNING: skipping custom pack '${pack_name}' — already exists in ${pack_type}" >&2
        continue
      fi
      ln -s "$pack" "${dest_dir}/${pack_name}"
      echo "Linked custom pack '${pack_name}' into ${pack_type}"
    done
  fi
done

exec /bedrock-server/bedrock_server
