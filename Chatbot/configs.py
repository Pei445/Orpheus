# -*- coding:utf-8 -*-
"""
Created on 18/5/29 上午11:35.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

class Configs(object):

    def __init__(self):

        # 对话系统基本信息
        self.name = "Orpheus"
        self.debug_mode = True

        # 数据库连接
        self.db_ip = "116.56.140.95"
        self.db_username = 'root'
        self.db_password = '198720'
        self.db_database = 'DialogueSystem'

        # AIML
        self.aiml_nlu_path = "./aiml/nlu-startup.xml"
        self.aiml_nlu_pattern = "load aiml nlu"
        self.aiml_nlg_path = "./aiml/nlg-startup.xml"
        self.aiml_nlg_pattern = "load aiml nlg"

        # LTP
        self.ltp_seg_model_path = "./utils/ltp/models/cws.model"
        self.ltp_seg_lexicon_path = "./utils/ltp/user_lexicon.txt"
        self.ltp_pos_model_path = "./utils/ltp/models/pos.model"
        self.ltp_rec_model_path = "./utils/ltp/models/ner.model"
        self.ltp_par_model_path = "./utils/ltp/models/parser.model"