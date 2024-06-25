[app]
# (str) Title of your application
title = Weather App

# (str) Package name
package.name = weather_app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# The dependencies your application requires
requirements = python3,kivy,requests

# (str) Application entry point
entrypoint = main.py

# (list) Permissions
# Specify any additional permissions required by your app
android.permissions = INTERNET

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/presplash.png

# (str) Presplash background color (for android)
presplash.color = #FFFFFF

# (list) Patterns to exclude from the source copy
source.exclude_exts = spec

# (str) The architecture to target when building for Android
android.arch = armeabi-v7a

[buildozer]
# (int) Log level (0-2) -- 0 = only critical messages, 1 = all except debug messages, 2 = debug messages
log_level = 2

# (bool) Warn on build as root
warn_on_root = 1

# (str) Android API to use
android.api = 28

# (str) Android NDK version to use
android.ndk = 19b

# (str) Directory in which to store the android SDK
android.sdk_path = /home/user/Android/Sdk

# (str) Directory in which to store the android NDK
android.ndk_path = /home/user/Android/Sdk/ndk-bundle

# (str) Directory in which to store android ndk
android.ndk_path = /home/user/Android/Sdk/ndk-bundle

# (str) Path to the Android SDK
# Replace with the actual path if you have manually installed the SDK
android.sdk = /home/user/Android/Sdk

# (str) Path to the Android NDK
# Replace with the actual path if you have manually installed the NDK
android.ndk = /home/user/Android/Sdk/ndk-bundle

# (str) Command to run to use the build cache
android.build_cache = /home/user/.buildozer/android/platform/build-arm64-v8a/dists

# (bool) Copy in default dependencies
android.copy_dists = 1
