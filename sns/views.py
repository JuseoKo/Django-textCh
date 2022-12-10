from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm
from trans.views import pj_name_load
#페이징
from django.core.paginator import Paginator
filenames = pj_name_load()

#게시글 목록
def index(request):
    question_list = Question.objects.order_by('-create_date')
    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

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

#답글 기능
def answer_create(request, question_id):
    #에러메세지 설정
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST['content'], name=request.POST['name'],
                    create_date=timezone.now())
    answer.save()
    #redirect 와 render의 차이는 redirect 는 링크로 이동시켜주고 render은 html파일을 열어준다.
    return redirect('sns:contents', content_id=question.id)

#글쓰기 기능
def sns_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('sns:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'sns/sns_create.html', context)