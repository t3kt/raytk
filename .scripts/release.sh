#!/bin/bash

version=$(cat ./\#jekyll-theme-hydejack/package.json | jq '.version' -r)

rm -rf   _zip/hydejack-pro-$version
mkdir -p _zip/hydejack-pro-$version
cd       _zip/hydejack-pro-$version

# mkdir -p ~/.ssh
# cp       ~/.ssh/hydejack_8_pro .ssh/

# cp ../../~V9_PROMO_CODE.TXT .

mkdir -p \#jekyll-theme-hydejack
mkdir -p starter-kit

# Make Jekyll theme folder
cp -r \
  ../../\#jekyll-theme-hydejack/assets \
  ../../\#jekyll-theme-hydejack/_includes \
  ../../\#jekyll-theme-hydejack/_layouts \
  ../../\#jekyll-theme-hydejack/_sass \
  ../../\#jekyll-theme-hydejack/_config.yml \
  ../../\#jekyll-theme-hydejack/README.md \
  ../../\#jekyll-theme-hydejack/LICENSE.md \
  ../../\#jekyll-theme-hydejack/NOTICE.md \
  ../../\#jekyll-theme-hydejack/CHANGELOG.md \
  ../../\#jekyll-theme-hydejack/*.gemspec \
  \#jekyll-theme-hydejack

# Make Starter Kit folder
cp -r \
  $(find ../.. \
    -not -name \#jekyll-theme-hydejack \
    -not -name .scripts \
    -not -name .sass-cache \
    -not -name .jekyll-cache \
    -not -name .bundle \
    -not -name node_modules \
    -not -name vendor\
    -not -name _zip  \
    -not -name '.git*' \
    -not -name '*.gem'  \
    -not -name '*~' \
    -not -name '~*' \
    -not -name '_site*' \
    -mindepth 1 \
    -maxdepth 1) \
  starter-kit
cp -r \#jekyll-theme-hydejack starter-kit

find . -name '.DS_Store' -delete

# # Generate PDFs.
# # This assumes the next version is already online at qwtel.com
# # This also assumes macOS with chrome installed...
# function pdfprint {
#   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
#     --headless \
#     --disable-gpu \
#     --disable-translate \
#     --disable-extensions \
#     --disable-background-networking \
#     --safebrowsing-disable-auto-update \
#     --disable-sync \
#     --metrics-recording-only \
#     --disable-default-apps \
#     --no-first-run \
#     --mute-audio \
#     --hide-scrollbars \
#     --run-all-compositor-stages-before-draw \
#     --virtual-time-budget=25000 \
#     --print-to-pdf="$1.pdf" $2
# }

# pdfprint "PRO License" "https://hydejack.com/licenses/PRO/"
# pdfprint "PRO–hy-drawer License" "https://hydecorp.github.io/drawer/licenses/hydejack/"
# pdfprint "PRO–hy-push-state License" "https://hydecorp.github.io/push-state/licenses/hydejack/"
# pdfprint "NOTICE" "https://hydejack.com/NOTICE/"
# pdfprint "CHANGELOG" "https://hydejack.com/CHANGELOG/"
# pdfprint "Documentation" "https://hydejack.com/docs/print/"

# Generate the zip
cd ..; zip -q -r hydejack-pro-$version.zip hydejack-pro-$version/
