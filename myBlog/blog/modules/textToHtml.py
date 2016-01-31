# -*- coding:utf8 -*-


class TextToHtml(object):
    def __init__(self):
        pass

    def txt2html(self, txt):
        """将txt以行为单位加上<li></li>标签"""
        def escape(txt):
            """将txt文本中的空格、&、<、>、（"）、（'）
            转化成对应的的字符实体，以方便在html上显示"""

            txt = txt.replace('&', '&#38;')
            txt = txt.replace(' ', '&#160;')
            txt = txt.replace('<', '<')
            txt = txt.replace('>', '>')
            txt = txt.replace('"', '&#34;')
            txt = txt.replace('\'', '&#39;')
            return txt

        txt = escape(txt)
        lines = txt.split('\n')
        for i, line in enumerate(lines):
            lines[i] = '<p>' + line + '</p>'
        txt = ''.join(lines)
        return txt

zen = u"""The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
            """

# print TextToHtml().txt2html(zen)
