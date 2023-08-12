from django.shortcuts import render
from django.contrib.auth.backends import UserModel
from django.shortcuts import render
from django.http import HttpResponse, request, response
from django.http import HttpResponseRedirect, HttpResponse,FileResponse
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import reverse,redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from MxPisite import settings
from django.utils import timezone
import subprocess,sys,mxpi,os,json,time
from app import models
import threading
import requests
import base64
import serial
import serial.tools.list_ports
import platform
from xml.etree.ElementTree import parse
import re
import shutil


# Create your views here.
def getip(request):
    host = request.get_host()
    ip_address= host.split(":")[0]
    return HttpResponse(ip_address)

def home(request):
    return render(request,'index.html')

def vnc(request):
    return render(request,'vnc.html')

def upfile(request):
    code = request.POST.get('code')
    f=open(os.path.dirname(mxpi.__file__)+'/file/test.py','w',encoding='utf-8')
    #f=open('file/test.py','w')
    f.write(code)
    f.close()
    return HttpResponse('ok')


def file_list(request):
    url_=os.path.dirname(mxpi.__file__).replace('\\','/')
    url=url_+'/static/file'
    dirs=os.listdir(url)
    s=[]
    id=0
    for f in dirs:
        id += 1
        f_i={'id':'','name':'',"size":'','url':'','last':''}
        size=os.path.getsize(url+'/'+f)
        f_i['id']=id
        f_i['name']=f
        f_i['size']='%.2f' % float(size/1000) + 'KB'
        f_i['url']=url+'/'+f
        f_i['url_g']='/static/file/'+f
        f_i['last']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(url+'/'+f).st_mtime))
        s.append(f_i)
    data={
        'msg':'ok',
        'data':s,
    }
    return HttpResponse(json.dumps(data))

def file_remove(request):
    data=request.GET.get('data')
    os.remove(data)
    return HttpResponse('ok')

def files(request):
    file_obj = request.FILES.get('avatar')
    if file_obj.name=='blob':
        with open(os.path.dirname(mxpi.__file__)+'/static/file/sound'+str(int(time.time()))+'.wav', "wb") as f:
                for line in file_obj:
                    f.write(line)
        return HttpResponse('ok')
    else:
        with open(os.path.dirname(mxpi.__file__)+'/static/file/'+file_obj.name, "wb") as f:
            for line in file_obj:
                f.write(line)
        return HttpResponse('ok')
 
def get_c(request):
    try:
        name=request.GET.get('name')
        file=os.path.dirname(mxpi.__file__)+'/example/'+name+'.mxpi'
        print(file)
        if os.path.exists(file):
            f=open(file,'r',encoding='utf-8')
            c=f.read()
            return HttpResponse(json.dumps({'msg':'ok','data':c}))
        else:
            return HttpResponse(json.dumps({'msg':'err','data':''}))
    except:
         return HttpResponse(json.dumps({'msg':'err','data':''}))


def read_model_list(request):
    try:
        rq = requests.get('http://120.79.209.170/getList')
        rq.encoding='utf-8'
        return HttpResponse(json.dumps({'msg':'ok','data':rq.json()}))
    except:
        print('无法连接网络数据库,请确定设备是否联网。')
        return HttpResponse(json.dumps({'msg':'err','data':'无法连接网络数据库,请确定设备是否联网。'}))
    
def get_upmodel(request):
    name=request.GET.get('name')
    filetype=request.GET.get('type')
    info=request.GET.get('info')
    people=request.GET.get('fp_people')
    files = { 
    "field1" : (name,open(os.path.dirname(mxpi.__file__)+'/static/file/'+name,"rb"),filetype),
    } 
    rq = requests.post(url='http://120.79.209.170/upfile_Ajax',files=files,params={'name':name,'type':filetype,'info':info,'people':people})
    rq.encoding='utf-8'
    print(rq.text)
    return HttpResponse(rq.text)

def downModel(request):
    id=request.GET.get('id')
    name=request.GET.get('name')
    r = requests.get('http://120.79.209.170/downfile_Ajax',params={'id':id}) # 发送请求
    with open (os.path.dirname(mxpi.__file__)+'/static/file/'+name, 'wb') as f:
        f.write(r.content)
        f.close
    return HttpResponse('ok')    

def SArduino_get_list(request):
    if platform.system()=='Windows':
        ports = serial.tools.list_ports.comports(include_links=False)
        spp=[]
        for port, desc, hwid in sorted(ports):
            sp={
                'port':port,
                'desc':desc,
            }
            spp.append(sp)
        return HttpResponse(json.dumps({'msg':'ok','data':spp}))
    else:
        return HttpResponse(json.dumps({'msg':'err','data':'目前SArduino只支持Windows,你目前的系统为'+platform.system()}))

def SArduino_add_data(request):
    data=request.GET.get('data')
    all_in_data=models.Mxpi_SArduino_in.objects.all()
    if len(all_in_data)>10:
        all_in_data.last().delete()
    s=models.Mxpi_SArduino_in()
    s.data=data
    s.save()
    return HttpResponse(json.dumps({'msg':'ok','data':''}))

def SArduino_get_data(request):
    all_in_data=models.Mxpi_SArduino_in.objects.all()
    p=all_in_data.first()
    return HttpResponse(p.data)

def mixly_ku_download(request):
    file_path=os.path.dirname(mxpi.__file__)+'/file/SArduino-com.zip'
    with open(file_path, 'rb') as f:
        try:
            response = HttpResponse(f)
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
        except:
            pass

