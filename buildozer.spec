[app]
title = Zorva
package.name = zorva
package.domain = com.karim.zorva
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
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
android.ndk = 25b
p4a.branch = stable
android.arch = armeabi-v7a
