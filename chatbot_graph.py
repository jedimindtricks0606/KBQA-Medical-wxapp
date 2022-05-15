#!/usr/bin/env python3
# coding: utf-8
# File: chatbot_graph.py

from question_classifier import *
from question_parser import *
from answer_search import *

'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    # 基于规则的问答系统没有复杂的算法，一般采用模板匹配的方式寻找匹配度最高的答案，
    # 回答结果依赖于问句类型、模板语料库的覆盖全面性，面对已知的问题，可以给出合适的答案。
    def chat_main(self, sent):
        # if sent == '你好':
        #     return '你好，有什么问题吗？'
        idk = '抱歉，我不知道怎么回答这个问题。祝你身体棒棒！'
        res_classify = self.classifier.classify(sent)  # 问题分类 res_classify是一个dict
        if not res_classify:
            return idk
        res_sql = self.parser.parser_main(res_classify)  # 问题解析
        ans = self.searcher.search_main(res_sql)  # 执行cypher查询，并返回相应结果
        if not ans:
            return idk
        else:
            return '\n'.join(ans)


if __name__ == '__main__':
    print('initializing...')
    handler = ChatBotGraph()
    print('欢迎来到大番茄医生的诊所，有什么可以帮你？')
    while 1:
        question = input('提问: ')
        if question == '886' or question == '再见' or question == '拜拜':
            print("大番茄医生: 再见(｡･ω･｡)ﾉ")
            exit(0)
        answer = handler.chat_main(question)
        print('大番茄医生: ', answer)
