from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def count(request):
    user_text=request.GET['text']
    total_count=len(user_text)#获取字典的方法
    word_dict={}
    for word in user_text:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1
    sorted_dict=sorted(word_dict.items(),key=lambda x:x[1] ,reverse=True)
    context={'total_count':total_count,'text':user_text,'word_dict':word_dict,'sorted_dict':sorted_dict}
    return render(request,'count.html',context=context)