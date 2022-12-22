from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm
from trans.views import pj_name_load
#페이징
from django.core.paginator import Paginator

from django.db.models import Max
filenames = pj_name_load()

#게시글 목록
def index(request):
    question_list = Question.objects.order_by('-create_date')

    page = request.GET.get('page', '1')  # 페이지 , url에 ?page=1 추가해서 보여주기
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page) # 객체 생성

    return render(request, 'sns/index.html', {'file_list': filenames,
                                              'question_list': page_obj})

#게시글 내용
def contents(request, content_id):
    question = get_object_or_404(Question, pk=content_id)
    question.click()
    #조회수
    # question.clik_num += 1
    # question.save()
    return render(request, 'sns/content.html', {'question': question, 'file_list': filenames})

#댓글 기능
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST['content'], name=request.POST['name'],
                    create_date=timezone.now(), an_password=request.POST['password'])
    answer.save()
    #redirect 와 render의 차이는 redirect 는 링크로 이동시켜주고 render은 html파일을 열어준다.
    return redirect('sns:contents', content_id=question.id)

#글쓰기 기능
def sns_create(request):
    #작성확인 버튼 누를시
    if request.method == 'POST':
        print(request.POST)
        question = Question(con_num=int(list(Question.objects.aggregate(Max('con_num')).values())[0]) + 1,
                            create_date= timezone.now(),
                            content=request.POST['content'],
                            name=request.POST['name'],
                            su_password=request.POST['su_password'],
                            subject=request.POST['subject'],
                            clik_num=0
                            )
        question.save()
        return redirect('sns:index')
    #페이지 오픈시
    else:
        form = QuestionForm()
    return render(request, 'sns/sns_create.html', {'form': form, 'file_list': filenames})

#글 수정 기능
def revise(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        if question.su_password == request.POST['password']:
            question.subject = request.POST['subject']
            question.name = request.POST['name']
            question.content = request.POST['content']
            question.create_date = timezone.now()
            question.save()
            return render(request, 'sns/content.html', {'question': question})
        else:
            return redirect('sns:erorr')
    else:
        return render(request, 'sns/sns_create_revise.html', {'question': question, 'file_list': filenames})

def dl(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        if question.su_password == request.POST['password']:
            question.delete()
            return redirect('sns:index')
        else:
            return redirect('sns:erorr')
    else:
        return render(request, 'sns/sns_create_del.html', {'question': question, 'file_list': filenames})

def erorr(request):
    if request.method == 'POST':
        return redirect('sns:index')
    return render(request, 'sns/sns_create_del_erorr.html', {'file_list': filenames})