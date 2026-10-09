# WORKLOG

## 2026-10-09 — Version detection broke on wiki layout change

**Goal:** Fix `latest-version.py`, which caused the scheduled workflow to commit
`ENV VERSION ` (empty) as "Update version to v" (ab7112d).

**Discoveries:**
- minecraft.wiki's Bedrock Dedicated Server page removed the Bedrock Edition
  download tables. The only `h4#Release_versions` left is under the
  "Minecraft Education" section, so the scraper picked the Education Edition
  table (`MinecraftEducation_LinuxDS_1.26.32.0.zip`). The regex didn't match and
  the script crashed.
- The workflow ran `echo "version=$(python latest-version.py)"`, which hides the
  script's exit code, so the empty version still got committed and tagged as `v`.
- Mojang's official endpoint
  `https://net-secondary.web.minecraft-services.net/api/v1.0/download/links`
  (what minecraft.net's download page uses) returns JSON with a
  `serverBedrockLinux` entry holding the release zip URL.

**Decisions:**
- Switched from scraping the wiki to the official JSON API. It's structured data
  from the source, so wiki edits no longer affect it. Dropped beautifulsoup4.
- Tightened the regex to `/bin-linux/bedrock-server-<digits.dots>.zip`.
- Workflow now checks the version against `^[0-9]+(\.[0-9]+)+$` and fails
  instead of committing a bad value.
- Restored the Dockerfile to `1.26.52.3` (still the latest release).

**Open items:**
- None.
