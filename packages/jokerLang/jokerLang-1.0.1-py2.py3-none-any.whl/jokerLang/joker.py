
import os
import requests
class Joker:
    """
    ################################
    ######   author: joker    ######
    ######   QQ: 524276169    ######
    ######   update:2023/8/13 ######
    ################################

    findPhonePlace:参数手机号，获取手机号所在地址
    createProgressBar: create a progress bar,
        params:
            max_value[the end value]
            update_value[every epoch update value]
            sleep: whether to set a delay
    sendMessage:send message
        params:
            phone: you know
            message:the message you want send
        notice: remember to change your userid,account and password in the url
    freeApi: some interesting free api demo
        mode:
            0: every day a sentence
            1: comfort somebody
            2: according to the real time,the function will give a sentence
            3: save a pretty_girl video named girl_video.mp4
            4: save your qq's headshot
            5: abandoned
            6: abandoned
            7: generate a backup's(tian gou)  quote
            8: generate a real life girl picture
            9: abandoned
            10: save a girl headshot
            11: sadness emotion quote
            12: an interesting conversation
            13: a joke sentence
            14: famous person's quote
            15: abandoned
            16: abandoned
            17: abandoned
            18: abandoned
            19: create a picture content your message
                params:msg
            20: return a sexual quote
            21: joke sentence 2.0
            22: get a elegent quote
            23: get a skinny quote
    """

    def checkResource(self):
        if not os.path.exists('resource'):
            os.mkdir('resource')

    def __init__(self):
        self.checkResource()

    def findPhonePlace(self, number=None):
        from phone import Phone
        p = Phone()
        return p.find(number)
        # pip install phone

    def createProgressBar(self, max_value, update_value, sleep=True):
        # pip install progressbar2
        # in most task,this function won't be uesd
        import time
        import progressbar
        p = progressbar.ProgressBar()  # 实例化进度条
        max_value = max_value
        p.start(max_value)
        n = 0
        while n < 100:
            p.update(n)  # 更新
            n += update_value
            if sleep:
                time.sleep(0.1)
        p.finish()

    def sendMessage(self, phone, message):
        import requests
        url = f'http://47.105.48.125:8888/sms.aspx?action=send&userid=541&account=深度学习' \
              f'&password=123456&mobile={phone}&content=【萨维塔的小屋】您的验证码为: {message}（若非本人操作，请删除本短信）'
        resp = requests.post(url)
        print(resp.text)

    def freeApi(self, mode=0, qq=None, msg=None):
        if mode == 0:
            # a single useless sentence
            resp = requests.get('https://v.api.aa1.cn/api/yiyan/index.php')
            text = resp.text.split('>')[1].split('<')[0]
            return text
        elif mode == 1:
            # when somebody feel sad,you should use this api to comfort him/her
            resp = requests.get('https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=json')
            text = resp.text.split(":")[1].split('"')[1]
            return text
        elif mode == 2:
            # according to the real time,it will return you different sentences
            resp = requests.get('https://v.api.aa1.cn/api/time-tx/index.php')
            return str(eval(resp.text).get("nxyj"))
        elif mode == 3:
            # save a pretty girl video  (0o0)
            url = 'https://v.api.aa1.cn/api/api-girl-11-02/index.php?type=json'
            resp = requests.get(url)
            url = 'https:' + resp.json().get("mp4")
            resp = requests.get(url)
            with open('resource/girl_video.mp4', 'wb') as f:
                f.write(resp.content)
            return 'success'
        elif mode == 4:
            resp = requests.get(f'https://v.api.aa1.cn/api/qqimg/index.php?qq={qq}')
            img_url = resp.text.split('src')[1][1:-1]
            with open('resource/QQ_pic.jpg', 'wb') as f:
                f.write(requests.get(img_url).content)
                print('获取成功')
            return 'success'
        elif mode == 5:
            pass

        elif mode == 6:
            pass
        elif mode == 7:
            resp = requests.get('https://v.api.aa1.cn/api/tiangou/index.php')
            return resp.text.split('>')[1].split("<")[0]
        elif mode == 8:
            resp = requests.get('https://v.api.aa1.cn/api/pc-girl_bz/index.php?wpon=json')
            img_url = 'https:' + eval(resp.text).get('img')
            with open('resource/pretty_girl.jpg', 'wb') as f:
                f.write(requests.get(img_url).content)
                print('图片保存成功')
            return 'success'
        elif mode == 9:
            pass
        elif mode == 10:
            resp = requests.get('https://v.api.aa1.cn/api/api-tx/index.php?wpon=json')
            img_url = 'https:' + eval(resp.text).get('img')
            with open('resource/head_shot_girl.jpg', 'wb') as f:
                f.write(requests.get(img_url).content)
                print('图片保存成功')
            return 'success'
        elif mode == 11:
            resp = requests.get('https://v.api.aa1.cn/api/api-wenan-qg/index.php?aa1=json')
            return eval(resp.text)[0].get('qinggan')
        elif mode == 12:
            resp = requests.get('https://v.api.aa1.cn/api/api-wenan-shenhuifu/index.php?aa1=json')
            return eval(resp.text)[0].get("shenhuifu")
        elif mode == 13:
            resp = requests.get('https://v.api.aa1.cn/api/api-wenan-gaoxiao/index.php?aa1=json')
            return eval(resp.text)[0].get('gaoxiao')
        elif mode == 14:
            resp = requests.get('https://v.api.aa1.cn/api/api-wenan-mingrenmingyan/index.php?aa1=json')
            return eval(resp.text)[0].get('mingrenmingyan')
        elif mode == 15:
            pass
        elif mode == 16:
            pass
        elif mode == 17:
            pass
        elif mode == 18:
            pass
        elif mode == 19:
            resp = requests.get(f'https://v.api.aa1.cn/api/api-jupai/index.php?msg={msg}')
            with open('resource/little_people.jpg', 'wb') as f:
                f.write(resp.content)
            return 'success'
        elif mode == 20:
            resp = requests.get('https://v.api.aa1.cn/api/api-saohua/index.php?type=json')
            return eval(resp.text).get('saohua')
        elif mode == 21:
            resp = requests.get('https://zj.v.api.aa1.cn/api/wenan-gaoxiao/?type=json')
            return eval(resp.text).get('msg')
        elif mode == 22:
            resp = requests.get('https://zj.v.api.aa1.cn/api/wenan-wm/?type=json')
            return eval(resp.text).get('msg')
        elif mode == 23:
            resp = requests.get('https://zj.v.api.aa1.cn/api/wenan-pp/?type=json')
            return eval(resp.text).get('msg')


if __name__ == '__main__':
    joker = Joker()
    result = joker.freeApi(mode=22, qq=524276169)
    print(result)
    # print(joker.__doc__)
