models
``````

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

``````

views
```

def rating(request):
    """比赛界面"""
    # if 'username' in session:
    #     username = session['username']
    #     return render_template("problem.html", username=username)
    # else:
    #     return render_template("login.html")
    #models.teaminfo.objects.all().delete()
    #models.teaminfo.objects.create(id=1,teamname="1", score="0")
    '''
    models.teaminfo.objects.create(id=1,teamname="难题肉搏小队",score="0")
    models.teaminfo.objects.create(id=2,teamname="刀削面的疲倦",score="0")
    models.teaminfo.objects.create(id=3,teamname="树上莫队", score="0")
    models.teaminfo.objects.create(id=4,teamname="帮帮我，icpc先生！", score="0")
    models.teaminfo.objects.create(id=5,teamname="此访问越界", score="0")
    models.teaminfo.objects.create(id=6,teamname="麦香鱼", score="0")
    models.teaminfo.objects.create(id=7,teamname="纹化输出自动鸡", score="0")
    models.teaminfo.objects.create(id=8,teamname="晚十208", score="0")
    models.teaminfo.objects.create(id=9,teamname="这也能队", score="0")
    '''
    #models.teaminfo.objects.all().order_by('-score')
    team_set = models.teaminfo.objects.all()
    return render(request, 'rating.html',{'team_set': team_set})

def rating_edit(request, nid):
    """ 修改部门 """
    if request.method == "GET":
        # 根据nid，获取他的数据 [obj,]
        row_object = models.teaminfo.objects.filter(id=nid).first()
        return render(request, 'rating_edit.html', {"row_object": row_object})

    # 获取用户提交的标题
    score1 = float(request.POST.get('score1'))
    score2 = float(request.POST.get('score2'))
    score3 = float(request.POST.get('score3'))
    score4 = float(request.POST.get('score4'))
    score5 = float(request.POST.get('score5'))
    score6 = float(request.POST.get('score6'))
    score7 = float(request.POST.get('score7'))
    score8 = float(request.POST.get('score8'))
    score9 = float(request.POST.get('score9'))
    score10 =float(request.POST.get('score10'))
    total=(float)(score1+score2+score3+score4+score5+score6+score7+score8+score9+score10)

    # 根据ID找到数据库中的数据并进行更新
    models.teaminfo.objects.filter(id=nid).update(score1 =score1,score2 =score2,score3 =score3,score4 =score4,score5 =score5,
                                                  score6 =score6,score7 =score7,score8 =score8,score9 =score9,score10 =score10,score=total)
    # Retrieve the players ranked by their scores
    ranked_players = Player.objects.all().order_by('-score')

    # Add ranking to the queryset using annotate()
    ranked_players_with_rank = (
        models.teaminfo.objects.all().extra(select={'rank': 'RANK() OVER (ORDER BY score DESC)'})
    )
    #models.teaminfo.objects.all().order_by('-score')
    # models.Department.objects.filter(id=nid).update(title=title,其他=123)
    #models.Department.objects.filter(id=nid).update(title=title)

    # 重定向回部门列表
    return redirect("/rating/")

```

url
```
    path('rating/', views.rating),
    path('rating/<int:nid>/edit/', views.rating_edit),
```