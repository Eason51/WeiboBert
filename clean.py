import json
import re
from weibo_preprocess_toolkit import WeiboPreprocess
#from settings import *

replace_dict = {
    u'吻腚':u'稳定',
    u'弓虽':u'强',
    u'女干':u'奸',
    u'示土':u'社',
    u'禾口':u'和',
    u'言皆':u'谐',
    u'释永性':u'释永信',
    u'大菊观':u'大局观',
    u'yl':u'一楼',
    u'cnm':u'草泥马',
    u'CCTV':u'中央电视台',
    u'CCAV':u'中央电视台',
    u'ccav':u'中央电视台',
    u'cctv':u'中央电视台',
    u'qq':u'腾讯聊天账号',
    u'QQ':u'腾讯聊天账号',
    u'cctv':u'中央电视台',
    u'CEO':u'首席执行官',
    u'克宫':u'克里姆林宫',
    u'PM2.5':u'细颗粒物',
    u'pm2.5':u'细颗粒物',
    u'SDR':u'特别提款权',
    u'装13':u'装逼',
    u'213':u'二逼',
    u'13亿':u'十三亿',
    u'巭':u'功夫',
    u'孬':u'不好',
    u'嫑':u'不要',
    u'夯':u'大力',
    u'芘':u'操逼',
    u'烎':u'开火',
    u'菌堆':u'军队',
    u'sb':u'傻逼',
    u'SB':u'傻逼',
    u'Sb':u'傻逼',
    u'sB':u'傻逼',
    u'is':u'伊斯兰国',
    u'isis':u'伊斯兰国',
    u'ISIS':u'伊斯兰国',
    u'ko':u'打晕',
    u'你M':u'你妹',
    u'你m':u'你妹',
    u'震精':u'震惊',
    u'返工分子':u'反共',
    u'黄皮鹅狗':u'黄皮肤俄罗斯狗腿',
    u'苏祸姨':u'苏霍伊',
    u'混球屎报':u'环球时报',
    u'屎报':u'时报',
    u'jb':u'鸡巴',
    u'j巴':u'鸡巴',
    u'j8':u'鸡巴',
    u'J8':u'鸡巴',
    u'JB':u'鸡巴',
    u'瞎BB':u'瞎说',
    u'nb':u'牛逼',
    u'牛b':u'牛逼',
    u'牛B':u'牛逼',
    u'牛bi':u'牛逼',
    u'牛掰':u'牛逼',
    u'苏24':u'苏两四',
    u'苏27':u'苏两七',
    u'痰腐集团':u'贪腐集团',
    u'痰腐':u'贪腐',
    u'反hua':u'反华',
    u'<br>':u' ',
    u'屋猫':u'五毛',
    u'5毛':u'五毛',
    u'傻大姆':u'萨达姆',
    u'霉狗':u'美狗',
    u'TMD':u'他妈的',
    u'tmd':u'他妈的',
    u'japan':u'日本',
    u'P民':u'屁民',
    u'八离开烩':u'巴黎开会',
    u'傻比':u'傻逼',
    u'潶鬼':u'黑鬼',
    u'cao':u'操',
    u'爱龟':u'爱国',
    u'天草':u'天朝',
    u'灰机':u'飞机',
    u'张将军':u'张召忠',
    u'大裤衩':u'中央电视台总部大楼',
    u'枪毕':u'枪毙',
    u'环球屎报':u'环球时报',
    u'环球屎包':u'环球时报',
    u'混球报':u'环球时报',
    u'还球时报':u'环球时报',
    u'人X日报':u'人民日报',
    u'人x日报':u'人民日报',
    u'清只县':u'清知县',
    u'PM值':u'颗粒物值',
    u'TM':u'他妈',
    u'首毒':u'首都',
    u'gdp':u'国内生产总值',
    u'GDP':u'国内生产总值',
    u'鸡的屁':u'国内生产总值',
    u'999':u'红十字会',
    u'霉里贱':u'美利坚',
    u'毛子':u'俄罗斯人',
    u'ZF':u'政府',
    u'zf':u'政府',
    u'蒸腐':u'政府',
    u'霉国':u'美国',
    u'狗熊':u'俄罗斯',
    u'恶罗斯':u'俄罗斯',
    u'我x':u'我操',
    u'x你妈':u'操你妈',
    u'p用':u'屁用',
    u'胎毒':u'台独',
    u'DT':u'蛋疼',
    u'dt':u'蛋疼',
    u'IT':u'信息技术',
    u'1楼':u'一楼',
    u'2楼':u'二楼',
    u'2逼':u'二逼',
    u'二b':u'二逼',
    u'二B':u'二逼',
    u'晚9':u'晚九',
    u'朝5':u'朝五',
    u'黄易':u'黄色网易',
    u'艹':u'操',
    u'滚下抬':u'滚下台',
    u'灵道':u'领导',
    u'煳':u'糊',
    u'跟贴被火星网友带走啦':u'',
    u'猿们':u'公务员们',
    u'棺猿':u'官员',
    u'贯猿':u'官员',
    u'每只猿':u'每个公务员',
    u'巢县':u'朝鲜',
    u'死大林':u'斯大林',
    u'无毛们':u'五毛们',
    u'天巢':u'天朝',
    u'普特勒':u'普京',
    u'依拉克':u'伊拉克',
    u'歼20':u'歼二零',
    u'歼10':u'歼十',
    u'歼8':u'歼八',
    u'f22':u'猛禽',
    u'p民':u'屁民',
    u'钟殃':u'中央',
    u'B站':u'哔哩哔哩',
    u'up主':u'博主',
    u'bilibili':u'哔哩哔哩',
    u'票圈':u'朋友圈',
    u'LOL':u'英雄联盟'
}

