from django.shortcuts import render

""" def show_data(request):
    original_data = request.db_data  # from middleware
    updated_data = original_data + " shet"  # append the word "shet"
    return render(request, "mainapp/show_data.html", {
        "updated_data": updated_data
    }) """

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render, redirect
from .forms import LoginForm

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thankyou.html')
    else:
        form = FeedbackForm()

    return render(request, 'mainapp/feedback.html', {'form': form})

def get_keyword_list(user_input):

    global kwl

    invalid_chr = ['~','`','!','@','#','$','%',
               '^','&','*','(',')','-','_',
               '+','=','    ','[',']','{','}','|','\\','\'','"',
               '<','>','?','/']

    valid_chr = ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d',
                 's','a','z','x','c','v','b','n','m',':',';','.',',',' ','1','2','3','4','5','6',
                 '7','8','9','0']

    user_input = user_input.lower() 
    user_input = user_input.strip()

    kwl = []

    message = ''

    if len(user_input) == 0:
        message = "Please enter keywords in the provided input box and then submit."
        return message
    
    if len(user_input) >= 120:
        message = "Total length of all keywords is exceeding 120 characters, Remove few keywords and try."
        return message

    for i in range(len(invalid_chr)):
        contains = invalid_chr[i] in user_input
        if contains:
            message = 'Remove any invalid characters, such as '+ str(invalid_chr[i]) +', from the input.'

    for i in range(len(user_input)):
        contains = user_input[i] in valid_chr
        if not contains:
            message = 'Remove any invalid characters, such as '+ str(user_input[i]) +', from the input.'
    

    new_string = user_input.replace(';', '#').replace(':', '#').replace(',','#').replace('.','#')
    split_string = new_string.split('#')

    switch = False

    for strr in split_string:
        str1 = strr
        str1 = str1.strip()
        kwl.append(str1)
        if len(str1) <= 2:
            switch = True
    
    if switch:
        message = "Make sure a keyword must contain atleast 3 characters (error KW:'" + str1 + "')"
        return message

    if len(kwl) > 10:
        message = "Input has more than 10 keywords, Remove few keywords and try."
        return message

    return message

def get_sdg_match(): 

    global kwl

    sdg_exact = [[] * 1 for _ in range(len(kwl))]
    
    i = 0
    for kw in kwl:

        for s_kw in data_01:
            if kw == s_kw: 
                sdg_exact[i].append(1)
                break
        for s_kw in data_02:
            if kw == s_kw: 
                sdg_exact[i].append(2)
                break
        for s_kw in data_03:
            if kw == s_kw: 
                sdg_exact[i].append(3)
                break
        for s_kw in data_04:
            if kw == s_kw: 
                sdg_exact[i].append(4)
                break
        for s_kw in data_05:
            if kw == s_kw: 
                sdg_exact[i].append(5)
                break
        for s_kw in data_06:
            if kw == s_kw: 
                sdg_exact[i].append(6)
                break
        for s_kw in data_07:
            if kw == s_kw: 
                sdg_exact[i].append(7)
                break
        for s_kw in data_08:
            if kw == s_kw: 
                sdg_exact[i].append(8)
                break
        for s_kw in data_09:
            if kw == s_kw: 
                sdg_exact[i].append(9)
                break
        for s_kw in data_10:
            if kw == s_kw: 
                sdg_exact[i].append(10)
                break
        for s_kw in data_11:
            if kw == s_kw: 
                sdg_exact[i].append(11)
                break
        for s_kw in data_12:
            if kw == s_kw: 
                sdg_exact[i].append(12)
                break
        for s_kw in data_13:
            if kw == s_kw: 
                sdg_exact[i].append(13)
                break
        for s_kw in data_14:
            if kw == s_kw: 
                sdg_exact[i].append(14)
                break
        for s_kw in data_15:
            if kw == s_kw: 
                sdg_exact[i].append(15)
                break
        for s_kw in data_16:
            if kw == s_kw: 
                sdg_exact[i].append(16)
                break
        for s_kw in data_17:
            if kw == s_kw: 
                sdg_exact[i].append(17)
                break
        for s_kw in data_xx:
            if kw == s_kw: 
                sdg_exact[i].append('xx')
                break
        for s_kw in data_yy:
            if kw == s_kw: 
                sdg_exact[i].append('yy')
                break

        i = i + 1

    return sdg_exact

