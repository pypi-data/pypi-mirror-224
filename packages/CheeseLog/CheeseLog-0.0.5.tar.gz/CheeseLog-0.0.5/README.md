# **CheeseLog**

## **介绍**

一个简单的日志系统。

## **功能**

1. 支持动态的自定义消息格式。

2. 支持控制台消息色彩输出。

3. 支持动态的消息等级设置。

4. 支持动态的日志文件输出。

5. 支持动态的消息过滤。

## **安装**

```bash
pip install CheeseLog
```

## **使用**

### **控制台打印**

```python
from CheeseLog import debug, info, warning, danger, error

debug('Hello World!') # (DEBUG) 2023-07-26 15:47:09.250318 > Hello World!
info('Hello World!') # (INFO) 2023-07-26 15:47:09.250589 > Hello World!
warning('Hello World!') # (WARNING) 2023-07-26 15:47:09.250600 > Hello World!
danger('Hello World!') # (DANGER) 2023-07-26 15:47:09.250611 > Hello World!
error('Hello World!') # (ERROR) 2023-07-26 15:47:09.250618 > Hello World!
```

### **自定义色彩**

自定义色彩后，消息的内容不再自动修改颜色。

```python
from CheeseLog import debug

debug('Hello World!', '\033[32mHello World\033[0m') # (DEBUG) 2023-07-26 15:47:09.250318 > Hello World!
```

### **自定义消息格式**

```python
from CheeseLog import logger, debug

logger.messageTemplate = '[%level] > %timer > %content'
logger.timerTemplate = '%Y-%m-%d %H-%M-%S-%f'

debug('Hello World!') # [DEBUG] > 2023-07-26 15-47-09-250318 > Hello World!
```

### **写入日志文件**

日志文件的创建是惰性的，只有第一次写入操作进行的时候才会尝试创建文件。

```python
from CheeseLog import logger, debug

logger.filepath = './myLog.log'

debug('Hello World!') # 写入 ./muLog.log

logger.filepath = './yourLog.log'

debug('Hello World!') # 写入 ./yourLog.log

logger.stop() # 当程序结束时，可能还有部分内容仍在缓冲区未写入文件，请使用该函数以等待写入完毕
```

### **自定义消息等级**

```python
from CheeseLog import logger, Level, default

print(logger.levels) # 查看已有的等级

logger.levels['MY_LEVEL'] = Level(weight = 20, color = '33') # 设置一个名为MY_LEVEL的等级。

default('MY_LEVEL', 'Hello World!') # (MY_LEVEL) 2023-07-26 17:03:41.982807 > Hello World!
```

### **过滤消息**

```python
from CheeseLog import logger, debug, info, warning

# 指定消息的过滤等级
logger.filter = [ 'DEBUG', 'INFO' ]
debug('Hello World!')
info('Hello World!')
warning('Hello World!') # (WARNING) 2023-07-26 15:47:09.250600 > Hello World!

# 使用权重过滤消息
logger.filter = 15
debug('Hello World!')
info('Hello World!') # (INFO) 2023-07-26 15:47:09.250589 > Hello World!
warning('Hello World!') # (WARNING) 2023-07-26 15:47:09.250600 > Hello World!
```

## **更多...**

### 1. **[消息等级](https://github.com/CheeseUnknown/CheeseLog/tree/master/documents/level.md)**

### 2. **[日志实例](https://github.com/CheeseUnknown/CheeseLog/tree/master/documents/logger.md)**

### 3. **[日志记录](https://github.com/CheeseUnknown/CheeseLog/tree/master/documents/log.md)**
