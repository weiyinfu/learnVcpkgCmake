# Triplets
triplets:三元组，意思是目标库可以用三元组进行描述。在triplets目录下可以找到所有支持的triplets。    
<体系架构>-<操作系统>-<动态静态>  
* 体系架构：x64，x86,arm64,arm
* 操作系统：linux、windows、android、osx
* 动态静态：dynamic、static

安装的时候，使用`vcpkg install protobuf:arm-android`命令进行安装特定triplet的库。也可以使用triplets参数,例如：`vcpkg install --triplet arm-android protobuf`

triplets目录下，有一个community文件夹，里面存放社区贡献的triplets。现在所有的triplets如下：

* x64-linux.cmake
* x64-windows.cmake
* x64-windows-static.cmake
* x86-windows.cmake
* arm64-windows.cmake
* x64-uwp.cmake
* x64-osx.cmake
* arm-uwp.cmake
* wasm32-emscripten.cmake
* ppc64le-linux.cmake
* x86-mingw-static.cmake
* arm64-ios.cmake
* x64-mingw-dynamic.cmake
* x64-windows-release.cmake
* x86-freebsd.cmake
* armv6-android.cmake
* x64-osx-release.cmake
* x64-android.cmake
* x86-windows-static.cmake
* arm-android.cmake
* arm64-mingw-dynamic.cmake
* arm64-osx.cmake
* arm64-windows-static.cmake
* arm-linux.cmake
* arm-windows.cmake
* arm64-uwp.cmake
* x86-mingw-dynamic.cmake
* s390x-linux.cmake
* x64-openbsd.cmake
* arm-mingw-dynamic.cmake
* arm-neon-android.cmake
* x64-ios.cmake
* x64-mingw-static.cmake
* arm-ios.cmake
* x64-osx-dynamic.cmake
* x64-linux-release.cmake
* x86-android.cmake
* x86-uwp.cmake
* arm64-linux.cmake
* x64-freebsd.cmake
* arm64-windows-static-md.cmake
* arm64-mingw-static.cmake
* x86-windows-static-md.cmake
* arm-mingw-static.cmake
* arm64-osx-dynamic.cmake
* x86-ios.cmake
* x64-windows-static-md.cmake
* arm64-android.cmake
* arm-windows-static.cmake
* x86-windows-v120.cmake

vcpkg默认加载triplets/和triplets/community两个目录下的triplets。用户也可以自己在triplets目录下新建文件夹，例如custom-triplets，使用的时候指明`--overlay-triplets`参数。例如`vcpkg install sqlite3:x64-linux-dynamic --overlay-triplets=custom-triplets`。

在安装的时候，在windows下默认创建的是动态链接库，在linux、mac下默认创建的是静态链接库。