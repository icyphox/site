#!/bin/sh
# creates '.well-known/host-meta'

well_known="build/.well-known"
host_meta="host-meta"
mkdir -p "$well_known"
touch "$well_known/$host_meta"

cat << EOF > "$well_known/$host_meta"
<?xml version="1.0" encoding="UTF-8"?>
<XRD xmlns="http://docs.oasis-open.org/ns/xri/xrd-1.0">
  <Link rel="lrdd" type="application/xrd+xml" template="https://toot.icyphox.sh/.well-known/webfinger?resource={uri}"/>
</XRD>
EOF
