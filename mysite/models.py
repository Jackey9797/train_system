from django.db import models

class teaminfo(models.Model):
    """队伍信息表"""
    teamname = models.CharField(verbose_name="队伍名字", max_length=45)

    score = models.FloatField(verbose_name="队伍分数", null=True, blank=True, default=0)
    rank = models.IntegerField(verbose_name="队伍排名", null=True, blank=True)

    score1 = models.FloatField(verbose_name="比赛1", null=True, blank=True, default=0)
    score2 = models.FloatField(verbose_name="比赛2", null=True, blank=True, default=0)
    score3 = models.FloatField(verbose_name="比赛3", null=True, blank=True, default=0)
    score4 = models.FloatField(verbose_name="比赛4", null=True, blank=True, default=0)
    score5 = models.FloatField(verbose_name="比赛5", null=True, blank=True, default=0)
    score6 = models.FloatField(verbose_name="比赛6", null=True, blank=True, default=0)
    score7 = models.FloatField(verbose_name="比赛7", null=True, blank=True, default=0)
    score8 = models.FloatField(verbose_name="比赛8", null=True, blank=True, default=0)
    score9 = models.FloatField(verbose_name="比赛9", null=True, blank=True, default=0)
    score10 = models.FloatField(verbose_name="比赛10", null=True, blank=True, default=0)

    class Meta:
        #db_table = 'track'
        ordering = ('-score','id')

class userinfo(models.Model):
    """用户信息表"""
    username = models.CharField(verbose_name="用户名", max_length=14)
    password = models.CharField(verbose_name="用户密码", max_length=25)
    name = models.CharField(verbose_name="姓名", max_length=14)
    selfintroduction = models.TextField(verbose_name="自我介绍", null=True, blank=True)
    avatar = models.ImageField(verbose_name="头像", blank=True, null=True)
    solved_problem = models.IntegerField(verbose_name="通过题目数", null=True, blank=True, default=0)
    is_admin = models.IntegerField(verbose_name="是否为管理员", default=0)
    team = models.ForeignKey(to="teaminfo", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    ranknum = models.IntegerField(verbose_name='排名', null=True, blank=True)
    qq = models.CharField(verbose_name='qq', max_length=13, null=True, blank=True)
    gender = models.CharField(verbose_name='性别', max_length=11)
    age = models.CharField(verbose_name='年龄', max_length=12)
    major = models.CharField(verbose_name='专业', max_length=12)
    github = models.CharField(verbose_name='github主页', max_length=120, null=True, blank=True)
    blog = models.CharField(verbose_name='博客主页', max_length=120, null=True, blank=True)
    mail = models.CharField(verbose_name='邮箱地址', max_length=120, null=True, blank=True)


class question(models.Model):
    """题目信息表"""
    name = models.CharField(verbose_name="题目名称", max_length=45)
    statement = models.TextField(verbose_name="题目描述")
    background = models.CharField(verbose_name="题目背景", max_length=45)
    solution = models.TextField(verbose_name="题解")

    difficulty = models.FloatField(verbose_name="题目难度", null=True, blank=True)
    tag = models.CharField(verbose_name="题目标签", max_length=100, null=True, blank=True)
    source = models.CharField(verbose_name="来源", max_length=100, null=True, blank=True)

class discussion(models.Model):
    """讨论区"""
    discussionPr = models.ForeignKey(verbose_name="题目id", to="question", to_field="id", on_delete=models.CASCADE)
    Contents = models.TextField(verbose_name="讨论区内容")
    owner = models.ForeignKey(verbose_name="用户id", to="userinfo", to_field="id", on_delete=models.CASCADE)
    response = models.ForeignKey(verbose_name="回复的讨论区id", to="discussion", to_field="id", null=True, blank=True, on_delete=models.CASCADE)


class problem_solved(models.Model):
    """通过题目"""
    solver = models.ForeignKey(to="userinfo", to_field="id", on_delete=models.CASCADE)
    solved = models.ForeignKey(to="question", to_field="id", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='题目名字', max_length=45)

class problem_collected(models.Model):
    """收藏题目"""
    collector = models.ForeignKey(to="userinfo", to_field="id", on_delete=models.CASCADE)
    collection = models.ForeignKey(to="question", to_field="id", on_delete=models.CASCADE)

class contest(models.Model):
    """比赛信息表"""
    name = models.CharField(verbose_name="比赛名称", max_length=100)
    date = models.TextField(verbose_name="日期")
    site = models.TextField(verbose_name="参赛链接")
    statement = models.TextField(verbose_name="题面")
    solution = models.TextField(verbose_name="题解")
    scoreboard = models.TextField(verbose_name="排行榜")

class selection(models.Model):
    """选拔表"""
    name = models.CharField(verbose_name='选拔名称', max_length=100)
    sign_d1 = models.TextField(verbose_name='报名开始日期')
    sign_d2 = models.TextField(verbose_name='报名结束日期')
    select_d1 = models.TextField(verbose_name='选拔开始时间')
    select_d2 = models.TextField(verbose_name='选拔结束时间')
    need = models.IntegerField(verbose_name='选拔人数')
    able = models.IntegerField(verbose_name='是否可用', default=0)

class submission(models.Model):
    selection_id = models.IntegerField(verbose_name='选拔id')
    user = models.ForeignKey(verbose_name='报名人id', to="userinfo", to_field="id", on_delete=models.CASCADE)

class self_collection(models.Model):
    """个人收藏题目"""
    collector = models.ForeignKey(to="userinfo", to_field="id", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="题目名", max_length=45)
    url = models.TextField(verbose_name="题目链接")
    solution = models.TextField(verbose_name="题解链接")
    difficulty = models.FloatField(verbose_name="题目难度", null=True, blank=True)
    tag = models.CharField(verbose_name="题目标签", max_length=100, null=True, blank=True)
    source = models.CharField(verbose_name="来源", max_length=100, null=True, blank=True)

class discussion_contest(models.Model):
    """比赛讨论区"""
    discussionCon = models.ForeignKey(verbose_name="比赛id", to="contest", to_field="id", on_delete=models.CASCADE)
    Contents = models.TextField(verbose_name="讨论区内容")
    owner = models.ForeignKey(verbose_name="用户id", to="userinfo", to_field="id", on_delete=models.CASCADE)
    response = models.ForeignKey(verbose_name="回复的讨论区id", to="discussion_contest", to_field="id", null=True, blank=True,
                                 on_delete=models.CASCADE)