def get_partial_match(kw):

    sdg_part = [[] * 1 for _ in range(17)]

    i = 0 

    for skw in data_01:
        contains = kw in skw
        if contains:
            sdg_part[0].append(skw)

    for skw in data_02:
        contains = kw in skw
        if contains:
            sdg_part[1].append(skw)   

    for skw in data_03:
        contains = kw in skw
        if contains:
            sdg_part[2].append(skw)  

    for skw in data_04:
        contains = kw in skw
        if contains:
            sdg_part[3].append(skw)   

    for skw in data_05:
        contains = kw in skw
        if contains:
            sdg_part[4].append(skw) 

    for skw in data_06:
        contains = kw in skw
        if contains:
            sdg_part[5].append(skw)    

    for skw in data_07:
        contains = kw in skw
        if contains:
            sdg_part[6].append(skw)    

    for skw in data_08:
        contains = kw in skw
        if contains:
            sdg_part[7].append(skw)  

    for skw in data_09:
        contains = kw in skw
        if contains:
            sdg_part[8].append(skw) 

    for skw in data_10:
        contains = kw in skw
        if contains:
            sdg_part[9].append(skw)  

    for skw in data_11:
        contains = kw in skw
        if contains:
            sdg_part[10].append(skw)   

    for skw in data_12:
        contains = kw in skw
        if contains:
            sdg_part[11].append(skw) 

    for skw in data_13:
        contains = kw in skw
        if contains:
            sdg_part[12].append(skw)  

    for skw in data_14:
        contains = kw in skw
        if contains:
            sdg_part[13].append(skw)   

    for skw in data_15:
        contains = kw in skw
        if contains:
            sdg_part[14].append(skw)  

    for skw in data_16:
        contains = kw in skw
        if contains:
            sdg_part[15].append(skw)  

    for skw in data_17:
        contains = kw in skw
        if contains:
            sdg_part[16].append(skw)            

    return sdg_part

