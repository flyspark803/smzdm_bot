"""
什么值得买自动签到脚本
使用github actions 定时执行
@author : stark
"""
import requests,os
from sys import argv

import config
from utils.serverchan_push import push_to_wechat

class SMZDM_Bot(object):
    def __init__(self):
        self.session = requests.Session()
        # 添加 headers
        self.session.headers = config.DEFAULT_HEADERS

    def __json_check(self, msg):
        """
        对请求 盖乐世社区 返回的数据进行进行检查
        1.判断是否 json 形式
        """
        try:
            result = msg.json()
            print(result)
            return True
        except Exception as e:
            print(f'Error : {e}')            
            return False

    def load_cookie_str(self, cookies):
        """
        起一个什么值得买的，带cookie的session
        cookie 为浏览器复制来的字符串
        :param cookie: 登录过的社区网站 cookie
        """
        self.session.headers['Cookie'] = __ckguid=CRc2wjbabCoSEw82QPiPfXf7; device_id=21307064331712103563594907f0b1287c9de56591419711ae04995e4b; homepage_sug=a; r_sort_type=score; sess=BA-1U%2BeA%2BV8jHvo%2FGkdWvw5BrcMXiGdKF%2B9ozkw4ytystZVqFTwlNF%2BZn273ctFJBRMYu1OK65%2FL5Wo%2BnaWzM1oO0VXP%2BuGR%2FXsuvd0LvHuVbvLt4wFWcAiIhYY; user=user%3A5404570445%7C5404570445; smzdm_id=5404570445; _zdmA.vid=*; footer_floating_layer=0; ad_date=16; ad_json_feed=%7B%7D; _zdmA.uid=ZDMA.OE3VZzBb1.1715831081.2419200; bannerCounter=%5B%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A8%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A3%2C%22surplus%22%3A1%7D%5D; _zdmA.time=1715831230048.0.https%3A%2F%2Fwww.smzdm.com%2F    

    def checkin(self):
        """
        签到函数
        """
        url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
        msg = self.session.get(url)
        if self.__json_check(msg):
            return msg.json()
        return msg.content




if __name__ == '__main__':
    sb = SMZDM_Bot()
    # sb.load_cookie_str(config.TEST_COOKIE)
    cookies = os.environ["COOKIES"]
    sb.load_cookie_str(cookies)
    res = sb.checkin()
    print(res)
    SERVERCHAN_SECRETKEY = os.environ["SERVERCHAN_SECRETKEY"]
    print('sc_key: ', SERVERCHAN_SECRETKEY)
    if isinstance(SERVERCHAN_SECRETKEY,str) and len(SERVERCHAN_SECRETKEY)>0:
        print('检测到 SCKEY， 准备推送')
        push_to_wechat(text = '什么值得买每日签到',
                        desp = str(res),
                        secretKey = SERVERCHAN_SECRETKEY)
    print('代码完毕')
