from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # We need to pass request object, template file name and can also pass dictionary name
    dictionary = {'name': 'Shreya', 'profession': 'Student'}
    return render(request, 'index.html', dictionary)


def analyze(request):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # If text is available in text area or else it will take default value
    text_area = request.POST.get('tarea', 'default')
    remove_punc_cb = request.POST.get('remove_punc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcnt = request.POST.get('charcount', 'off')

    # 1. Punctuation Remover
    if remove_punc_cb == "on":
        analyzed = ''
        for ch in text_area:
            if ch not in punctuations:
                analyzed += ch

        params = {"purpose": "Remove Punctuation Marks", "analyzed_text": analyzed}
        text_area = analyzed

        # return render(request=request, template_name='analyze.html', context=params)

    # 2. Uppercase
    if uppercase == "on":
        analyzed = text_area.upper()
        params = {"purpose": "Converted to Uppercase", "analyzed_text": analyzed}
        text_area = analyzed
        # return render(request=request, template_name='analyze.html', context=params)

    # 3. New Line Remover
    if newlineremover == "on":
        analyzed = ''
        for ch in text_area:
            if not ch == '\n' and not ch == '\r':
                analyzed += ch

        params = {"purpose": "Removed New Line Character", "analyzed_text": analyzed}
        text_area = analyzed

        # return render(request=request, template_name='analyze.html', context=params)

    # 4. Space Remover
    if spaceremover == "on":
        analyzed = ''
        for index, ch in enumerate(text_area):
            if not (text_area[index] == " " and text_area[index + 1] == " "):
                analyzed += ch

        params = {"purpose": "Removed Extra Spaces", "analyzed_text": analyzed}
        text_area = analyzed
        # return render(request=request, template_name='analyze.html', context=params)

    # 5. Character Count
    if charcnt == "on":
        analyzed = len(text_area)

        params = {"purpose": "Chatacter Counts", "analyzed_text": analyzed}

        # return render(request=request, template_name='analyze.html', context=params)

    if remove_punc_cb != "on" and newlineremover != "on" and spaceremover != "on" \
            and charcnt != "on" and uppercase != "on":
        return HttpResponse("Please Select Any Operation")

    return render(request=request, template_name='analyze.html', context=params)