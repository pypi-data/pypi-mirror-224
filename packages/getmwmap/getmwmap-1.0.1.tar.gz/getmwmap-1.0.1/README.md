# getmwmap: 为MW锦标赛提高快速随机抽取地图的拓展

`getmwmap` 是一个用于MW锦标赛的Python包，旨在提供一种快速随机抽取地图的方式。它可以从地图列表中获取指定数量的随机地图，并支持限制特定地图的使用。

## 安装

您可以使用以下命令通过`pip`安装 `getmwmap` 包：

```bash
pip install getmwmap
```

## 使用方法

导入 `getmwmap` 函数并调用它，如下所示：

```python
from getmwmap import getMap

# 获取4个随机地图，限制地图 "未开发岩石区" 和 "失落之城"
random_maps = getMap(4, ["未开发岩石区", "失落之城"])
print("随机地图：", random_maps)
```

## 许可证

这个项目在 [AGPL 3.0](https://www.gnu.org/licenses/agpl-3.0.html) 许可证下发布。请查阅许可证文档以了解更多详情。


## 问题和反馈

如果您遇到任何问题或者有任何反馈，请在QQ频道联系MWCTTO技术人员