__author__ = 'adwo15511'
#coding = utf-8
from django.http import JsonResponse
from guest.models import Event, Guest
from django.core.exceptions import ObjectDoesNotExist


#活动增加
def add_event(request):
    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')
    status = request.POST.get('status', '')
    limit = request.POST.get('limit', '')
    start_time = request.POST.get('start_time', '')
    address = request.POST.get('address', '')

    if eid =='' or name =='' or start_time =='' or address =='':
        return JsonResponse({'status': 201, 'message': 'parameter error'})

    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status': 202, 'message': 'eid already exist'})

    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status': 203, 'message': 'name already exist'})

    if status =='':
        status = 1

    if limit =='':
        limit = 0

    Event.objects.create(id=eid,name=name,status=status,limit=limit,start_time=start_time,address=address)
    return JsonResponse({'status': 200, 'message': 'add event success'})

#用户增加
def add_guest(request):
    gid = request.POST.get('gid', '')
    realname = request.POST.get('realname', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    sign = request.POST.get('sign', '')

    if gid == '' or realname == '' or phone == '':
        return JsonResponse({'status': 201, 'message': 'parameter error'})

    result = Guest.objects.filter(gid=id)
    if result:
        return JsonResponse({'status': 202, 'message': 'Guest id already exist'})

    result = Guest.objects.filter(realname=realname)
    if result:
        return JsonResponse({'status': 203, 'message': 'Guest name already exist'})

    result = Guest.objects.filter(phone=phone)
    if result:
        return JsonResponse({'status': 204, 'message': 'Guest phone already exist'})

    if email == '':
        email = null

    if sign == '':
        sign = 1


#    Guest.objects.create(id=gid, realname=realname, email=email, phone=phone, sign=sign)
    return JsonResponse({'status': 200, 'message': 'add guest success'})






def search_event(request):
    eid = request.GET.get('eid', '')
    name = request.GET.get('name', '')

    if eid == '' and name == '':
        return JsonResponse({'status': 201, 'message': 'parameter error'})

    if eid != '':
        try:
            result = Event.objects.get(id=eid)
            if result:
                data = {}
                data['eid'] = result.id
                data['name'] = result.name
                data['status'] = result.status
                data['address'] = result.address
                data['limit'] = result.limit
                data['start_time'] = result.start_time
                return JsonResponse({'status': 200, 'message': 'search event success','data': data})
        except ObjectDoesNotExist as e:
            return JsonResponse({'status': 205, 'message': 'no this event'})

    if name != '':
        result = Event.objects.filter(name__contains = name)
        if result:
            data = []
            for r in result:
                event = {}
                event['eid'] = r.id
                event['name'] = r.name
                event['status'] = r.status
                event['address'] = r.address
                event['limit'] = r.limit
                event['start_time'] = r.start_time
                data.append(event)
            return JsonResponse({'status': 200, 'message': 'search name success','data': data})
        else:
            return JsonResponse({'status': 206, 'message': 'no this name'})





