# Android ABI
Android支持四种架构，分别是intel和arm的32位和64为架构，每一种架构有其独特的ABI(Application Binary Interface，应用程序二进制接口)。  
使用vcpkg编译NDK的时候，需要先安装好特定平台的包。

|VCPKG_TARGET_TRIPLET|	ANDROID_ABI|
|---|---|
|arm64-android|	arm64-v8a|
|arm-android|	armeabi-v7a|
|x64-android|	x86_64|
|x86-android|	x86|