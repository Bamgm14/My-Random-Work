from django.shortcuts import render
import pandas as pd
def test(request):
    if request.method=='POST':
        info={'Name':request.POST.get('name'),'Anime':request.POST.get('anime'),'Cars':request.POST.get('cars')}
        df = pd.DataFrame(info, columns= ['Name','Anime','Cars'],index=[0])
        print(df)
        df.to_csv('my_csv.csv', mode='a', header=True)
    return render(request,'index1.html')
# Create your views here.