def upblock(request):
    file_obj = request.FILES.get('avatar')
    if file_obj.name[-3:]=='xml':
        file=os.path.dirname(mxpi.__file__)+'/block/'+file_obj.name
        #file='block/'+file_obj.name
        if os.path.exists(os.path.dirname(mxpi.__file__)+'/block'):
            pass
        else:
            os.mkdir(os.path.dirname(mxpi.__file__)+'/block')
        with open(file, "wb") as f:
            for line in file_obj:
                f.write(line)
        f=jianchaxml(file)
        if f:
            if mxltojs(file):
                return HttpResponse(json.dumps({'msg':'ok','data':''}))
            else:
                return HttpResponse(json.dumps({'msg':'err','data':'库已存在'}))
        else:
            return HttpResponse(json.dumps({'msg':'err','data':'xml格式错误,请检查'}))
    else:
        return HttpResponse(json.dumps({'msg':'err','data':'上传格式错误,模块文件格式为xml'}))


def jianchaxml(filepath):
    f = open(filepath,encoding='utf-8')
    et = parse(f)
    root = et.getroot()
    if root.tag=='mxpiblock':
        namelist=[]
        for i in root:
            namelist.append(i.tag)
        if namelist == ['name','version','author','info','xml','block','code']:
            return True
        else:
            return False
    else:
        return False

def mxltojs(filepath):
    f = open(filepath,encoding='utf-8')
    et = parse(f)
    f.close()
    xmlstr=open(filepath,'r',encoding='utf-8').read()
    root = et.getroot()
    name=root.find('name').text
    info=root.find('info').text
    author=root.find('info').text
    version=root.find('version').text
    block=root.find('block').text
    code=root.find('code').text
    result={'name':name,'version':version,'info':info,'author':author}
    if os.path.exists(os.path.dirname(mxpi.__file__)+'/static/block'):
        pass
    else:
        os.mkdir(os.path.dirname(mxpi.__file__)+'/static/block')
    dirpath=os.path.dirname(mxpi.__file__)+'/static/block/'+name+'_'+version
    #dirpath='static/block/'+name+'_'+version
    if os.path.exists(dirpath):
        return False
    else:
        os.mkdir(dirpath)
    try:
        savefile=dirpath+'/'+name+'_'+version+'_info.json'
        #savefile=dirpath+'/'+name+'_'+version+'_info.json'
        op=open(savefile,'w',encoding='utf-8')
        op.write(json.dumps(result))
        op.close()
        pattern = re.compile(r'<xml>.*?xml>',re.I|re.S)
        result = pattern.search(xmlstr)
        result=result.group().replace('<xml>\n','').replace('</xml>','')
        xmlpath=dirpath+'/'+name+'_'+version+'_block.xml'
        #xmlpath=dirpath+'/'+name+'_'+version+'_block.xml'
        op=open(xmlpath,'w',encoding='utf-8')
        op.write(result)
        op.close()
        txpath=dirpath+'/'+name+'_'+version+'_tx.js'
        #txpath=dirpath+'/'+name+'_'+version+'_tx.js'
        with open(txpath,'w',encoding='utf-8')as file:
            file.write(block)
        codepath=dirpath+'/'+name+'_'+version+'_code.js'
        #codepath=dirpath+'/'+name+'_'+version+'_code.js'
        with open(codepath,'w',encoding='utf-8')as file:
            file.write(code)
        return True
    except:
        shutil.rmtree(dirpath)
        return False
    
    
def load_mk_list(request):
    if os.path.exists(os.path.dirname(mxpi.__file__)+'/static/block'):
        pass
    else:
        os.mkdir(os.path.dirname(mxpi.__file__)+'/static/block')
    kupath=os.path.dirname(mxpi.__file__)+'/static/block'
    #kupath='static/block/'
    kulist=os.listdir(kupath)
    return HttpResponse(json.dumps({'msg':'ok','data':kulist}))

def load_mk_add(request):
    name=request.GET.get('name')
    xmlpath=os.path.dirname(mxpi.__file__)+'/static/block/'+name+'/'+name+'_block.xml'
    #xmlpath='static/block/'+name+'/'+name+'_block.xml'
    f=open(xmlpath,'r',encoding='utf-8')
    xml=f.read()
    op={
        'name':name,
        'xml':xml,
        'code':"static/block/"+name+"/"+name+"_code.js",
        'tx':"static/block/"+name+"/"+name+"_tx.js",
    }
    return HttpResponse(json.dumps({'msg':'ok','data':op}))

def mk_list(request):
    kupath=os.path.dirname(mxpi.__file__)+'/static/block/'
    #kupath='static/block/'
    kulists=os.listdir(kupath)
    s=[]
    i=0
    for ku in kulists:
        i += 1
        f=open(kupath+'/'+ku+"/"+ku+'_info.json', "r", encoding="utf-8")
        content = json.load(f)
        content['id']=i
        content['down']='<i class="fa fa-close" style="color: red;" onclick="del_mk(\''+content['name']+'_'+content['version']+'\')"></i>'
        s.append(content)

    return HttpResponse(json.dumps({'msg':'ok','data':s}))

def del_mk(request):
    mkname=request.GET.get('mkname')
    kupath=os.path.dirname(mxpi.__file__)+'/static/block/'
    #kupath='static/block/'
    try:
        shutil.rmtree(kupath+'/'+mkname)
        return HttpResponse(json.dumps({'msg':'ok','data':'删除成功'}))
    except Exception as e:
        return HttpResponse(json.dumps({'msg':'err','data':'删除失败:'+str(e)}))