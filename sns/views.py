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
    search = request.GET.get('search')
    #검색
    if search != None:
        question_list = question_list.filter(content__icontains=search)
    # 페이지당 10개씩 보여주기
    paginator = Paginator(question_list, 10)
    # 페이지 , url에 ?page=1 추가해서 보여주기
    page = request.GET.get('page', '1')
    # 객체 생성
    page_obj = paginator.get_page(page)

    return render(request, 'sns/index.html', {'file_list': filenames,
                                                  'question_list': page_obj, 'search': search})

#게시글 내용
def contents(request, content_id):
    question = get_object_or_404(Question, pk=content_id)
    question.click()
    return render(request, 'sns/content.html', {'question': question, 'file_list': filenames})

#댓글 기능
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user.is_authenticated:
        answer = Answer(question=question, content=request.POST['content'], name=request.user.username,
                        create_date=timezone.now(), an_password='1234')
    else:
        answer = Answer(question=question, content=request.POST['content'], name=request.POST['name'],
                    create_date=timezone.now(), an_password=request.POST['password'])
    answer.save()
    #redirect 와 render의 차이는 redirect 는 링크로 이동시켜주고 render은 html파일을 열어준다.
    return redirect('sns:contents', content_id=question.id)

#글쓰기 기능
def sns_create(request):
    #작성확인 버튼 누를시
    if request.method == 'POST':
        #로그인 확인
        if request.user.is_authenticated:
            paw, name = '1234', request.user.username
        else:
            paw, name = request.POST['su_password'], request.POST['name']
        question = Question(create_date= timezone.now(),
                            content=request.POST['content'],
                            name=name,
                            su_password=paw,
                            subject=request.POST['subject'],
                            clik_num=0,
                            #암호화 해서 저장하지 않으면 해킹에 취약할 수 있음
                            user_name=request.user.username
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
        #유저확인
        if request.user.username == question.user_name:
            if request.method == 'POST':
                if request.user.is_authenticated or question.su_password == request.POST['su_password']:
                    question.content=request.POST['content']
                    question.subject=request.POST['subject']
                    question.create_date= timezone.now()
                    question.save()
                    return render(request, 'sns/content.html', {'question': question})
            else:
                #폼에 초기값 삽입
                form = QuestionForm(initial={'content': question.content})
                return render(request, 'sns/sns_create_revise.html', {'question': question,
                                                                      'file_list': filenames, 'form': form})
        #에러창 만들어야함
        return redirect('sns:index')
#글삭제 기능
def dl(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #로그인되어있는 경우 자기 게시물이 맞다면 삭제
    if request.user.is_authenticated and request.user.username == question.user_name:
        question.delete()
        return redirect('sns:index')

    #비밀번호 확인
    if request.method == 'POST':
        #로그인 안되어있는 경우
        try:
            if request.user.is_authenticated or question.su_password == request.POST['su_password']:
                question.delete()
                return redirect('sns:index')
        except:
            return render(request, 'sns/sns_create_del_erorr.html', {'question': question, 'file_list': filenames})

    #로그인 아닐경우 비밀번호 확인
    else:
        if request.user.username == question.user_name:
            return render(request, 'sns/sns_create_del.html', {'question': question, 'file_list': filenames})
        else:
            return render(request, 'sns/sns_create_del_erorr.html', {'question': question, 'file_list': filenames})