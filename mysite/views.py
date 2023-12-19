from django.shortcuts import render, redirect
from mysite import models
from mysite.templates.login_check import is_empty2, is_correct
from mysite.templates.register_check import is_empty3, is_different, is_existed, add_user
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
from django.db.models import F, Count

def collection(request):
    """收藏"""
    if request.session.get('username') == None:
        return redirect('/login/?warning=1')
    user_name = request.session.get('username')
    user_id = int(models.userinfo.objects.filter(username=user_name).get().id)
    combined_data = models.self_collection.objects.filter(collector_id=user_id).order_by('id')
    return render(request, 'collection.html', {'collection': combined_data})

def home(request):
    """主页"""
    username = None
    team_set = models.teaminfo.objects.all()
    user_list = models.userinfo.objects.all()
    if request.session.get('username') is not None:
        username = request.session.get('username')
    if username is None:
        return render(request, 'home_1.html', {'username': username, 'team_set': team_set, 'user_list': user_list})
    if username is not None:
        user_info = models.userinfo.objects.filter(username=username).get()
        team_id = user_info.team_id
    if team_id is not None:
        cts_set = models.contest.objects.all()
        return render(request, 'home_old.html', {'user_info': user_info, 'cts_set': cts_set, 'team_set': team_set, 'user_list': user_list})
    else:
        return render(request, 'home_1.html', {'username': username, 'team_set': team_set, 'user_list': user_list})

def index(request):
    """"""
    return render(request, 'index.html')

def login(request):
    """登陆界面"""
    print("in", request.method)
    if request.method == 'GET':
        if request.GET.get("warning"):
            login_message = "请先登录"
            return render(request, 'login.html', {"message": login_message})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if is_empty2(username, password):
            login_message = "账号和密码均不能为空"
            print("empty")
            return render(request, 'login.html', {"message": login_message})
        elif is_correct(username, password):
            print("corr")
            request.session['username'] = username  # 登陆成功
            return redirect('/home')
        elif not is_existed(username):
            login_message = "不存在该用户"
            return render(request, 'login.html', {"message": login_message})
        else:
            login_message = "密码错误"
            return render(request, 'login.html', {"message": login_message})
    else:
        return render(request, 'login.html')


def problem(request):
    """题目界面"""
    if request.session.get('username') == None:
        return redirect('/login/?warning=1')
    pro_set = models.question.objects.all()
    pro_col = []
    for i in range(models.question.objects.count()):
        pro_col.append(0)
    user_info = models.userinfo.objects.filter(username=request.session.get("username")).get()
    col_list = models.problem_collected.objects.filter(collector_id=user_info.id)
    for obj in col_list:
        pro_col[obj.collection_id - 1] = 1
    pro_set = zip(pro_set, pro_col)
    return render(request, 'problem_1.html', {'pro_set': pro_set})

