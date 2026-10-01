[app]
title = Color Flashlight
package.name = colorflashlight
package.domain = org.myapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,plyer

# Очень важно: запрашиваем доступ к камере (вспышке) смартфона!
android.permissions = CAMERA, FLASHLIGHT

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
