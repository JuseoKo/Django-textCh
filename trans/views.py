from django.shortcuts import render, redirect
from .transdata import data_compare, data_add, add_f
import os

def pj_name_load():
    filenames = os.listdir('./trans/data/')
    for j in range(0, len(filenames)):
        ch = filenames[j].replace('.json', '')
        filenames[j] = ch
    return filenames


#메인페이지
def abuot(request):

    #하위 디렉토리 이름을 이름정렬 순으로 리스트화
    filenames = pj_name_load()

    return render(request, 'about/about.html', {'file_list': filenames})


#url에 file_name 즉 매개변수로 설정했으니 이 함수에서 받아와야함
#번역페이지
def main(request, file_name):

    filenames = pj_name_load()

    if request.method == 'POST':
        data = request.POST['inp']
        out_data = data_compare(data, file_name)
        return render(request, 'main/index.html', {'out_data': out_data, 'file_list': filenames})
    else:
        return render(request, "main/index.html", {'file_list': filenames})

#번역등록페이지
def main_add(request, file_name):

    filenames = pj_name_load()

    for j in range(0, len(filenames)):
        ch = filenames[j].replace('.json', '')
        filenames[j] = ch
    if request.method == 'POST':
        f_data = request.POST['inps']
        s_data = request.POST['oups']
        data_add(f_data, s_data, file_name)

        return render(request, 'main/index_add.html', {'file_name': file_name, 'file_list': filenames})
    else:
        return render(request, 'main/index_add.html', {'file_name': file_name, 'file_list': filenames})

def pj_add(request):
    if request.method == 'POST':
        pj_name = request.POST['pj_add']
        add_f(pj_name)
        return redirect('about')
    else:
        return redirect('about')



#return render(request, 'main/main.html') : 요청이 들어오면 main/main.html을 보여줘라
#return render(request, 'main/main.html', {'data': data}) : html에서 data라는 폼에 반환할 값
