# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/HYOWV7ImvTXImyYWtwADog
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/9 22:50 
@本段代码的视频说明     ：
'''
import jieba
# 生成词云需要使用的类库
from wordcloud import WordCloud


class ImageProcess:
    def txt2wordcloud(self, filename: str, color: str, result_file: str):
        """
        @Author & Date  : CoderWanFeng 2022/4/28 9:26
        @Desc  : 生成词云的代码，可以添加更多个性化功能
        @Return  ：
        """
        # print("txt2wordcloud，该功能已过期")

        with open(filename, encoding='utf8') as fp:
            text = fp.read()
            # 将读取的中文文档进行分词
            # 接收分词的字符串
            word_list = jieba.cut(text)
            # 分词后在单独个体之间加上空格
            cloud_text = " ".join(word_list)

            # 生成wordcloud对象
            wc = WordCloud(background_color=color,
                           max_words=200,
                           min_font_size=15,
                           max_font_size=50,
                           width=400,
                           font_path="msyh.ttc",  # 默认的简体中文字体，没有会报错
                           )
            wc.generate(cloud_text)
            wc.to_file(result_file)
