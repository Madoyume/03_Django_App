from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Message,Good
from .forms import PostForm

# indexビュー関数
@login_required(login_url='admin/login/')
def index(request, page=1):
    # ページ当たりの表示数
    max = 10
    form = PostForm(request.user)
    msgs = Message.objects.all()
    # ページネーションで指定ページを取得
    paginate = Paginator(msgs, max)
    page_items = paginate.get_page(page)
    
    params = {
        'login_user':request.user,
        'form':form,
        'content':page_items,
    }
    return render(request, 'sns/index.html', params)

# goodsビュー関数
@login_required(login_url='admin/login/')
def goods(request):
    goods = Good.objects.filter(owner=request.user).all()
    
    params = {
        'login_user':request.user,
        'contents':goods,
    }
    return render(request, 'sns/good.html', params)

# メッセージのポスト処理
@login_required(login_url='admin/login/')
def post(request):
    # POST送信の処理
    if request.method == 'POST':
        #送信内容の取得
        content = request.POST['content']
        # Messageを作成し設定して保存
        msg = Message()
        msg.owner = request.user
        msg.content = content
        msg.save()
        return redirect(to='/sns/')
    else:
        messages = Message.objects.filter(owner=request.user).all()
        params = {
            'login_user':request.user,
            'content':messages,
        }
        return render(request, 'sns/post.html', params)

# goodボタンの処理
@login_required(login_url='admin/login/')
def good(request, good_id):
    # goodするメッセージを取得
    good_msg = Message.objects.get(id=good_id)
    # 自分がメッセージにGoodした数を調べる
    is_good = Good.objects.filter(owner=request.user) \
        .filter(message=good_msg).count()
    # ゼロより多ければ既にgood済み
    if is_good > 0:
        messages.success(request, '既にメッセージをGoodしています。')
        return redirect(to='/sns')
    
    # Messageのgood_countを1増やす
    good_msg.good_count += 1
    good_msg.save()
    # Goodを作成し、設定して保存
    good = Good()
    good.owner = request.user
    good.message = good_msg
    good.save()
    # メッセージを設定
    messages.success(request, 'メッセージにGoodしました！')
    return redirect(to='/sns')
