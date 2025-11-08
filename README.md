![Plot](square_plot.png)

# 项目功能

## 1. 方形图表绘制
使用 `plot_square.py` 绘制方形图表

## 2. 文字转 Emoji 转换器

一个智能的中文文字到 Emoji 表情转换工具，支持 200+ 个常用关键词。

### 功能特性

- 🎯 智能关键词识别：自动识别文本中的关键词并转换为对应的 emoji
- 🔄 多种转换模式：
  - **append** - 在关键词后添加 emoji（默认模式）
  - **replace** - 用 emoji 替换关键词
  - **both** - 同时显示关键词和 emoji
- 📚 丰富的 emoji 库：支持情感、动物、食物、天气、交通、运动等多个分类
- 💬 交互式界面：友好的命令行交互体验

### 使用方法

#### 交互式模式

```bash
python3 text_to_emoji.py
```

然后按照提示输入文字即可。

#### 编程接口

```python
from text_to_emoji import TextToEmojiConverter

converter = TextToEmojiConverter()

# 默认模式（追加）
text = "我今天很开心"
result = converter.convert(text)
print(result)  # 输出：我今天很开心😊

# 替换模式
result = converter.convert("加油工作", mode='replace')
print(result)  # 输出：💪💼

# 同时显示模式
result = converter.convert("下雨了", mode='both')
print(result)  # 输出：下(⬇️)雨(🌧️)了
```

### 支持的关键词类别

- 😊 情感表达：开心、难过、生气、喜欢、爱等
- 🐱 动物：猫、狗、熊、兔、鸟等
- 🍎 食物：苹果、香蕉、蛋糕、咖啡等
- ☀️ 天气自然：太阳、雨、雪、花、树等
- 🚗 交通工具：车、飞机、火车、自行车等
- ⚽ 运动活动：足球、篮球、游泳、跑步等
- 💻 物品符号：电话、电脑、礼物、钱等
- 👍 手势人物：好、加油、鼓掌、祈祷等

### 命令说明

在交互模式下支持以下命令：

- `/mode <模式>` - 切换转换模式（append/replace/both）
- `/list` - 查看所有支持的关键词
- `/help` - 显示帮助信息
- `/quit` - 退出程序

### 测试

运行测试程序查看效果：

```bash
python3 test_emoji.py
```
