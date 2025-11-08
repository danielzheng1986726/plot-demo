#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试文字转 Emoji 转换器
"""

from text_to_emoji import TextToEmojiConverter


def test_converter():
    """测试转换器的基本功能"""
    converter = TextToEmojiConverter()

    # 测试用例
    test_cases = [
        ("我今天很开心", "append"),
        ("我喜欢吃苹果和香蕉", "append"),
        ("外面下雨了", "both"),
        ("加油工作", "replace"),
        ("猫和狗是好朋友", "append"),
    ]

    print("=" * 60)
    print("文字转 Emoji 转换器测试")
    print("=" * 60 + "\n")

    for text, mode in test_cases:
        result = converter.convert(text, mode=mode)
        emoji_count = converter.get_emoji_count(text)
        print(f"原文：{text}")
        print(f"模式：{mode}")
        print(f"结果：{result}")
        print(f"转换：{emoji_count} 个关键词\n")

    print("=" * 60)
    print("测试完成！")
    print("=" * 60)


if __name__ == "__main__":
    test_converter()
