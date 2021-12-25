# 把vcpkg项目放在项目目录中
编辑ports即可实现版本管理，在一个vcpkg中，不允许出现版本冲突，用户必须手动解决菱形冲突。    
# 只是用vcpkg的产物
`vcpkg export protobuf`

# 与cmake的配合
`include(<vcpkg_root>\scripts\buildsystems\vcpkg.cmake)`