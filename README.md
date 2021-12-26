# vcpkg官方文档
* https://vcpkg.io/en/getting-started.html
* https://vcpkg.readthedocs.io/en/latest/about/faq/  

vcpkg是一类东西，是一种解决方案。  
数据集管理器与vcpkg逻辑类似，为每个数据集单独写一个构建脚本，将数据集下载到指定目录。  

# cmake官方文档
https://cmake.org/cmake/help/latest/index.html
cmake用于生成make、ninja等文件。  
CMakeTutorial:https://github.com/BrightXiaoHan/CMakeTutorial
# ninja
gn、cmake、premake等编译处理工具相当于高级语言，它们的目标就是生成ninja这样的"汇编语言"。  
ninja的作用是"锦上添花"的，因为它位于比较底层的位置，大多数用户无需直接使用ninja。ninja的作用就是能够让减少文件改变到编译之间需要花费的时间。  
ninja的原理是更合理的处理依赖以及依赖发生变化之后应该执行的动作。  
ninja与make比较相似，但是ninja的语法是make的缩减版。  
ninja是google开发chrome的一位工程师的作品，它能够大大提升改动代码之后的编译速度。  

https://ninja-build.org/manual.html#_tarball_extraction