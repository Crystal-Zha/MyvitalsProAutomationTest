import random


class CommonFun:


    '''
    1.获取随机的邮箱
    '''
    def random_email(emailType=None, rang=None):
        __emailtype = ["@gmail.com", "@163.com", "@126.com", "@189.com"]
        # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
        if emailType is None:
            __randomEmail = random.choice(__emailtype)
        else:
            __randomEmail = emailType
        # 如果没有指定邮箱长度，默认在4-10之间随机
        if rang is None:
            __rang = random.randint(4, 10)
        else:
            __rang = int(rang)
        # __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        __Number = "0123456789"
        __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
        _email = __randomNumber + __randomEmail
        return _email
    email = random_email()