def register(request):
    """注册界面"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        selfinstruction = request.POST.get('instruction')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        major = request.POST.get('major')
        qq = request.POST.get('qq')
        blog = request.POST.get('blog')
        github = request.POST.get('github')
        mail = request.POST.get('mail')
        if is_empty3(username, password1, password2):
            login_massage = "账号和密码均不能为空"
            return render(request, 'register.html', {"message": login_massage})
        elif is_different(password1, password2):
            login_massage = "两次输入的密码不符"
            return render(request, 'register.html', {"message": login_massage})
        elif is_existed(username):
            login_massage = "用户名已存在"
            return render(request, 'register.html', {"message": login_massage})
        else:
            models.userinfo.objects.create(username=username, password=password1, name=name,
                                           selfintroduction=selfinstruction, gender=gender,
                                           age=age, major=major, qq=qq, github=github, mail=mail, blog=blog)
            return render(request, 'login.html')
    return render(request, 'register.html')

def feedback(request):
    """反馈页面"""
    if request.session.get('username') == None:
        return redirect('/login/?warning=1')
    return render(request, 'feedback.html')

def discussion(request):
    """讨论区"""
    if request.session.get('username') == None:
        return redirect('/login/?warning=1')
    user_name = request.session.get('username')
    contest_id = int(request.GET.get('id'))
    user_id = int(models.userinfo.objects.filter(username=user_name).get().id)
    if request.method == 'GET':
        dis_set = models.discussion_contest.objects.filter(discussionCon=contest_id).order_by('-id').select_related("owner")
        return render(request, 'discussion.html', {'dis_set': dis_set, 'contest_id': contest_id, 'username':user_name})
    if request.method == 'POST':
        flag = request.POST.get('formType')
        if flag == 'noresponse':
            new_content = request.POST.get('content')
            response_id = request.POST.get('')
            models.discussion_contest.objects.create(discussionCon=models.contest.objects.get(id=contest_id),
                                         Contents=new_content,
                                         owner=models.userinfo.objects.get(id=user_id),
                                         response=None)
            dis_set = models.discussion_contest.objects.filter(discussionCon=contest_id).order_by('-id').select_related("owner")
            return render(request, 'discussion.html', {'dis_set': dis_set, 'contest_id': contest_id, 'username':user_name})
        else:
            new_content = request.POST.get('content')
            response_id = request.POST.get('commentId')
            models.discussion_contest.objects.create(discussionCon=models.contest.objects.get(id=contest_id),
                                             Contents=new_content,
                                             owner=models.userinfo.objects.get(id=user_id),
                                             response=models.discussion_contest.objects.get(id=response_id))
            dis_set = models.discussion_contest.objects.filter(discussionCon=contest_id).order_by('-id').select_related("owner")
            return render(request, 'discussion.html', {'dis_set': dis_set, 'contest_id': contest_id, 'username':user_name})

def user_homepage(request, username = None):
    """用户主页"""
    if username==None and request.session.get('username') is not None: # for oneself
        return redirect('/user_homepage/'+request.session.get('username'))
    user_info = models.userinfo.objects.filter(username=username).get()
    team_num = 10
    pro_col = models.self_collection.objects.filter(collector_id=user_info.id)
    dis_set = models.discussion_contest.objects.filter(owner=user_info.id)
    print('team_id:', user_info.team_id)
    if user_info.team_id == None:
        team_info = None
    else:
        team_info = models.teaminfo.objects.filter(id=user_info.team_id).get()
    return render(request, 'my_homepage.html', {'user_info': user_info, 'team_info': team_info,
                                                'team_num': team_num,'pro_col':pro_col,
                                                'dis_set': dis_set,} )

def logout(request):
    """清空session"""
    request.session.flush()
    return redirect('/home/')

def users(request):
    """用户排名展示"""
    combined_data = models.userinfo.objects.select_related('team').order_by('id')
    return render(request, 'user_ranking.html', {'user_info': combined_data})

def teams(request):
    """队伍排名展示"""
    teaminfo = models.teaminfo.objects.all().order_by('-score')
    return render(request, 'team_ranking.html', {'team_info': teaminfo})

def add(request):
    """添加信息"""
    return render(request, "home.html")

# @method_decorator(never_cache, name='dispatch')
def favorite(request):
    """收藏题目"""
    pro_id = request.POST.get('pro_id')
    user_info = models.userinfo.objects.filter(username=request.session.get("username")).get()
    models.problem_collected.objects.create(collector_id=user_info.id
                                            , collection_id=pro_id)
    return redirect("/problem")

def unfavorite(request):
    """取消收藏"""
    pro_id = request.POST.get('pro_id')
    user_info = models.userinfo.objects.filter(username=request.session.get("username")).get()
    record = models.problem_collected.objects.get(collector_id=user_info.id
                                            , collection_id=pro_id)
    record.delete()
    return redirect("/problem")

def post_info(request):
    """上传信息"""
    user_name = request.session.get('username')
    user_id = int(models.userinfo.objects.filter(username=user_name).get().id)
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    major = request.POST.get('major')
    qq = request.POST.get('qq')
    github = request.POST.get('github')
    blog = request.POST.get('blog')
    mail = request.POST.get('mail')
    item = models.userinfo.objects.get(id=user_id)
    item.name = name
    item.gender = gender
    item.age = age
    item.major = major
    item.qq = qq
    item.github = github
    item.mail = mail
    item.blog = blog
    item.save()
    return redirect('/user_homepage')

def post_intro(request):
    """上传自我介绍"""
    user_name = request.session.get('username')
    user_id = int(models.userinfo.objects.filter(username=user_name).get().id)
    introduction = request.POST.get('self_introduction')
    item = models.userinfo.objects.get(id=user_id)
    item.selfintroduction = introduction
    item.save()
    return redirect('/user_homepage')

def contest(request):
    """比赛界面"""
    if request.session.get('username') == None:
        return redirect('/login/?warning=1')
    cts_set = models.contest.objects.all()
    return render(request, 'contest.html',{'cts_set': cts_set})

def contest_add(request):
    """添加比赛"""
    if request.session.get('username') == None:
        return redirect('/login/?warning=1')
    if request.method == "GET":
        return render(request, 'contest_add.html')
    # 获取用户POST提交过来的数据（title输入为空）
    name = request.POST.get('name')
    date = request.POST.get('date')
    site = request.POST.get('site')
    statement = request.POST.get('statement')
    solution = request.POST.get('solution')
    scoreboard = request.POST.get('scoreboard')

    # 保存到数据库
    models.contest.objects.create(name=name, date=date, site=site,
                                   statement=statement, solution=solution,
                                   scoreboard=scoreboard)

    # 重定向回部门列表
    return redirect("/contest/")

def contest_delete(request):
    """ 删除部门 """
    # 获取ID http://127.0.0.1:8000/depart/delete/?nid=1
    nid = request.GET.get('nid')

    # 删除
    models.contest.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/contest/")

def contest_edit(request, nid):
    """ 修改部门 """
    if request.method == "GET":
        # 根据nid，获取他的数据 [obj,]
        row_object = models.contest.objects.filter(id=nid).first()
        return render(request, 'contest_edit.html', {"row_object": row_object})

    # 获取用户提交的标题
    name = request.POST.get('name')
    date = request.POST.get('date')
    site = request.POST.get('site')
    statement = request.POST.get('statement')
    solution = request.POST.get('solution')
    scoreboard = request.POST.get('scoreboard')

    # 根据ID找到数据库中的数据并进行更新
    models.contest.objects.filter(id=nid).update(name=name, date=date, site=site,
                                   statement=statement, solution=solution,
                                   scoreboard=scoreboard)
    # models.Department.objects.filter(id=nid).update(title=title,其他=123)
    #models.Department.objects.filter(id=nid).update(title=title)

    # 重定向回部门列表
    return redirect("/contest/")

def application(request):
    """选拔报名"""
    if request.session.get('username') == None:
        return redirect('/login/?warning=1')
    username = request.session.get('username')
    user_info = models.userinfo.objects.filter(username=username).get()
    selection_info = models.submission.objects.filter(user_id=user_info.id)
    flag = []
    flagg = []
    for i in range(100):
        flag.append(0)
    for obj in selection_info:
        flag[obj.selection_id] = 1
    selection = models.selection.objects.all().order_by('-id')
    for obj in selection:
        if flag[obj.id] == 1:
            flagg.append(1)
        else:
            flagg.append(0)
    selection = zip(selection, flagg)
    return render(request, "application.html", {"selection": selection, "user_info": user_info, "flag": flag})

def application_add(request):
    """添加选拔赛"""
    if request.session.get('username') == None:
        return redirect('/login/?warning=1')
    if request.method == "GET":
        return render(request, 'application_add.html')
    # 获取用户POST提交过来的数据（title输入为空）
    name = request.POST.get('name')
    sign_d1 = request.POST.get('sign_d1')
    sign_d2 = request.POST.get('sign_d2')
    select_d1 = request.POST.get('select_d1')
    select_d2 = request.POST.get('select_d2')
    need = request.POST.get('need')

    # 保存到数据库
    models.selection.objects.create(name=name, sign_d1=sign_d1, sign_d2=sign_d2,
                                   select_d1=select_d1, select_d2=select_d2,
                                   need=need, able=1)

    # 重定向回部门列表
    return redirect("/application/")

def application_delete(request):
    """ 删除部门 """
    nid = request.GET.get('nid')

    models.selection.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/application/")

def application_edit(request, nid):
    """ 修改部门 """
    if request.method == "GET":
        # 根据nid，获取他的数据 [obj,]
        row_object = models.selection.objects.filter(id=nid).first()
        return render(request, 'application_edit.html', {"row_object": row_object})

    # 获取用户提交的标题
    name = request.POST.get('name')
    sign_d1 = request.POST.get('sign_d1')
    sign_d2 = request.POST.get('sign_d2')
    select_d1 = request.POST.get('select_d1')
    select_d2 = request.POST.get('select_d2')
    need = request.POST.get('need')
    able = request.POST.get('able')

    # 根据ID找到数据库中的数据并进行更新
    models.selection.objects.filter(id=nid).update(name=name, sign_d1=sign_d1, sign_d2=sign_d2,
                                   select_d1=select_d1, select_d2=select_d2,
                                   need=need, able= able)
    # models.Department.objects.filter(id=nid).update(title=title,其他=123)
    #models.Department.objects.filter(id=nid).update(title=title)

    # 重定向回部门列表
    return redirect("/application/")

def application_submission(request):
    select_id = request.GET.get("id")
    username = request.session.get('username')
    user_info = models.userinfo.objects.filter(username=username).get()
    models.submission.objects.create(selection_id=select_id, user_id=user_info.id)
    return redirect("/application/")

def submission_list(request):
    select_id = request.GET.get("id")
    select_list = models.submission.objects.filter(selection_id=select_id)
    selection_info = models.selection.objects.filter(id=select_id).get()
    return render(request, 'submission_list.html', {"select_list": select_list, "selection_info": selection_info})

def question_add(request):
    """添加收藏题目"""
    if request.session.get('username') == None:
        return redirect('/login/?warning=1')
    user_name = request.session.get('username')
    user_id = int(models.userinfo.objects.filter(username=user_name).get().id)
    if request.method == "GET":
        return render(request, 'question_add.html')
    # 获取用户POST提交过来的数据（title输入为空）
    collector = user_id
    name = request.POST.get('name')
    url = request.POST.get('url')
    solution = request.POST.get('solution')
    difficulty = request.POST.get('difficulty')
    tag = request.POST.get('tag')
    source = request.POST.get('source')

    # 保存到数据库
    models.self_collection.objects.create(collector_id=user_id, name=name, url=url,
                                          solution=solution,difficulty=difficulty,
                                          tag=tag,source=source)

    # 重定向回部门列表
    return redirect("/collection/")

def question_delete(request):
    """ 删除收藏题目 """
    nid = request.GET.get('nid')

    models.self_collection.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/collection/")

def question_edit(request, nid):
    """ 修改收藏题目 """
    if request.method == "GET":
        row_object = models.self_collection.objects.filter(id=nid).first()
        return render(request, 'question_edit.html', {"row_object": row_object})

    # 获取用户提交的标题
    name = request.POST.get('name')
    url = request.POST.get('url')
    solution = request.POST.get('solution')
    difficulty = request.POST.get('difficulty')
    tag = request.POST.get('tag')
    source = request.POST.get('source')

    # 根据ID找到数据库中的数据并进行更新
    models.self_collection.objects.filter(id=nid).update( name=name, url=url,
                                          solution=solution,difficulty=difficulty,
                                          tag=tag,source=source)
    # models.Department.objects.filter(id=nid).update(title=title,其他=123)
    #models.Department.objects.filter(id=nid).update(title=title)

    # 重定向回部门列表
    return redirect("/collection/")

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

    rows = models.teaminfo.objects.order_by('-score')

    # 使用 enumerate 为每一行分配一个排名，并更新 rank 属性
    for index, row in enumerate(rows):
        row.rank = index + 1
        row.save()
    return redirect("/home/")

