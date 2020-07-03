#!/bin/usr/env python3

import random

import unicodedata

import typing

class Numbers(typing.NamedTuple):
    value: int
    character: str
    pinyin: str 

class Colors(typing.NamedTuple):
    value: str
    character: str
    pinyin: str 

def as_ascii(input: str):
    normalized = unicodedata.normalize('NFD', input)
    as_bytes = normalized.encode('ascii', 'ignore')
    return as_bytes.decode('ascii')

COLORS = [
    Colors('white', 'báisè', '白色'),
    Colors('blue', 'lánsè', '蓝色'),
    Colors('yellow', 'huángsè', '黄色'),
    Colors('green', 'lǜsè', '绿色'),
    Colors('red', 'hóngsè', '红色'),
    Colors('orange1', 'júsè', '橘色'),
    Colors('orange2', 'chéngsè', '橙色'),
    Colors('brown', 'kāfēisè', '咖啡色'),
    Colors('black', 'hēisè', '黑色'),
    Colors('purple', 'zǐsè', '紫色'),
    Colors('grey', 'huīsè', '灰色'),
]

NUMBERS = [
    Numbers(0, '零', 'Líng'),
    Numbers(1, '一', 'Yī'),
    Numbers(2, '二', 'Èr'),
    Numbers(3, '三', 'Sān'),
    Numbers(4, '四', 'Sì'),
    Numbers(5, '五', 'Wǔ'),
    Numbers(6, '六', 'Liù'),
    Numbers(7, '七', 'Qī'),
    Numbers(8, '八', 'Bā'),
    Numbers(9, '九', 'Jiǔ'),
    Numbers(10, '十', 'Shí'),
    Numbers(11, '十一', 'Shíyī'),
    Numbers(12, '十二', 'Shíèr'),
    Numbers(13, '十三', 'Shísān'),
    Numbers(14, '十四', 'Shísì'),
    Numbers(15, '十五', 'Shíwǔ'),
    Numbers(16, '十六', 'Shíliù'),
    Numbers(17, '十七', 'Shíqī'),
    Numbers(18, '十八', 'Shíbā'),
    Numbers(19, '十九', 'Shíjiǔ'),
    Numbers(20, '二十', 'Èrshí'),
    Numbers(21, '二十一', 'Èrshíyī'),
    Numbers(22, '二十二', 'Èrshíèr'),
    Numbers(23, '二十三', 'Èrshísān'),
    Numbers(24, '二十四', 'Èrshísì'),
    Numbers(25, '二十五', 'Èrshíwǔ'),
    Numbers(26, '二十六', 'Èrshíliù'),
    Numbers(27, '二十七', 'Èrshíqī'),
    Numbers(28, '二十八', 'Èrshíbā'),
    Numbers(29, '二十九', 'Èrshíjiǔ'),
    Numbers(30, '三十', 'Sānshí'),
    Numbers(31, '三十一', 'Sānshíyī'),
    Numbers(32, '三十二', 'Sānshíèr'),
    Numbers(33, '三十三', 'Sānshísān'),
    Numbers(34, '三十四', 'Sānshísì'),
    Numbers(35, '三十五', 'Sānshíwǔ'),
    Numbers(36, '三十六', 'Sānshíliù'),
    Numbers(37, '三十七', 'Sānshíqī'),
    Numbers(38, '三十八', 'Sānshíbā'),
    Numbers(39, '三十九', 'Sānshíjiǔ'),
    Numbers(40, '四十', 'Sìshí'),
    Numbers(41, '四十一', 'Sìshíyī'),
    Numbers(42, '四十二', 'Sìshíèr'),
    Numbers(43, '四十三', 'Sìshísān'),
    Numbers(44, '四十四', 'Sìshísì'),
    Numbers(45, '四十五', 'Sìshíwǔ'),
    Numbers(46, '四十六', 'Sìshíliù'),
    Numbers(47, '四十七', 'Sìshíqī'),
    Numbers(48, '四十八', 'Sìshíbā'),
    Numbers(49, '四十九', 'Sìshíjiǔ'),
    Numbers(50, '五十', 'Wǔshí'),
    Numbers(51, '五十一', 'Wǔshíyī'),
    Numbers(52, '五十二', 'Wǔshíèr'),
    Numbers(53, '五十三', 'Wǔshísān'),
    Numbers(54, '五十四', 'Wǔshísì'),
    Numbers(55, '五十五', 'Wǔshíwǔ'),
    Numbers(56, '五十六', 'Wǔshíliù'),
    Numbers(57, '五十七', 'Wǔshíqī'),
    Numbers(58, '五十八', 'Wǔshíbā'),
    Numbers(59, '五十九', 'Wǔshíjiǔ'),
    Numbers(60, '六十', 'Liùshí'),
    Numbers(61, '六十一', 'Liùshíyī'),
    Numbers(62, '六十二', 'Liùshíèr'),
    Numbers(63, '六十三', 'Liùshísān'),
    Numbers(64, '六十四', 'Liùshísì'),
    Numbers(65, '六十五', 'Liùshíwǔ'),
    Numbers(66, '六十六', 'Liùshíliù'),
    Numbers(67, '六十七', 'Liùshíqī'),
    Numbers(68, '六十八', 'Liùshíbā'),
    Numbers(69, '六十九', 'Liùshíjiǔ'),
    Numbers(70, '七十', 'Qīshí'),
    Numbers(71, '七十一', 'Qīshíyī'),
    Numbers(72, '七十二', 'Qīshíèr'),
    Numbers(73, '七十三', 'Qīshísān'),
    Numbers(74, '七十四', 'Qīshísì'),
    Numbers(75, '七十五', 'Qīshíwǔ'),
    Numbers(76, '七十六', 'Qīshíliù'),
    Numbers(77, '七十七', 'Qīshíqī'),
    Numbers(78, '七十八', 'Qīshíbā'),
    Numbers(79, '七十九', 'Qīshíjiǔ'),
    Numbers(80, '八十', 'Bāshí'),
    Numbers(81, '八十一', 'Bāshíyī'),
    Numbers(82, '八十二', 'Bāshíèr'),
    Numbers(83, '八十三', 'Bāshísān'),
    Numbers(84, '八十四', 'Bāshísì'),
    Numbers(85, '八十五', 'Bāshíwǔ'),
    Numbers(86, '八十六', 'Bāshíliù'),
    Numbers(87, '八十七', 'Bāshíqī'),
    Numbers(88, '八十八', 'Bāshíbā'),
    Numbers(89, '八十九', 'Bāshíjiǔ'),
    Numbers(90, '九十', 'Jiǔshí'),
    Numbers(91, '九十一', 'Jiǔshíyī'),
    Numbers(92, '九十二', 'Jiǔshíèr'),
    Numbers(93, '九十三', 'Jiǔshísān'),
    Numbers(94, '九十四', 'Jiǔshísì'),
    Numbers(95, '九十五', 'Jiǔshíwǔ'),
    Numbers(96, '九十六', 'Jiǔshíliù'),
    Numbers(97, '九十七', 'Jiǔshíqī'),
    Numbers(98, '九十八', 'Jiǔshíbā'),
    Numbers(99, '九十九', 'Jiǔshíjiǔ'),
    Numbers(100, '一百', 'Yìbǎi'),
]

while True:
    current_character = random.choice(NUMBERS)
    current_characters = random.choice(COLORS)
    remaining_attempts = 2
    expected = as_ascii(current_character.pinyin.lower, current_characters.pinyin.lower())

    while remaining_attempts > 0:
        answer = input(f"What does {current_character.character}{current_characters.character} mean? ")
        if answer.lower() == expected:
            print(current_character.pinyin or current_characters.pinyin)
            break
        else:
            print("Not quite!", end=" ")
            remaining_attempts -= 1
        if remaining_attempts == 0:
            print("Try this instead:")
