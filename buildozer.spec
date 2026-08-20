[app]
title = Zorva
package.name = zorva
package.domain = com.karim.zorva
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
rerequirements = hostpython3==3.10.13,python3==3.10.13,kivy,requests,certifi,charset-normalizer,idna,urllib3
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.accept_sdk_license_agreements = True
android.api = 33
android.minapi = 21
android.ndk = 28c
p4a.branch = stable
android.arch = arm64-v8a
