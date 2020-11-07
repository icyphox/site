#!/bin/sh

acme_dir="build/.well-known/acme-challenge"
challenge_file="KGSQ6fNidceTVkJatdhhbQpbcuk3Uv-QJU6UnG-BsAM"
mkdir -p "$acme_dir"
touch "$acme_dir/$challenge_file"
echo 'KGSQ6fNidceTVkJatdhhbQpbcuk3Uv-QJU6UnG-BsAM.KutP6lSJGR7mxzITPurdA_OhqcIAPzTLyo0UUCSObro
' > "$acme_dir/$challenge_file"

