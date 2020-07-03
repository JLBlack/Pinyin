#!/bin/usr/envpython3

import unicodedata


def as_ascii(input: str):
    normalized = unicodedata.normalize('NFD', input)
    return normalized.encode('ascii', 'ignore')


(0, '零', 'Líng'),
(1, '一', 'Yī'),
(2, '二', 'Èr'),
(3, '三', 'Sān'),
(4, '四', 'Sì'),
(5, '五', 'Wǔ'),
(6, '六', 'Liù'),
(7, '七', 'Qī'),
(8, '八', 'Bā'),
(9, '九', 'Jiǔ'),
(10, '十', 'Shí'),
(11, '十一', 'Shíyī'),
(12, '十二', 'Shíèr'),
(13, '十三', 'Shísān'),
(14, '十四', 'Shísì'),
(15, '十五', 'Shíwǔ'),
(16, '十六', 'Shíliù'),
(17, '十七', 'Shíqī'),
(18, '十八', 'Shíbā'),
(19, '十九', 'Shíjiǔ'),
(20, '二十', 'Èrshí'),
(21, '二十一', 'Èrshíyī'),
(22, '二十二', 'Èrshíèr'),
(23, '二十三', 'Èrshísān'),
(24, '二十四', 'Èrshísì'),
(25, '二十五', 'Èrshíwǔ'),
(26, '二十六', 'Èrshíliù'),
(27, '二十七', 'Èrshíqī'),
(28, '二十八', 'Èrshíbā'),
(29, '二十九', 'Èrshíjiǔ'),
(30, '三十', 'Sānshí'),
(31, '三十一', 'Sānshíyī'),
(32, '三十二', 'Sānshíèr'),
(33, '三十三', 'Sānshísān'),
(34, '三十四', 'Sānshísì'),
(35, '三十五', 'Sānshíwǔ'),
(36, '三十六', 'Sānshíliù'),
(37, '三十七', 'Sānshíqī'),
(38, '三十八', 'Sānshíbā'),
(39, '三十九', 'Sānshíjiǔ'),
(40, '四十', 'Sìshí'),
(41, '四十一', 'Sìshíyī'),
(42, '四十二', 'Sìshíèr'),
(43, '四十三', 'Sìshísān'),
(44, '四十四', 'Sìshísì'),
(45, '四十五', 'Sìshíwǔ'),
(46, '四十六', 'Sìshíliù'),
(47, '四十七', 'Sìshíqī'),
(48, '四十八', 'Sìshíbā'),
(49, '四十九', 'Sìshíjiǔ'),
(50, '五十', 'Wǔshí'),
(51, '五十一', 'Wǔshíyī'),
(52, '五十二', 'Wǔshíèr'),
(53, '五十三', 'Wǔshísān'),
(54, '五十四', 'Wǔshísì'),
(55, '五十五', 'Wǔshíwǔ'),
(56, '五十六', 'Wǔshíliù'),
(57, '五十七', 'Wǔshíqī'),
(58, '五十八', 'Wǔshíbā'),
(59, '五十九', 'Wǔshíjiǔ'),
(60, '六十', 'Liùshí'),
(61, '六十一', 'Liùshíyī'),
(62, '六十二', 'Liùshíèr'),
(63, '六十三', 'Liùshísān'),
(64, '六十四', 'Liùshísì'),
(65, '六十五', 'Liùshíwǔ'),
(66, '六十六', 'Liùshíliù'),
(67, '六十七', 'Liùshíqī'),
(68, '六十八', 'Liùshíbā'),
(69, '六十九', 'Liùshíjiǔ'),
(70, '七十', 'Qīshí'),
(71, '七十一', 'Qīshíyī'),
(72, '七十二', 'Qīshíèr'),
(73, '七十三', 'Qīshísān'),
(74, '七十四', 'Qīshísì'),
(75, '七十五', 'Qīshíwǔ'),
(76, '七十六', 'Qīshíliù'),
(77, '七十七', 'Qīshíqī'),
(78, '七十八', 'Qīshíbā'),
(79, '七十九', 'Qīshíjiǔ'),
(80, '八十', 'Bāshí'),
(81, '八十一', 'Bāshíyī'),
(82, '八十二', 'Bāshíèr'),
(83, '八十三', 'Bāshísān'),
(84, '八十四', 'Bāshísì'),
(85, '八十五', 'Bāshíwǔ'),
(86, '八十六', 'Bāshíliù'),
(87, '八十七', 'Bāshíqī'),
(88, '八十八', 'Bāshíbā'),
(89, '八十九', 'Bāshíjiǔ'),
(90, '九十', 'Jiǔshí'),
(91, '九十一', 'Jiǔshíyī'),
(92, '九十二', 'Jiǔshíèr'),
(93, '九十三', 'Jiǔshísān'),
(94, '九十四', 'Jiǔshísì'),
(95, '九十五', 'Jiǔshíwǔ'),
(96, '九十六', 'Jiǔshíliù'),
(97, '九十七', 'Jiǔshíqī'),
(98, '九十八', 'Jiǔshíbā'),
(99, '九十九', 'Jiǔshíjiǔ'),
(100, '一百', 'Yìbǎi'),

('white', 'bái sè', '白色'),
('blue', 'lán sè', '蓝色'),
('yellow', 'huáng sè', '黄色'),
('green', 'lǜ sè', '绿色'),
('red', 'hóng sè', '红色'),
('orange1', 'jú sè', '橘色'),
('orange2', 'chéng sè', '橙色'),
('brown', 'kāfēi sè', '咖啡色'),
('black', 'hēi sè', '黑色'),
('purple', 'zǐ sè', '紫色'),
('grey', 'huī sè', '灰色'),