def filter_emoji(desstr, restr=''):
    # 过滤表情
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)

def filter_location(str):
    if '显示地图' in str:
        str_list = str.split(' ')
        leng = len(str_list)
        for i in range(leng):
            if str_list[i] == '显示地图':
                str = str.replace("显示地图", "")
                str = str.replace(str_list[i - 1], "")
                break

    return str.strip()

def clean(text):
    text = text.replace("抱歉，作者已设置仅展示半年内微博，此微博已不可见。 ", "")
    text = text.replace("抱歉，由于作者设置，你暂时没有这条微博的查看权限哦。查看帮助： 网页链接 ", "")
    text = text.replace("抱歉，此微博已被作者删除。查看帮助： 网页链接", "")
    text = text.replace("该账号因被投诉违反《微博社区公约》的相关规定，现已无法查看。查看帮助  网页链接", "")
    text = re.sub("\S+客户端下载", "", text)  # 去除"xxx客户端下载"
    text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text)  # 去除正文中的@和回复/转发中的用户名
    text = re.sub(r"\[\S+\]", "", text)  # 去除表情符号
    #text = re.sub("#\S+#", "", text)  # 去除话题内容
    text = re.sub("\S+的微博视频", "", text)  # 去除"xxx的微博视频"
    URL_REGEX = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
        re.IGNORECASE)
    text = re.sub(URL_REGEX, "", text)  # 去除网址
    text = text.replace("转发微博", "")  # 去除无意义的词语
    text = text.replace("分享图片", "")
    text = text.replace("网页链接", "")
    text = text.replace("查看图片", "")
    text = text.replace("#", "")
    text = filter_location(text)
    text = re.sub(r"\s+ ", " ", text)  # 合并正文中过多的空格
    #text = emoji.get_emoji_regexp().sub(r'', text)  # 去除emoji
    text = filter_emoji(text)
    text = re.sub(
        '[\001\002\003\004\005\006\007\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a]+',
        "", text)  # 去除不可见字符
    text = re.sub('[↓�⁍̴̛ᴗ•̫͡•ོʕʔ•͓͡ʔཻ︍︍︍]', '', text)
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace(r'\n', '')
    text = text.replace(r'\t', '')
    allpuncs = re.compile(
        r"[，\_《。》、？；：‘’＂“”【「】」、·！@￥…\|（）—\,\<\.\>\/\?\;\:\'\"\[\]\{\}\~\`\!\@\#\$\%\^\&\*\(\)\-\=\+～×\\]")
    text = re.sub(allpuncs, " ", text)
    text = WeiboPreprocess().traditional2simplified(text)  # 简体字转换
    return text.strip()


with open('D:\Documents\Babe\w\Tweets1_1.json', 'r', encoding='utf-8') as json_tweet:
    tweets=json.load(json_tweet)

a=0
for tweet in tweets:
    a=a+1
    print(a)
    tweet['text_own']=re.sub("//@.*", "", tweet['text'])
    tweet['pure_content'] = clean(tweet['text_own'])
    if "//@" in tweet['text']:
        tweet['text_other'] = '//@' + re.sub(".*?//@", "", tweet['text'], count=1)+' '
    else:
        tweet['text_other'] = ''
    if 'retweet' in tweet.keys():
        tweet['text_other']=tweet['text_other']+ tweet['retweet']['text']
        tweet['pure_origin_content'] = clean(tweet['text_other'])

json_str = json.dumps(tweets,indent=4,ensure_ascii=False)
with open('D:\Documents\Babe\w\Tweets1_1.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)