def main(request):
    
    global data_01, data_02, data_03, data_04, data_05, data_06, \
    data_07, data_08, data_09, data_10, data_11, data_12, data_13, \
    data_14, data_15, data_16, data_17, user_input, data_xx, data_yy

    context = {}
    data_01 = request.data_01
    data_02 = request.data_02
    data_03 = request.data_03
    data_04 = request.data_04
    data_05 = request.data_05
    data_06 = request.data_06
    data_07 = request.data_07
    data_08 = request.data_08
    data_09 = request.data_09
    data_10 = request.data_10
    data_11 = request.data_11
    data_12 = request.data_12
    data_13 = request.data_13
    data_14 = request.data_14
    data_15 = request.data_15
    data_16 = request.data_16
    data_17 = request.data_17
    data_xx = request.data_xx
    data_yy = request.data_yy

    template = loader.get_template('mainapp/main.html')
    
    if 'button1' in request.POST: 
        user_input = request.POST.get('user_keyword')
        
        message = ''

        message = get_keyword_list(user_input)

        if len(message) != 0:

            context = { 
                'err': "Input Error : ",
                'msg': message ,
                       }
            return HttpResponse(template.render(context, request))

        sdg_exact = get_sdg_match()

        data = []
        j = 0
        for i in range(len(kwl)):
            if sdg_exact[i] != []:
                j = j + 1
        k = len(kwl)

        str2 = ', '.join(kwl)       

        strr = '<h2>Summary:</h2>' + \
        'Your Keywords: '+ str2 + '<br>' + \
        'Keywords Found: ' + str(j) + '/' + str(k) + ' (' + str(round((j/k)*100,0)) + '%) ' + \
        '<br>****************************************************************************<br>'
        
        data.append(strr)

        switch = False

        for i in range(len(kwl)):

            one_percent = False
            two_percent = False

            strr = ''
            if sdg_exact[i] == []:
                strr = '<span style="color:red;">' + str(i+1) + '. "' + str(kwl[i]) + '" Not Found.</span><br>'

                switch = True
                data.append(strr)

            else:
                str2 = ''

                for j in range(len(sdg_exact[i])):
                    
                    if str(sdg_exact[i][j]) == 'xx':
                        one_percent = True
                        sdg_exact[i].pop()
                    elif str(sdg_exact[i][j]) == 'yy':
                        two_percent = True
                        sdg_exact[i].pop()
                    else:
                        str2 = str2 + str(sdg_exact[i][j]) + ', '
                
                str2 = str2[0:len(str2)-2]

                if one_percent: 
                    strr = '<span style="color:green;">' + str(i+1) + '. "' + str(kwl[i]) + '" found in ' + str(len(sdg_exact[i])) + ' SDGs: ' + str2 + ' </span> <br>'
                elif two_percent: 
                    strr = '<span style="color:orange;">' + str(i+1) + '. "' + str(kwl[i]) + '" found in ' + str(len(sdg_exact[i])) + ' SDGs: ' + str2 + ' </span> <br>'
                else:
                    strr ='<span>' + str(i+1) + '. "' + str(kwl[i]) + '" found in ' + str(len(sdg_exact[i])) + ' SDGs: ' + str2 + '</span> <br>'

                str2 = ''
                data.append(strr)
            

        if switch: 
            strr = '<span style="color:violet;">Try Advanced search for the keyword not found here and also make sure keyword spelled correctly.</span>'
            switch = False
            data.append(strr)
        
        context = { 
            'data':data ,
            'usr' : user_input
            } 
        
    elif 'button2' in request.POST:

        user_input = request.POST.get('user_keyword')

        message = get_keyword_list(user_input)

        if len(message) != 0:

            context = { 
                'err': "Input Error : ",
                'msg': message ,
                       }
            return HttpResponse(template.render(context, request))


        data = []

        str2 = ', '.join(kwl)


        strr = '<h2>Summary:</h2>' + \
        '<h3>Your keywords: '+ str2 + '</h3>' + \
            '****************************************************************************<br>' 
        
        data.append(strr)

        

        for i in range(len(kwl)):

            strr = ''
            sdg_part = get_partial_match(kwl[i])

            k = 0
            for j in range(len(sdg_part)):
                if sdg_part[j] != []:
                    k = k + 1
            
            strr = '<h3>'+str(i+1)+'. "' + str(kwl[i]) + '" has partial match in ' + str(k) + ' SDGs.</h3>'
            data.append(strr) 
            switch = True
            strr = ''

            for j in range(17):

                if sdg_part[j] != []:
                    strr = strr + 'SDG ' + str(j+1) + ' ('+str(len(sdg_part[j]))+' matches)'+ ': "'
                    strr2 = ', '.join(sdg_part[j])
                    strr = strr + strr2 + '" <br><br>'
                    switch = False

            if switch:
                strr2 = str(kwl[i])
                #a = TextBlob(strr2)
                #strr2 = str(a.correct())
                str3 = '<p style="color:red;">The keyword "' + str(kwl[i]) + '" might be spelled wrongly<br>' \
                + 'Suggested words: ' + strr2 + '</p><br>'
                strr = strr + str3


           
            data.append(strr)

        context = { 
            'data':data,
            'usr' : user_input
              } 

    return HttpResponse(template.render(context, request))


def help(request):
    template = loader.get_template('mainapp/help.html')
    return HttpResponse(template.render())

def get_user_info(request):
    return render(request, 'mainapp/user_info_form.html')

def confirmation_page(request):
    return render(request, 'mainapp/confirmation_page.html')

# myapp/views.py

def login_view(request):
    if request.method == 'POST':
              
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print('form  = ', name)
            #template = loader.get_template('index.html')
            return redirect('mainapp.main.html')
            
        
    else:
        
        form = LoginForm()
    
    return render(request, 'mainapp/login.html', {'form': form})


# myapp/views.py
def success_view(request):
    name = request.GET.get('name')
    return render(request, 'mainapp/success.html', {'name': name})

kwl = []
user_input = ''
