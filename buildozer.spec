[app]
title = Zorva
package.name = zorva
package.domain = com.karim.zorva
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.0,requests,certifi,charset-normalizer,idna,urllib3
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.allow_backup = False

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.accept_sdk_license_agreements = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
p4a.branch = master
android.archs = arm64-v8a, armeabi-v7a
android.ant = False
android.gradle_dependencies =
p4a.bootstrap = sdl2
