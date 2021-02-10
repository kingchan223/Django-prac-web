from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import QuestionForm
# Create your views here.
def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'pybo/question_list.html',context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)#모델데이터 불러
    context = {'question':question}#파이썬 변수에 모델db데이터 저
    return render(request, 'pybo/question_detail.html',context)#데이터를 탬플릿html에따라서 화면에 출력
    # context에서 'question'은 템플릿에 사용될 이름, question은 파이썬에서 이름

def answer_create(request, question_id):
    '''
    pybo 답변 등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)#현재 질문페이지로 이

def question_create(request):
    """
    pybo 질문 등록
    """
    form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form':form})