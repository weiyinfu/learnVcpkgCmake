vcpkg的包的个数是1800+，已经足够使用了，但是我们自己也可以提供包。  

# 从github构建vcpkg的包
以libogg为例，首先在ports/libogg/vcpkg.json中创建版本和描述信息。
```json
{
  "name": "libogg",
  "version-string": "1.3.3",
  "description": "Ogg is a multimedia container format, and the native file and stream format for the Xiph.org multimedia codecs."
}
```
ports/libogg/portscmake.cmake
```cmake
vcpkg_from_github(
    OUT_SOURCE_PATH SOURCE_PATH
    REPO xiph/ogg
    REF v1.3.3
    SHA512 0bd6095d647530d4cb1f509eb5e99965a25cc3dd9b8125b93abd6b248255c890cf20710154bdec40568478eb5c4cde724abfb2eff1f3a04e63acef0fbbc9799b
    HEAD_REF master
)
vcpkg_configure_cmake(
    SOURCE_PATH ${SOURCE_PATH}
    PREFER_NINJA
)
vcpkg_install_cmake()
file(INSTALL ${SOURCE_PATH}/COPYING DESTINATION ${CURRENT_PACKAGES_DIR}/share/libogg RENAME copyright)
```
指明一个github地址，设置好SHA512，实际上SHA512一开始可以设置成1，等安装失败了再过来改掉。  

vcpkg/ports目录下有很多个例子，是学习cmake的好资料。  