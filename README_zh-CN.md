# 用于React Native的JS引擎基准测试工具

[English](README.md) | 简体中文

## 测试结果

[测试结果将在Google SpreadSheets上持续更新](https://docs.google.com/spreadsheets/d/1uce3WZ9IaAEUu6Owj3eXEuZb25PDi6ZcgUVV2i500S0/edit#gid=1258377944)

这些基准测试均在Samsung Galaxy Note 5上执行。

## 基准测试

### 渲染测试

[测试结果](https://docs.google.com/spreadsheets/d/1uce3WZ9IaAEUu6Owj3eXEuZb25PDi6ZcgUVV2i500S0/edit#gid=469794458)

下面这些测试用例用于测试在规定时间内能够渲染多少React组件。
- RenderComponentThroughput 10s
- RenderComponentThroughput 60s
- RenderComponentThroughput 180s

我们猜测，在长时间执行重复任务后JIT才会开始工作，因此我们针对不同的渲染时间设置了不同的测试用例。

**结果值越高越好**

### TTI (Time-To-Interaction)

[测试结果](https://docs.google.com/spreadsheets/d/1uce3WZ9IaAEUu6Owj3eXEuZb25PDi6ZcgUVV2i500S0/edit#gid=718456099)

下面这些测试用例用于测试JS引擎解释并执行需要多长时间。
这个时间，或者说是TTI，通过`视图渲染时刻的时间戳 - ReactInstanceManager即将创建时刻的时间戳`获得。
这里对上述算式涉及的名词作一下解释：
- 视图渲染时刻
指ReactRootView的onViewAdded方法被调用的时刻，此时第一个RN组件被渲染到ReactRootView上
- ReactInstanceManager即将创建时刻
指ReactInstanceManager创建前的时刻，换句话说，下一行代码就将执行ReactInstanceManager创建任务

在下面各个测试用例中，我们生成不同大小的JS bundle供应用加载，以此来观察随着bundle大小增大，相应的TTI差异是否更加明显。
- TTI ~3 MiB bundle
- TTI ~10 MiB bundle
- TTI ~15 MiB bundle

### APK大小

[测试结果](https://docs.google.com/spreadsheets/d/1uce3WZ9IaAEUu6Owj3eXEuZb25PDi6ZcgUVV2i500S0/edit#gid=246943941)

简单比较二进制库大小和最终的APK大小。

## 如何执行基准测试

准备环境:

- macOS 10.14 (其他macOS版本或Linux可能也支持)
- Python 3
- Node 8+

执行：

```sh
python3 start.py -a
```

## 免责声明

此项目专门用于测试React Native的JS引擎性能而非通用JS引擎。

例如，在React Native Android上，我们没有启动JavaScriptCore的所有JIT层。在V8上，目前我正在尝试使用无JIT模式。我正尝试在足够好的性能、较低的内存使用率和较小的二进制文件之间找到一个理想的平衡点。这就是为什么有时要禁用JIT。
