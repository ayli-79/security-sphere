from django.shortcuts import render

def mvd(request):
    return render(request, 'MVD.html')

def sredstva(request):
    return render(request, 'sredstva.html')

def chs(request):
    return render(request, 'CHS.html')

def fire(request):
    return render(request, 'fire.html')

def test(request):
    return render(request, 'test.html')

def video(request):
    return render(request, 'video.html')

def yroc(request):
    return render(request, 'yroc.html')

def valcovka(request):
    return render(request, 'valcovka.html')

def yroc2(request):
    return render(request, 'yroc2.html')

def yroc3(request):
    return render(request, 'yroc3.html')

def yroc4(request):
    return render(request, 'yroc4.html')


# Словарь с правильными ответами
from django.shortcuts import render, redirect

# Словарь с правильными ответами
CORRECT_ANSWERS = {
    'question1': 'Пыль',
    'question2': 'Поднятие тяжестей, повторяющиеся движения, неудобные позы',
    'question3': 'Освещение',
    'question4': 'Одноразовые респираторы эффективны против пыли и тумана, но не против газов или паров.',
    'question5': 'В специально отведенных и хорошо проветриваемых помещениях.',
    'question6': 'Портативные огнетушители',
    'question7': 'Защитные перчатки',
    'question8': 'Защитники органов слуха',
    'question9': 'Должны, на случай, если их основной путь будет заблокирован.',
    'question10': 'Могут, если основное место сбора недоступно.'
}

def submit_test(request):
    if request.method == 'POST':
        score = 0
        total_questions = len(CORRECT_ANSWERS)

        for question, correct_answer in CORRECT_ANSWERS.items():
            if request.POST.get(question) == correct_answer:
                score += 1

        percentage = (score / total_questions) * 100
        certificate = score == total_questions

        context = {
            'score': score,
            'total_questions': total_questions,
            'percentage': percentage,
            'certificate': certificate
        }
        return render(request, 'result.html', context)
    else:
        return redirect('test')
