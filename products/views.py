from django.shortcuts import render, redirect
import baostock as bs
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta, FR
import pytz
from .models import Document
from .forms import DocumentForm

# 当下日期 市区转换!!! 小时、分钟为中国时间 周、天为UTC时间
TODAY_UTC = datetime.date.today()   #2021-09-30
NOW_UTC = datetime.datetime.now()   #
NOW_CHINA = NOW_UTC.astimezone(pytz.timezone('Asia/Shanghai'))
DAYOFTODAY = int(TODAY_UTC.strftime("%w"))  # 1 monday, 6 saturday, 0 sunday
print(NOW_CHINA.strftime("%H"))
print(NOW_CHINA.strftime("%M"))


# 上周五日期
LASTFRIDAY = datetime.date.today() + relativedelta(weekday=FR(-1)) # 2021-09-24
LASTLASTFRIDAY = datetime.date.today() + relativedelta(weekday=FR(-2)) # 2021-09-17
THISFRIDAY = datetime.date.today() + relativedelta(weekday=FR(0)) # 2021-09-24

# 日期上限下限
if DAYOFTODAY == 0 or DAYOFTODAY == 6:                 #周日看本周涨幅
    STARTDATE = LASTFRIDAY
    ENDDATE = THISFRIDAY
elif DAYOFTODAY == 5 and int(NOW_CHINA.strftime("%H")) > 17:                #周5看zhe周涨幅
    STARTDATE = LASTFRIDAY
    ENDDATE = THISFRIDAY  
elif DAYOFTODAY == 5 and int(NOW_CHINA.strftime("%H")) == 17 and int(NOW_CHINA.strftime("%M")) >= 31:
    STARTDATE = LASTFRIDAY
    ENDDATE = THISFRIDAY 
else:                               #周一二三四看上周涨幅
    STARTDATE = LASTLASTFRIDAY
    ENDDATE = LASTFRIDAY  


# jointquant api 获取数据 保存为csv
def createcsvfilesfromjoinquantapi (stockcode,startdate,enddate,csvname):
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print(lg.error_code)
    print(lg.error_msg)

    rs = bs.query_history_k_data(stockcode,
    "date,code,open,high,low,close,volume,amount,adjustflag",
    start_date=str(startdate), end_date=str(enddate),   
    frequency="d", adjustflag="3")
    print(rs.error_code)
    print(rs.error_msg)

    # 获取具体的信息
    result_list = []
    while (rs.error_code == '0') & rs.next():
        # 分页查询，将每页信息合并在一起
        result_list.append(rs.get_row_data())
    result = pd.DataFrame(result_list, columns=rs.fields)
    result.to_csv("./products/static/" + csvname, encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()

# 上证指数 ####################################################################################
stockcode_sz = "sh.000001"
csv_sz = "shangzheng_data.csv"
createcsvfilesfromjoinquantapi(stockcode_sz,STARTDATE,ENDDATE,csv_sz)
# 沪深300####################################################################################
stockcode_hs = "sh.000300"
csv_hs = "hushen300_data.csv"
createcsvfilesfromjoinquantapi(stockcode_hs,STARTDATE,ENDDATE,csv_hs)
# 创业板指 ####################################################################################
stockcode_cybz = "sz.399006"
csv_cybz = "chuangyebanzhi_data.csv"
createcsvfilesfromjoinquantapi(stockcode_cybz,STARTDATE,ENDDATE,csv_cybz)
# 科创50 api没有此数据 ####################################################################################
#createcsvfilesfromjoinquantapi("sh.000688",STARTDATE,ENDDATE,"kechuang50_data.csv")


"""
# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print(lg.error_code)
print(lg.error_msg)

rs = bs.query_history_k_data("sh.000001",
"date,code,open,high,low,close,volume,amount,adjustflag",
start_date=str(STARTDATE), end_date=str(ENDDATE),   
frequency="d", adjustflag="3")
print(rs.error_code)
print(rs.error_msg)

# 获取具体的信息
result_list = []
while (rs.error_code == '0') & rs.next():
    # 分页查询，将每页信息合并在一起
    result_list.append(rs.get_row_data())
result = pd.DataFrame(result_list, columns=rs.fields)
result.to_csv("./products/static/shangzheng_data.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()
"""

def home(request, *args):
    context = {
        'TODAY' : str(TODAY_UTC).replace("-", "."),
    }
    return render(request, 'product/home.html', context)

def zhantou1(request, *args, **kwargs):
    return render(request, 'product/zhantou1.html')

def xinshidai8(request):
    return render(request, 'product/xinshidai8.html')

def taishan1(request):
    return render(request, 'product/taishan1.html')

def xiangjun1(request):
    return render(request, 'product/xiangjun1.html')

def gaohua1(request):
    return render(request, 'product/gaohua1.html')


def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'product/list.html', context)