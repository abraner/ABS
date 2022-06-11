from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from .models import CustomerInfo, DeleteCust, Appointment, AppQueue, AppQueueCount, Bidpage, BeamInfo, JobCost, TaxRate,\
    LallyColumn, FootingSize, Contract, Photo, PDF
from .forms import Custinfo, AppointMent, QueueCount, AppointMent1, BidPage, BeamTypeChoiceField, BeamSizeChoiceField,\
    CostJob, ConTract, CustinfoC, JobImages, JobPdf
from django.db.models import Q, Sum, F
from django.core.paginator import Paginator
from .functions import handle_uploaded_file, handle_uploaded_PDF_file


def welcome(request):
    return render(request, 'abs/welcome.html')


def main(request, id=None):
    instance = AppQueueCount.objects.get(id=id)
    form = QueueCount(request.POST or None, instance=instance)
    context = {
        "instance": instance,
        "form": form,
    }
    ###return redirect(instance.get_absolute3_url(), context)
    return render(request, 'abs/main.html', context)


def preappoint(request):
    return render(request, 'abs/preappoint.html')



def newcust(request):
    if request.method == 'POST':
        form = CustinfoC(request.POST)
        if form.is_valid():
            form.save()
            a = CustomerInfo.objects.all()
            b = Appointment.objects.all()
            instance = CustomerInfo.objects.order_by('id').last()
            c = a.values_list('id', flat=True).last()
            d = Appointment.objects.create(custid=c)
            e = b.values_list('id', flat=True).last()
            instance2 = Appointment.objects.order_by('custid').last()
            CustomerInfo.objects.filter(id=c).update(custid=c)
            f = b.values_list('id', flat=True).last()
            g = b.values_list('date', flat=True).get(id=f)
            h = b.filter(id=f).update(callindate=g, mainid=1)
            i = Bidpage.objects.create(custid=c)
            j = Bidpage.objects.values_list('id', flat=True).last()
            k = Bidpage.objects.filter(id=j).update(bidid=j)
            l = JobCost.objects.create(bidid=j, custid=c)
            m = Contract.objects.create(bidid=j, custid=c)
            context2 = {
                "instance": instance,
                "instance2": instance2,
                "a": a,
                "b": b,
                "d": d,
                "e": e,
                "h": h,
                "i": i,
                "j": j,
                "k": k,
                "l": l,
                "m": m,
            }

            ###return render(request, 'wsc/newcon.html', context2)
            return redirect(instance.get_absolute6_url(), context2)
        else:
            form = CustinfoC()
            return render(request, 'abs/custerror.html', {'form': form})
    else:
        form = CustinfoC()
        return render(request, 'abs/newcust.html', {'form': form})





def custerror(request):
    return render(request, 'abs/custerror.html')


def deletecust(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/deletecust.html', context)


def deletecustconfirm(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)
    DeleteCust.objects.all().delete()
    a = CustomerInfo.objects.all()
    b = CustomerInfo.objects.values_list('custid', flat=True).get(custid=id)
    c = DeleteCust.objects.create(deletecust=id, deletecon=b)
    instance6 = a.order_by('id').last()
    context2 = {
        "instance6": instance6,
        "form": form,
        "c": c,
    }
    return redirect(instance6.get_absolute45_url(), context2)


def deletecust2(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)

    a = CustomerInfo.objects.all()
    b = CustomerInfo.objects.values_list('conid', flat=True).get(custid=id)
    c = a.values_list('conid', flat=True).last()
    d = DeleteCust.objects.filter(id=c).update(deletecust=id, deletecon=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute28_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "d": d,
    }
    return render(request, 'abs/deletecust2.html', context)


def deletecust4(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)
    a = Appointment.objects.all()
    b = AppQueue.objects.all()
    c = Bidpage.objects.all()
    d = Contract.objects.all()
    e = JobCost.objects.all()
    f = CustomerInfo.objects.all()
    g = Photo.objects.all()
    h = PDF.objects.all()
    a.filter(custid=id).delete()
    b.filter(custid=id).delete()
    c.filter(custid=id).delete()
    d.filter(custid=id).delete()
    e.filter(custid=id).delete()
    f.filter(custid=id).delete()
    g.filter(custid=id).delete()
    h.filter(custid=id).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute10_url(), context)


def cust_info_existing(request):
    instance2 = Appointment.objects.order_by('mainid').last()
    queryset = CustomerInfo.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(custcompanytname__icontains=search_term)
                                   | Q(custfirstname__icontains=search_term)
                                   | Q(custlastname__icontains=search_term)
                                   | Q(custadd1__icontains=search_term)
                                   | Q(custadd2__icontains=search_term)
                                   | Q(custcity__icontains=search_term)
                                   | Q(custst__icontains=search_term)
                                   | Q(custzipcode__icontains=search_term)
                                   | Q(custwork1__icontains=search_term)
                                   | Q(custwork2__icontains=search_term)
                                   | Q(custcell1__icontains=search_term)
                                   | Q(custcell2__icontains=search_term)
                                   | Q(custhome__icontains=search_term)
                                   | Q(custemail1__icontains=search_term)
                                   | Q(custemail2__icontains=search_term))
    paginator = Paginator(queryset, 13)  # Show 6 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "instance2": instance2,
               }
    return render(request, 'abs/cust_info_existing.html', context)


def custinfo(request, id):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)
    queryset = CustomerInfo.objects.filter(id=id)
    instance2 = Bidpage.objects.order_by('id').get(custid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute7_url(), context2)
    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
    }
    return render(request, 'abs/custinfo.html', context)


def edit_cust_info(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfo(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute5_url())

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/edit_cust_info.html', context)


def appointment(request, custid):
    instance = get_object_or_404(Appointment, custid=custid)
    form = AppointMent(request.POST or None, instance=instance)
    queryset2 = CustomerInfo.objects.filter(custid=custid).values()
    context = {
        "instance": instance,
        "form": form,
        "object_list2": queryset2,
    }
    return render(request, 'abs/appointment.html', context)


def scheduledappt(request, custid):
    instance = get_object_or_404(Appointment, custid=custid)
    form = AppointMent1(request.POST or None, instance=instance)
    queryset2 = CustomerInfo.objects.filter(custid=custid).values()
    instance2 = Bidpage.objects.order_by('id').get(custid=custid)
    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list2": queryset2,
    }
    return render(request, 'abs/scheduledappt.html', context)


def appointmentdate(request, custid=None):
    instance = Appointment.objects.get(custid=custid)
    form = AppointMent(request.POST or None, instance=instance)
    d = request.POST['id_appointmentdate']
    e = Appointment.objects.filter(custid=custid).update(appdate=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'abs/appointment.html', context)


def time(request, custid=None):
    instance = Appointment.objects.get(custid=custid)
    form = AppointMent(request.POST or None, instance=instance)
    d = request.POST['id_apptime']
    e = Appointment.objects.filter(custid=custid).update(apptime_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'abs/appointment.html', context)


def scopeofwork(request, custid=None):
    instance = Appointment.objects.get(custid=custid)
    form = AppointMent(request.POST or None, instance=instance)
    d = request.POST['id_appdescrip']
    e = Appointment.objects.filter(custid=custid).update(appdescrip=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'abs/appointment.html', context)


def appendapp(request, custid=None):
    instance = Appointment.objects.get(custid=custid)
    form = AppointMent(request.POST or None, instance=instance)
    a = Appointment.objects.values_list('custid', flat=True).last()
    b = Appointment.objects.values_list('appdate', flat=True).last()
    c = Appointment.objects.values_list('apptime_id', flat=True).last()
    d = Appointment.objects.values_list('appdescrip', flat=True).last()
    instance2 = Appointment.objects.order_by('mainid').last()
    f = AppQueue.objects.create(custid=a, appdate=b, apptime=c, appdescrip=d)
    g = AppQueue.objects.count()
    h = AppQueueCount.objects.values_list('id', flat=True).last()
    i = AppQueueCount.objects.filter(id=h).update(count=g)
    context2 = {
        "form": form,
        "f": f,
        "g": g,
        "i": i,
    }
    return redirect(instance2.get_absolute3_url(), context2)



def appqueue(request):
    instance2 = Appointment.objects.order_by('mainid').last()
    a = AppQueue.objects.annotate(cust=F('custid'))
    b = list(a.values_list('custid', flat=True))
    try:
        cust1 = CustomerInfo.objects.filter(custid=b[0])
        appqueue1 = AppQueue.objects.filter(custid=b[0])
    except Exception:
        cust1 = CustomerInfo.objects.filter(custid=0)
        appqueue1 = AppQueue.objects.filter(custid=0)
    try:
        cust2 = CustomerInfo.objects.filter(custid=b[1])
        appqueue2 = AppQueue.objects.filter(custid=b[1])
    except Exception:
        cust2 = CustomerInfo.objects.filter(custid=0)
        appqueue2 = AppQueue.objects.filter(custid=0)
    try:
        cust3 = CustomerInfo.objects.filter(custid=b[2])
        appqueue3 = AppQueue.objects.filter(custid=b[2])
    except Exception:
        cust3 = CustomerInfo.objects.filter(custid=0)
        appqueue3 = AppQueue.objects.filter(custid=0)
    try:
        cust4 = CustomerInfo.objects.filter(custid=b[3])
        appqueue4 = AppQueue.objects.filter(custid=b[3])
    except Exception:
        cust4 = CustomerInfo.objects.filter(custid=0)
        appqueue4 = AppQueue.objects.filter(custid=0)
    try:
        cust5 = CustomerInfo.objects.filter(custid=b[4])
        appqueue5 = AppQueue.objects.filter(custid=b[4])
    except Exception:
        cust5 = CustomerInfo.objects.filter(custid=0)
        appqueue5 = AppQueue.objects.filter(custid=0)
    try:
        cust6 = CustomerInfo.objects.filter(custid=b[5])
        appqueue6 = AppQueue.objects.filter(custid=b[5])
    except Exception:
        cust6 = CustomerInfo.objects.filter(custid=0)
        appqueue6 = AppQueue.objects.filter(custid=0)
    try:
        cust7 = CustomerInfo.objects.filter(custid=b[6])
        appqueue7 = AppQueue.objects.filter(custid=b[6])
    except Exception:
        cust7 = CustomerInfo.objects.filter(custid=0)
        appqueue7 = AppQueue.objects.filter(custid=0)
    try:
        cust8 = CustomerInfo.objects.filter(custid=b[7])
        appqueue8 = AppQueue.objects.filter(custid=b[7])
    except Exception:
        cust8 = CustomerInfo.objects.filter(custid=0)
        appqueue8 = AppQueue.objects.filter(custid=0)
    try:
        cust9 = CustomerInfo.objects.filter(custid=b[8])
        appqueue9 = AppQueue.objects.filter(custid=b[8])
    except Exception:
        cust9 = CustomerInfo.objects.filter(custid=0)
        appqueue9 = AppQueue.objects.filter(custid=0)
    try:
        cust10 = CustomerInfo.objects.filter(custid=b[9])
        appqueue10 = AppQueue.objects.filter(custid=b[9])
    except Exception:
        cust10 = CustomerInfo.objects.filter(custid=0)
        appqueue10 = AppQueue.objects.filter(custid=0)
    try:
        cust11 = CustomerInfo.objects.filter(custid=b[10])
        appqueue11 = AppQueue.objects.filter(custid=b[10])
    except Exception:
        cust11 = CustomerInfo.objects.filter(custid=0)
        appqueue11 = AppQueue.objects.filter(custid=0)
    try:
        cust12 = CustomerInfo.objects.filter(custid=b[11])
        appqueue12 = AppQueue.objects.filter(custid=b[11])
    except Exception:
        cust12 = CustomerInfo.objects.filter(custid=0)
        appqueue12 = AppQueue.objects.filter(custid=0)
    try:
        cust13 = CustomerInfo.objects.filter(custid=b[12])
        appqueue13 = AppQueue.objects.filter(custid=b[12])
    except Exception:
        cust13 = CustomerInfo.objects.filter(custid=0)
        appqueue13 = AppQueue.objects.filter(custid=0)

    context = {
        "cust1": cust1,
        "cust2": cust2,
        "cust3": cust3,
        "cust4": cust4,
        "cust5": cust5,
        "cust6": cust6,
        "cust7": cust7,
        "cust8": cust8,
        "cust9": cust9,
        "cust10": cust10,
        "cust11": cust11,
        "cust12": cust12,
        "cust13": cust13,
        "appqueue1": appqueue1,
        "appqueue2": appqueue2,
        "appqueue3": appqueue3,
        "appqueue4": appqueue4,
        "appqueue5": appqueue5,
        "appqueue6": appqueue6,
        "appqueue7": appqueue7,
        "appqueue8": appqueue8,
        "appqueue9": appqueue9,
        "appqueue10": appqueue10,
        "appqueue11": appqueue11,
        "appqueue12": appqueue12,
        "appqueue13": appqueue13,
        "instance2": instance2,

    }
    return render(request, 'abs/appqueue.html', context)


def bidpage(request, id=None):
    instance = Bidpage.objects.get(id=id)
    instance2 = JobCost.objects.get(bidid=id)
    form = BidPage(request.POST or None, instance=instance)
    form2 = CostJob(request.POST or None, instance=instance2)
    a = Bidpage.objects.values_list('custid', flat=True).get(id=id)
    instance3 = CustomerInfo.objects.order_by('id').get(id=a)
    context = {
        "instance": instance,
        "instance2": instance2,
        "instance3": instance3,
        "form": form,
        "form2": form2,

    }

    return render(request, 'abs/bidpage.html', context)


def beamtype(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamtype1']
    Bidpage.objects.filter(id=id).update(beamtype1=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_beamtype(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamtypeB = Bidpage.objects.values('beamtype1').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "beamtypeB": beamtypeB,
        "form": form,
    }
    return render(request, 'abs/load_beamtype.html', context)


def load_beamtypeB(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamtypeB = Bidpage.objects.values('beamtype1').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "beamtypeB": beamtypeB,
        "form": form,
    }
    return render(request, 'abs/load_beamtypeB.html', context)


def beamsize(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST.get('id_beamsize1')
    Bidpage.objects.filter(id=id).update(beamsize1=d, beamselect=1, disabled=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_beamsize(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    a = Bidpage.objects.all()
    form = BidPage(request.POST or None, instance=instance)
    b = a.values_list('beamtype1', flat=True).get(id=id)
    c = BeamInfo.objects.filter(beam_type=b).values('beam_size').distinct().order_by('beam_size')

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "c": c,
        "form": form,
    }
    return render(request, 'abs/beamsize_dropdown.html', context)


def load_beamselect(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    c = Bidpage.objects.filter(id=id).values('beamselect')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "c": c,
        "form": form,
    }
    return render(request, 'abs/load_beam_select.html', context)



def load_beaminfo(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    a = Bidpage.objects.all()
    form = BidPage(request.POST or None, instance=instance)
    beamselectB = Bidpage.objects.values('beamselect').get(id=id)
    beamtypeB = Bidpage.objects.values('beamtype1').get(id=id)
    beamsizeB = Bidpage.objects.values('beamsize1').get(id=id)
    beamtype1 = BeamTypeChoiceField
    beamsize1 = BeamSizeChoiceField
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "a": a,
        "beamselectB": beamselectB,
        "beamtypeB": beamtypeB,
        "beamsizeB": beamsizeB,
        "beamtype1": beamtype1,
        "beamsize1": beamsize1,
    }
    return render(request, 'abs/load_beaminfo.html', context)


def beamreset(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    Bidpage.objects.filter(id=id).update(beamselect=0, disabled=0)
    beamtype1 = BeamTypeChoiceField
    beamsize1 = BeamSizeChoiceField
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamtype1": beamtype1,
        "beamsize1": beamsize1,
    }
    return render(request, 'abs/bidpage.html', context)



def worktype(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_worktype']
    Bidpage.objects.filter(id=id).update(worktype_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)



def chfeet(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_chfeet1']
    Bidpage.objects.filter(id=id).update(chfeet1_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def chinches(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_chinches1']
    Bidpage.objects.filter(id=id).update(chinches1_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)

def qty1(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty1']
    Bidpage.objects.filter(id=id).update(qty1_id=d, beamlength1ft_id=0, beamlength1in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def qty1A(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty1']
    Bidpage.objects.filter(id=id).update(qty1_id=d, beamlength1ft_id=0, beamlength1in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_qty1(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength1ft_id = Bidpage.objects.values('beamlength1ft_id').get(id=id)
    beamlength1in_id = Bidpage.objects.values('beamlength1in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength1ft_id": beamlength1ft_id,
        "beamlength1in_id": beamlength1in_id,

    }
    return render(request, 'abs/bidpage.html', context)


def load_ft1_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength1ft_id = Bidpage.objects.values('beamlength1ft_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength1ft_id": beamlength1ft_id,

    }
    return render(request, 'abs/load_ft1_0.html', context)


def load_disable(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    disabledA = Bidpage.objects.values('disabled').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "disabledA": disabledA,
    }
    return render(request, 'abs/load_disable.html', context)


def ft1(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength1ft']
    Bidpage.objects.filter(id=id).update(beamlength1ft_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/load_ft1_0.html', context)


def inch1(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength1in']
    Bidpage.objects.filter(id=id).update(beamlength1in_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_in1_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength1in_id = Bidpage.objects.values('beamlength1in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength1in_id": beamlength1in_id,

    }
    return render(request, 'abs/load_in1_0.html', context)



def lcqty1(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lcqty1']
    Bidpage.objects.filter(id=id).update(lcqty1_id=d, lclength1_id=0, lctransition1_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def lclenght1(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lclength1']
    Bidpage.objects.filter(id=id).update(lclength1_id=d, lctransition1_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_lclenght1_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lclength1_id = Bidpage.objects.values('lclength1_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lclength1_id": lclength1_id,

    }
    return render(request, 'abs/load_lclenght1_0.html', context)


def lctransition1(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lctransition1']
    Bidpage.objects.filter(id=id).update(lctransition1_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_lctransition1_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lctransition1_id = Bidpage.objects.values('lctransition1_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lctransition1_id": lctransition1_id,

    }
    return render(request, 'abs/load_lctransition1_id_0.html', context)


def qty2(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty2']
    Bidpage.objects.filter(id=id).update(qty2_id=d, beamlength2ft_id=0, beamlength2in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def qty2A(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty2']
    Bidpage.objects.filter(id=id).update(qty2_id=d, beamlength2ft_id=0, beamlength2in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_qty2(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength2ft_id = Bidpage.objects.values('beamlength2ft_id').get(id=id)
    beamlength2in_id = Bidpage.objects.values('beamlength2in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength2ft_id": beamlength2ft_id,
        "beamlength2in_id": beamlength2in_id,

    }
    return render(request, 'abs/bidpage.html', context)


def ft2(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength2ft']
    Bidpage.objects.filter(id=id).update(beamlength2ft_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_ft2_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength2ft_id = Bidpage.objects.values('beamlength2ft_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength2ft_id": beamlength2ft_id,

    }
    return render(request, 'abs/load_ft2_0.html', context)


def inch2(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength2in']
    Bidpage.objects.filter(id=id).update(beamlength2in_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_in2_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength2in_id = Bidpage.objects.values('beamlength2in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength2in_id": beamlength2in_id,

    }
    return render(request, 'abs/load_in2_0.html', context)


def lcqty2(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lcqty2'] or 0
    Bidpage.objects.filter(id=id).update(lcqty2_id=d, lclength2_id=0, lctransition2_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def lclenght2(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lclength2']
    Bidpage.objects.filter(id=id).update(lclength2_id=d, lctransition2_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_lclenght2_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lclength2_id = Bidpage.objects.values('lclength2_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lclength2_id": lclength2_id,

    }
    return render(request, 'abs/load_lclenght2_0.html', context)


def lctransition2(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lctransition2']
    Bidpage.objects.filter(id=id).update(lctransition2_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_lctransition2_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lctransition2_id = Bidpage.objects.values('lctransition2_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lctransition2_id": lctransition2_id,
    }
    return render(request, 'abs/load_lctransition2_id_0.html', context)

def qty3(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty3']
    Bidpage.objects.filter(id=id).update(qty3_id=d, beamlength3ft_id=0, beamlength3in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def qty3A(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty3']
    Bidpage.objects.filter(id=id).update(qty3_id=d, beamlength3ft_id=0, beamlength3in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_qty3(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength3ft_id = Bidpage.objects.values('beamlength3ft_id').get(id=id)
    beamlength3in_id = Bidpage.objects.values('beamlength3in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength3ft_id": beamlength3ft_id,
        "beamlength3in_id": beamlength3in_id,

    }
    return render(request, 'abs/bidpage.html', context)


def ft3(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength3ft']
    Bidpage.objects.filter(id=id).update(beamlength3ft_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_ft3_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength3ft_id = Bidpage.objects.values('beamlength3ft_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength3ft_id": beamlength3ft_id,

    }
    return render(request, 'abs/load_ft3_0.html', context)


def inch3(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength3in']
    Bidpage.objects.filter(id=id).update(beamlength3in_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_in3_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength3in_id = Bidpage.objects.values('beamlength3in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength3in_id": beamlength3in_id,

    }
    return render(request, 'abs/load_in3_0.html', context)


def lcqty3(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lcqty3']
    Bidpage.objects.filter(id=id).update(lcqty3_id=d, lclength3_id=0, lctransition3_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def lcqty3A(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lcqty3']
    Bidpage.objects.filter(id=id).update(lcqty3_id=d, lclength3_id=0, lctransition3_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def lclenght3(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lclength3']
    Bidpage.objects.filter(id=id).update(lclength3_id=d, lctransition3_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_lclenght3_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lclength3_id = Bidpage.objects.values('lclength3_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lclength3_id": lclength3_id,

    }
    return render(request, 'abs/load_lclenght3_0.html', context)


def lctransition3(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lctransition3']
    Bidpage.objects.filter(id=id).update(lctransition3_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_lctransition3_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lctransition3_id = Bidpage.objects.values('lctransition3_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lctransition3_id": lctransition3_id,

    }
    return render(request, 'abs/load_lctransition3_id_0.html', context)


def qty4(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty4']
    Bidpage.objects.filter(id=id).update(qty4_id=d, beamlength4ft_id=0, beamlength4in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def qty4A(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty4']
    Bidpage.objects.filter(id=id).update(qty4_id=d, beamlength4ft_id=0, beamlength4in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_qty4(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength4ft_id = Bidpage.objects.values('beamlength4ft_id').get(id=id)
    beamlength4in_id = Bidpage.objects.values('beamlength4in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength4ft_id": beamlength4ft_id,
        "beamlength4in_id": beamlength4in_id,

    }
    return render(request, 'abs/bidpage.html', context)


def ft4(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength4ft']
    Bidpage.objects.filter(id=id).update(beamlength4ft_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_ft4_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength4ft_id = Bidpage.objects.values('beamlength4ft_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength4ft_id": beamlength4ft_id,

    }
    return render(request, 'abs/load_ft4_0.html', context)


def inch4(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength4in']
    Bidpage.objects.filter(id=id).update(beamlength4in_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_in4_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength4in_id = Bidpage.objects.values('beamlength4in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength4in_id": beamlength4in_id,

    }
    return render(request, 'abs/load_in4_0.html', context)


def lcqty4(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lcqty4']
    Bidpage.objects.filter(id=id).update(lcqty4_id=d, lclength4_id=0, lctransition4_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def lclenght4(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lclength4']
    Bidpage.objects.filter(id=id).update(lclength4_id=d, lctransition4_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_lclenght4_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lclength4_id = Bidpage.objects.values('lclength4_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lclength4_id": lclength4_id,

    }
    return render(request, 'abs/load_lclenght4_0.html', context)


def lctransition4(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lctransition4']
    Bidpage.objects.filter(id=id).update(lctransition4_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_lctransition4_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lctransition4_id = Bidpage.objects.values('lctransition4_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lctransition4_id": lctransition4_id,

    }
    return render(request, 'abs/load_lctransition4_id_0.html', context)


def qty5(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty5']
    Bidpage.objects.filter(id=id).update(qty5_id=d, beamlength5ft_id=0, beamlength5in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def qty5A(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty5']
    Bidpage.objects.filter(id=id).update(qty5_id=d, beamlength5ft_id=0, beamlength5in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_qty5(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength5ft_id = Bidpage.objects.values('beamlength5ft_id').get(id=id)
    beamlength5in_id = Bidpage.objects.values('beamlength5in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength5ft_id": beamlength5ft_id,
        "beamlength5in_id": beamlength5in_id,

    }
    return render(request, 'abs/bidpage.html', context)


def ft5(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength5ft']
    Bidpage.objects.filter(id=id).update(beamlength5ft_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_ft5_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength5ft_id = Bidpage.objects.values('beamlength5ft_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength5ft_id": beamlength5ft_id,

    }
    return render(request, 'abs/load_ft5_0.html', context)


def inch5(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength5in']
    Bidpage.objects.filter(id=id).update(beamlength5in_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_in5_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength5in_id = Bidpage.objects.values('beamlength5in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength5in_id": beamlength5in_id,

    }
    return render(request, 'abs/load_in5_0.html', context)


def lcqty5(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lcqty5']
    Bidpage.objects.filter(id=id).update(lcqty5_id=d, lclength5_id=0, lctransition5_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def lclenght5(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lclength5']
    Bidpage.objects.filter(id=id).update(lclength5_id=d, lctransition5_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_lclenght5_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lclength5_id = Bidpage.objects.values('lclength5_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lclength5_id": lclength5_id,

    }
    return render(request, 'abs/load_lclenght5_0.html', context)


def lctransition5(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lctransition5']
    Bidpage.objects.filter(id=id).update(lctransition5_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_lctransition5_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lctransition5_id = Bidpage.objects.values('lctransition5_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lctransition5_id": lctransition5_id,

    }
    return render(request, 'abs/load_lctransition5_id_0.html', context)


def qty6(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty6']
    Bidpage.objects.filter(id=id).update(qty6_id=d, beamlength6ft_id=0, beamlength6in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def qty6A(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_qty6']
    Bidpage.objects.filter(id=id).update(qty6_id=d, beamlength6ft_id=0, beamlength6in_id=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_qty6(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength6ft_id = Bidpage.objects.values('beamlength6ft_id').get(id=id)
    beamlength6in_id = Bidpage.objects.values('beamlength6in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength6ft_id": beamlength6ft_id,
        "beamlength6in_id": beamlength6in_id,

    }
    return render(request, 'abs/bidpage.html', context)


def ft6(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength6ft']
    Bidpage.objects.filter(id=id).update(beamlength6ft_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_ft6_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength6ft_id = Bidpage.objects.values('beamlength6ft_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength1ft_id": beamlength6ft_id,

    }
    return render(request, 'abs/load_ft6_0.html', context)


def inch6(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_beamlength6in']
    Bidpage.objects.filter(id=id).update(beamlength6in_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def load_in6_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    beamlength6in_id = Bidpage.objects.values('beamlength6in_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "beamlength6in_id": beamlength6in_id,

    }
    return render(request, 'abs/load_in6_0.html', context)


def lcqty6(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lcqty6']
    Bidpage.objects.filter(id=id).update(lcqty6_id=d, lclength6_id=0, lctransition6_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def lclenght6(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lclength6']
    Bidpage.objects.filter(id=id).update(lclength6_id=d, lctransition6_id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)



def load_lclenght6_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lclength6_id = Bidpage.objects.values('lclength6_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lclength6_id": lclength6_id,

    }
    return render(request, 'abs/load_lclenght6_0.html', context)


def lctransition6(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_lctransition6']
    Bidpage.objects.filter(id=id).update(lctransition6_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)



def load_lctransition6_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    lctransition6_id = Bidpage.objects.values('lctransition6_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "lctransition6_id": lctransition6_id,

    }
    return render(request, 'abs/load_lctransition6_id_0.html', context)


def jobcost(request, id=None):
    instance = JobCost.objects.get(bidid=id)
    form2 = CostJob(request.POST or None, instance=instance)
    a = JobCost.objects.values_list('materialcost', flat=True).get(bidid=id)
    b = JobCost.objects.values_list('laborcost', flat=True).get(bidid=id)
    c = a + b
    d = JobCost.objects.filter(bidid=id).update(totalcost=c)
    e = Bidpage.objects.values_list('prodqueue_id', flat=True).get(id=id)
    f = JobCost.objects.values_list('totalcost', flat=True).get(bidid=id)
    g = f * e
    h = f + g
    i = JobCost.objects.filter(bidid=id).update(increase=g, grandtotalcost=h)

    context = {
        "instance": instance,
        "form2": form2,
        "d": d,
        "i": i,

    }
    return redirect(instance.get_absolute5_url(), context)


def load_materialcost(request, id=None):
    instance = JobCost.objects.get(bidid=id)
    form = CostJob(request.POST or None, instance=instance)
    materialcostA = JobCost.objects.values('materialcost').get(bidid=id)
    laborcost = JobCost.objects.values('laborcost').get(bidid=id)
    totalcost= JobCost.objects.values('totalcost').get(bidid=id)
    increase = JobCost.objects.values('increase').get(bidid=id)
    grandtotalcost = JobCost.objects.values('grandtotalcost').get(bidid=id)
    context = {
        "instance": instance,
        "form": form,
        "grandtotalcost": grandtotalcost,
        "increase": increase,
        "totalcost": totalcost,
        "laborcost": laborcost,
        "materialcostA": materialcostA,

    }
    return render(request, 'abs/load_materialcost.html', context)


def increase(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_prodqueue']
    Bidpage.objects.filter(id=id).update(prodqueue_id=d)
    a = Bidpage.objects.values_list('prodqueue_id', flat=True).get(id=id)
    b = JobCost.objects.values_list('totalcost', flat=True).get(bidid=id)
    c = b * a
    e = JobCost.objects.filter(bidid=id).update(increase=c)
    f = JobCost.objects.values_list('increase', flat=True).get(bidid=id)
    g = b + f
    h = JobCost.objects.filter(bidid=id).update(grandtotalcost=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h,
    }
    return render(request, 'abs/bidpage.html', context)


def totals(request, id=None):
    instance = JobCost.objects.get(bidid=id)
    form = CostJob(request.POST or None, instance=instance)
    a = Bidpage.objects.values_list('qty1_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('beamlength1ft_id', flat=True).get(id=id)
    c = Bidpage.objects.values_list('beamlength1in_id', flat=True).get(id=id)
    d = 12
    e = c / d
    f = b + e
    g = a * f
    h = Bidpage.objects.values_list('beamsize1', flat=True).get(id=id)
    i = BeamInfo.objects.values_list('beam_cost', flat=True).get(beam_size=h)
    i2 = BeamInfo.objects.values_list('beam_labor', flat=True).get(beam_size=h)
    j = g * i
    j2 = g * i2
    k = Bidpage.objects.filter(id=id).update(beamcost1=j)
    k2 = Bidpage.objects.filter(id=id).update(lcost1=j2)
    t1 = Bidpage.objects.values_list('lclength1_id', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('lctransition1_id', flat=True).get(id=id)
    t3 = LallyColumn.objects.values_list('lally_cost', flat=True).get(lally_size=t1, lally_return=t2)
    t4 = Bidpage.objects.values_list('lcqty1_id', flat=True).get(id=id)
    t5 = t3 * t4
    t6 = Bidpage.objects.filter(id=id).update(lallycost1=t5)

    l = Bidpage.objects.values_list('beamcost1', flat=True).get(id=id)
    m = Bidpage.objects.values_list('beamcost2', flat=True).get(id=id)
    n = Bidpage.objects.values_list('beamcost3', flat=True).get(id=id)
    o = Bidpage.objects.values_list('beamcost4', flat=True).get(id=id)
    p = Bidpage.objects.values_list('beamcost5', flat=True).get(id=id)
    q = Bidpage.objects.values_list('beamcost6', flat=True).get(id=id)
    r = Bidpage.objects.values_list('footingmat', flat=True).get(id=id)
    s = Bidpage.objects.values_list('miscmat1', flat=True).get(id=id)
    t = Bidpage.objects.values_list('miscmat2', flat=True).get(id=id)
    u = Bidpage.objects.values_list('miscmat3', flat=True).get(id=id)
    v = Bidpage.objects.values_list('miscmat4', flat=True).get(id=id)
    v1 = Bidpage.objects.values_list('lallycost1', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('lallycost2', flat=True).get(id=id)
    v3 = Bidpage.objects.values_list('lallycost3', flat=True).get(id=id)
    v4 = Bidpage.objects.values_list('lallycost4', flat=True).get(id=id)
    v5 = Bidpage.objects.values_list('lallycost5', flat=True).get(id=id)
    v6 = Bidpage.objects.values_list('lallycost6', flat=True).get(id=id)
    w = l + m + n + o + p + q + r + s + t + u + v + v1 + v2 + v3 + v4 + v5 + v6
    l2 = Bidpage.objects.values_list('lcost1', flat=True).get(id=id)
    m2 = Bidpage.objects.values_list('lcost2', flat=True).get(id=id)
    n2 = Bidpage.objects.values_list('lcost3', flat=True).get(id=id)
    o2 = Bidpage.objects.values_list('lcost4', flat=True).get(id=id)
    p2 = Bidpage.objects.values_list('lcost5', flat=True).get(id=id)
    q2 = Bidpage.objects.values_list('lcost6', flat=True).get(id=id)
    r2 = Bidpage.objects.values_list('footinglabor', flat=True).get(id=id)
    s2 = Bidpage.objects.values_list('misclabor1', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('misclabor2', flat=True).get(id=id)
    u2 = Bidpage.objects.values_list('misclabor3', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('misclabor4', flat=True).get(id=id)
    w2 = l2 + m2 + n2 + o2 + p2 + q2 + r2 + s2 + t2 + u2 + v2
    x = JobCost.objects.filter(bidid=id).update(materialcost=w, laborcost=w2)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "k": k,
        "k2": k2,
        "t6": t6,
        "x": x,
    }
    return render(request, 'abs/bidpage.html', context)

def totals2(request, id=None):
    instance = JobCost.objects.get(bidid=id)
    form = CostJob(request.POST or None, instance=instance)
    a = Bidpage.objects.values_list('qty2_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('beamlength2ft_id', flat=True).get(id=id)
    c = Bidpage.objects.values_list('beamlength2in_id', flat=True).get(id=id)
    d = 12
    e = c / d
    f = b + e
    g = a * f
    h = Bidpage.objects.values_list('beamsize1', flat=True).get(id=id)
    i = BeamInfo.objects.values_list('beam_cost', flat=True).get(beam_size=h)
    i2 = BeamInfo.objects.values_list('beam_labor', flat=True).get(beam_size=h)
    j = g * i
    j2 = g * i2
    k = Bidpage.objects.filter(id=id).update(beamcost2=j)
    k2 = Bidpage.objects.filter(id=id).update(lcost2=j2)
    t1 = Bidpage.objects.values_list('lclength2_id', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('lctransition2_id', flat=True).get(id=id)
    t3 = LallyColumn.objects.values_list('lally_cost', flat=True).get(lally_size=t1, lally_return=t2)
    t4 = Bidpage.objects.values_list('lcqty2_id', flat=True).get(id=id)
    t5 = t3 * t4
    t6 = Bidpage.objects.filter(id=id).update(lallycost2=t5)


    l = Bidpage.objects.values_list('beamcost1', flat=True).get(id=id)
    m = Bidpage.objects.values_list('beamcost2', flat=True).get(id=id)
    n = Bidpage.objects.values_list('beamcost3', flat=True).get(id=id)
    o = Bidpage.objects.values_list('beamcost4', flat=True).get(id=id)
    p = Bidpage.objects.values_list('beamcost5', flat=True).get(id=id)
    q = Bidpage.objects.values_list('beamcost6', flat=True).get(id=id)
    r = Bidpage.objects.values_list('footingmat', flat=True).get(id=id)
    s = Bidpage.objects.values_list('miscmat1', flat=True).get(id=id)
    t = Bidpage.objects.values_list('miscmat2', flat=True).get(id=id)
    u = Bidpage.objects.values_list('miscmat3', flat=True).get(id=id)
    v = Bidpage.objects.values_list('miscmat4', flat=True).get(id=id)
    v1 = Bidpage.objects.values_list('lallycost1', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('lallycost2', flat=True).get(id=id)
    v3 = Bidpage.objects.values_list('lallycost3', flat=True).get(id=id)
    v4 = Bidpage.objects.values_list('lallycost4', flat=True).get(id=id)
    v5 = Bidpage.objects.values_list('lallycost5', flat=True).get(id=id)
    v6 = Bidpage.objects.values_list('lallycost6', flat=True).get(id=id)
    w = l + m + n + o + p + q + r + s + t + u + v + v1 + v2 + v3 + v4 + v5 + v6
    l2 = Bidpage.objects.values_list('lcost1', flat=True).get(id=id)
    m2 = Bidpage.objects.values_list('lcost2', flat=True).get(id=id)
    n2 = Bidpage.objects.values_list('lcost3', flat=True).get(id=id)
    o2 = Bidpage.objects.values_list('lcost4', flat=True).get(id=id)
    p2 = Bidpage.objects.values_list('lcost5', flat=True).get(id=id)
    q2 = Bidpage.objects.values_list('lcost6', flat=True).get(id=id)
    r2 = Bidpage.objects.values_list('footinglabor', flat=True).get(id=id)
    s2 = Bidpage.objects.values_list('misclabor1', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('misclabor2', flat=True).get(id=id)
    u2 = Bidpage.objects.values_list('misclabor3', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('misclabor4', flat=True).get(id=id)
    w2 = l2 + m2+ n2 + o2 + p2 + q2 + r2 + s2 + t2 + u2 + v2
    x = JobCost.objects.filter(bidid=id).update(materialcost=w, laborcost=w2)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "k": k,
        "k2": k2,
        "x": x,
        "t6": t6,
    }
    return render(request, 'abs/bidpage.html', context)


def totals3(request, id=None):
    instance = JobCost.objects.get(bidid=id)
    form = CostJob(request.POST or None, instance=instance)
    a = Bidpage.objects.values_list('qty3_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('beamlength3ft_id', flat=True).get(id=id)
    c = Bidpage.objects.values_list('beamlength3in_id', flat=True).get(id=id)
    d = 12
    e = c / d
    f = b + e
    g = a * f
    h = Bidpage.objects.values_list('beamsize1', flat=True).get(id=id)
    i = BeamInfo.objects.values_list('beam_cost', flat=True).get(beam_size=h)
    i2 = BeamInfo.objects.values_list('beam_labor', flat=True).get(beam_size=h)
    j = g * i
    j2 = g * i2
    k = Bidpage.objects.filter(id=id).update(beamcost3=j)
    k2 = Bidpage.objects.filter(id=id).update(lcost3=j2)
    t1 = Bidpage.objects.values_list('lclength3_id', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('lctransition3_id', flat=True).get(id=id)
    t3 = LallyColumn.objects.values_list('lally_cost', flat=True).get(lally_size=t1, lally_return=t2)
    t4 = Bidpage.objects.values_list('lcqty3_id', flat=True).get(id=id)
    t5 = t3 * t4
    t6 = Bidpage.objects.filter(id=id).update(lallycost3=t5)

    l = Bidpage.objects.values_list('beamcost1', flat=True).get(id=id)
    m = Bidpage.objects.values_list('beamcost2', flat=True).get(id=id)
    n = Bidpage.objects.values_list('beamcost3', flat=True).get(id=id)
    o = Bidpage.objects.values_list('beamcost4', flat=True).get(id=id)
    p = Bidpage.objects.values_list('beamcost5', flat=True).get(id=id)
    q = Bidpage.objects.values_list('beamcost6', flat=True).get(id=id)
    r = Bidpage.objects.values_list('footingmat', flat=True).get(id=id)
    s = Bidpage.objects.values_list('miscmat1', flat=True).get(id=id)
    t = Bidpage.objects.values_list('miscmat2', flat=True).get(id=id)
    u = Bidpage.objects.values_list('miscmat3', flat=True).get(id=id)
    v = Bidpage.objects.values_list('miscmat4', flat=True).get(id=id)
    v1 = Bidpage.objects.values_list('lallycost1', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('lallycost2', flat=True).get(id=id)
    v3 = Bidpage.objects.values_list('lallycost3', flat=True).get(id=id)
    v4 = Bidpage.objects.values_list('lallycost4', flat=True).get(id=id)
    v5 = Bidpage.objects.values_list('lallycost5', flat=True).get(id=id)
    v6 = Bidpage.objects.values_list('lallycost6', flat=True).get(id=id)
    w = l + m + n + o + p + q + r + s + t + u + v + v1 + v2 + v3 + v4 + v5 + v6
    l2 = Bidpage.objects.values_list('lcost1', flat=True).get(id=id)
    m2 = Bidpage.objects.values_list('lcost2', flat=True).get(id=id)
    n2 = Bidpage.objects.values_list('lcost3', flat=True).get(id=id)
    o2 = Bidpage.objects.values_list('lcost4', flat=True).get(id=id)
    p2 = Bidpage.objects.values_list('lcost5', flat=True).get(id=id)
    q2 = Bidpage.objects.values_list('lcost6', flat=True).get(id=id)
    r2 = Bidpage.objects.values_list('footinglabor', flat=True).get(id=id)
    s2 = Bidpage.objects.values_list('misclabor1', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('misclabor2', flat=True).get(id=id)
    u2 = Bidpage.objects.values_list('misclabor3', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('misclabor4', flat=True).get(id=id)
    w2 = l2 + m2+ n2 + o2 + p2 + q2 + r2 + s2 + t2 + u2 + v2
    x = JobCost.objects.filter(bidid=id).update(materialcost=w, laborcost=w2)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "k": k,
        "k2": k2,
        "x": x,
        "t6": t6,
    }
    return render(request, 'abs/bidpage.html', context)


def totals4(request, id=None):
    instance = JobCost.objects.get(bidid=id)
    form = CostJob(request.POST or None, instance=instance)
    a = Bidpage.objects.values_list('qty4_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('beamlength4ft_id', flat=True).get(id=id)
    c = Bidpage.objects.values_list('beamlength4in_id', flat=True).get(id=id)
    d = 12
    e = c / d
    f = b + e
    g = a * f
    h = Bidpage.objects.values_list('beamsize1', flat=True).get(id=id)
    i = BeamInfo.objects.values_list('beam_cost', flat=True).get(beam_size=h)
    i2 = BeamInfo.objects.values_list('beam_labor', flat=True).get(beam_size=h)
    j = g * i
    j2 = g * i2
    k = Bidpage.objects.filter(id=id).update(beamcost4=j)
    k2 = Bidpage.objects.filter(id=id).update(lcost4=j2)

    t1 = Bidpage.objects.values_list('lclength4_id', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('lctransition4_id', flat=True).get(id=id)
    t3 = LallyColumn.objects.values_list('lally_cost', flat=True).get(lally_size=t1, lally_return=t2)
    t4 = Bidpage.objects.values_list('lcqty4_id', flat=True).get(id=id)
    t5 = t3 * t4
    t6 = Bidpage.objects.filter(id=id).update(lallycost4=t5)
    l = Bidpage.objects.values_list('beamcost1', flat=True).get(id=id)
    m = Bidpage.objects.values_list('beamcost2', flat=True).get(id=id)
    n = Bidpage.objects.values_list('beamcost3', flat=True).get(id=id)
    o = Bidpage.objects.values_list('beamcost4', flat=True).get(id=id)
    p = Bidpage.objects.values_list('beamcost5', flat=True).get(id=id)
    q = Bidpage.objects.values_list('beamcost6', flat=True).get(id=id)
    r = Bidpage.objects.values_list('footingmat', flat=True).get(id=id)
    s = Bidpage.objects.values_list('miscmat1', flat=True).get(id=id)
    t = Bidpage.objects.values_list('miscmat2', flat=True).get(id=id)
    u = Bidpage.objects.values_list('miscmat3', flat=True).get(id=id)
    v = Bidpage.objects.values_list('miscmat4', flat=True).get(id=id)
    v1 = Bidpage.objects.values_list('lallycost1', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('lallycost2', flat=True).get(id=id)
    v3 = Bidpage.objects.values_list('lallycost3', flat=True).get(id=id)
    v4 = Bidpage.objects.values_list('lallycost4', flat=True).get(id=id)
    v5 = Bidpage.objects.values_list('lallycost5', flat=True).get(id=id)
    v6 = Bidpage.objects.values_list('lallycost6', flat=True).get(id=id)
    w = l + m + n + o + p + q + r + s + t + u + v + v1 + v2 + v3 + v4 + v5 + v6
    l2 = Bidpage.objects.values_list('lcost1', flat=True).get(id=id)
    m2 = Bidpage.objects.values_list('lcost2', flat=True).get(id=id)
    n2 = Bidpage.objects.values_list('lcost3', flat=True).get(id=id)
    o2 = Bidpage.objects.values_list('lcost4', flat=True).get(id=id)
    p2 = Bidpage.objects.values_list('lcost5', flat=True).get(id=id)
    q2 = Bidpage.objects.values_list('lcost6', flat=True).get(id=id)
    r2 = Bidpage.objects.values_list('footinglabor', flat=True).get(id=id)
    s2 = Bidpage.objects.values_list('misclabor1', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('misclabor2', flat=True).get(id=id)
    u2 = Bidpage.objects.values_list('misclabor3', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('misclabor4', flat=True).get(id=id)
    w2 = l2 + m2+ n2 + o2 + p2 + q2 + r2 + s2 + t2 + u2 + v2
    x = JobCost.objects.filter(bidid=id).update(materialcost=w, laborcost=w2)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "k": k,
        "k2": k2,
        "x": x,
        "t6": t6,
    }
    return render(request, 'abs/bidpage.html', context)


def totals5(request, id=None):
    instance = JobCost.objects.get(bidid=id)
    form = CostJob(request.POST or None, instance=instance)
    a = Bidpage.objects.values_list('qty5_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('beamlength5ft_id', flat=True).get(id=id)
    c = Bidpage.objects.values_list('beamlength5in_id', flat=True).get(id=id)
    d = 12
    e = c / d
    f = b + e
    g = a * f
    h = Bidpage.objects.values_list('beamsize1', flat=True).get(id=id)
    i = BeamInfo.objects.values_list('beam_cost', flat=True).get(beam_size=h)
    i2 = BeamInfo.objects.values_list('beam_labor', flat=True).get(beam_size=h)
    j = g * i
    j2 = g * i2
    k = Bidpage.objects.filter(id=id).update(beamcost5=j)
    k2 = Bidpage.objects.filter(id=id).update(lcost5=j2)
    t1 = Bidpage.objects.values_list('lclength5_id', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('lctransition5_id', flat=True).get(id=id)
    t3 = LallyColumn.objects.values_list('lally_cost', flat=True).get(lally_size=t1, lally_return=t2)
    t4 = Bidpage.objects.values_list('lcqty5_id', flat=True).get(id=id)
    t5 = t3 * t4
    t6 = Bidpage.objects.filter(id=id).update(lallycost5=t5)
    l = Bidpage.objects.values_list('beamcost1', flat=True).get(id=id)
    m = Bidpage.objects.values_list('beamcost2', flat=True).get(id=id)
    n = Bidpage.objects.values_list('beamcost3', flat=True).get(id=id)
    o = Bidpage.objects.values_list('beamcost4', flat=True).get(id=id)
    p = Bidpage.objects.values_list('beamcost5', flat=True).get(id=id)
    q = Bidpage.objects.values_list('beamcost6', flat=True).get(id=id)
    r = Bidpage.objects.values_list('footingmat', flat=True).get(id=id)
    s = Bidpage.objects.values_list('miscmat1', flat=True).get(id=id)
    t = Bidpage.objects.values_list('miscmat2', flat=True).get(id=id)
    u = Bidpage.objects.values_list('miscmat3', flat=True).get(id=id)
    v = Bidpage.objects.values_list('miscmat4', flat=True).get(id=id)
    v1 = Bidpage.objects.values_list('lallycost1', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('lallycost2', flat=True).get(id=id)
    v3 = Bidpage.objects.values_list('lallycost3', flat=True).get(id=id)
    v4 = Bidpage.objects.values_list('lallycost4', flat=True).get(id=id)
    v5 = Bidpage.objects.values_list('lallycost5', flat=True).get(id=id)
    v6 = Bidpage.objects.values_list('lallycost6', flat=True).get(id=id)
    w = l + m + n + o + p + q + r + s + t + u + v + v1 + v2 + v3 + v4 + v5 + v6
    l2 = Bidpage.objects.values_list('lcost1', flat=True).get(id=id)
    m2 = Bidpage.objects.values_list('lcost2', flat=True).get(id=id)
    n2 = Bidpage.objects.values_list('lcost3', flat=True).get(id=id)
    o2 = Bidpage.objects.values_list('lcost4', flat=True).get(id=id)
    p2 = Bidpage.objects.values_list('lcost5', flat=True).get(id=id)
    q2 = Bidpage.objects.values_list('lcost6', flat=True).get(id=id)
    r2 = Bidpage.objects.values_list('footinglabor', flat=True).get(id=id)
    s2 = Bidpage.objects.values_list('misclabor1', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('misclabor2', flat=True).get(id=id)
    u2 = Bidpage.objects.values_list('misclabor3', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('misclabor4', flat=True).get(id=id)
    w2 = l2 + m2+ n2 + o2 + p2 + q2 + r2 + s2 + t2 + u2 + v2
    x = JobCost.objects.filter(bidid=id).update(materialcost=w, laborcost=w2)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "k": k,
        "k2": k2,
        "x": x,
        "t6": t6,
    }
    return render(request, 'abs/bidpage.html', context)


def totals6(request, id=None):
    instance = JobCost.objects.get(bidid=id)
    form = CostJob(request.POST or None, instance=instance)
    a = Bidpage.objects.values_list('qty6_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('beamlength6ft_id', flat=True).get(id=id)
    c = Bidpage.objects.values_list('beamlength6in_id', flat=True).get(id=id)
    d = 12
    e = c / d
    f = b + e
    g = a * f
    h = Bidpage.objects.values_list('beamsize1', flat=True).get(id=id)
    i = BeamInfo.objects.values_list('beam_cost', flat=True).get(beam_size=h)
    i2 = BeamInfo.objects.values_list('beam_labor', flat=True).get(beam_size=h)
    j = g * i
    j2 = g * i2
    k = Bidpage.objects.filter(id=id).update(beamcost6=j)
    k2 = Bidpage.objects.filter(id=id).update(lcost6=j2)
    t1 = Bidpage.objects.values_list('lclength6_id', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('lctransition6_id', flat=True).get(id=id)
    t3 = LallyColumn.objects.values_list('lally_cost', flat=True).get(lally_size=t1, lally_return=t2)
    t4 = Bidpage.objects.values_list('lcqty6_id', flat=True).get(id=id)
    t5 = t3 * t4
    t6 = Bidpage.objects.filter(id=id).update(lallycost6=t5)
    l = Bidpage.objects.values_list('beamcost1', flat=True).get(id=id)
    m = Bidpage.objects.values_list('beamcost2', flat=True).get(id=id)
    n = Bidpage.objects.values_list('beamcost3', flat=True).get(id=id)
    o = Bidpage.objects.values_list('beamcost4', flat=True).get(id=id)
    p = Bidpage.objects.values_list('beamcost5', flat=True).get(id=id)
    q = Bidpage.objects.values_list('beamcost6', flat=True).get(id=id)
    r = Bidpage.objects.values_list('footingmat', flat=True).get(id=id)
    s = Bidpage.objects.values_list('miscmat1', flat=True).get(id=id)
    t = Bidpage.objects.values_list('miscmat2', flat=True).get(id=id)
    u = Bidpage.objects.values_list('miscmat3', flat=True).get(id=id)
    v = Bidpage.objects.values_list('miscmat4', flat=True).get(id=id)
    v1 = Bidpage.objects.values_list('lallycost1', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('lallycost2', flat=True).get(id=id)
    v3 = Bidpage.objects.values_list('lallycost3', flat=True).get(id=id)
    v4 = Bidpage.objects.values_list('lallycost4', flat=True).get(id=id)
    v5 = Bidpage.objects.values_list('lallycost5', flat=True).get(id=id)
    v6 = Bidpage.objects.values_list('lallycost6', flat=True).get(id=id)
    w = l + m + n + o + p + q + r + s + t + u + v + v1 + v2 + v3 + v4 + v5 + v6
    l2 = Bidpage.objects.values_list('lcost1', flat=True).get(id=id)
    m2 = Bidpage.objects.values_list('lcost2', flat=True).get(id=id)
    n2 = Bidpage.objects.values_list('lcost3', flat=True).get(id=id)
    o2 = Bidpage.objects.values_list('lcost4', flat=True).get(id=id)
    p2 = Bidpage.objects.values_list('lcost5', flat=True).get(id=id)
    q2 = Bidpage.objects.values_list('lcost6', flat=True).get(id=id)
    r2 = Bidpage.objects.values_list('footinglabor', flat=True).get(id=id)
    s2 = Bidpage.objects.values_list('misclabor1', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('misclabor2', flat=True).get(id=id)
    u2 = Bidpage.objects.values_list('misclabor3', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('misclabor4', flat=True).get(id=id)
    w2 = l2 + m2+ n2 + o2 + p2 + q2 + r2 + s2 + t2 + u2 + v2
    x = JobCost.objects.filter(bidid=id).update(materialcost=w, laborcost=w2)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "k": k,
        "k2": k2,
        "x": x,
        "t6": t6,
    }
    return render(request, 'abs/bidpage.html', context)


def footingqty(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_footingqty']
    Bidpage.objects.filter(id=id).update(footingqty_id=d, footingsize_id=1, footinglabor=0, footingmat=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def footingsize(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_footingsize']
    Bidpage.objects.filter(id=id).update(footingsize_id=d)
    a = Bidpage.objects.values_list('footingqty_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('footingsize_id', flat=True).get(id=id)
    c = FootingSize.objects.values_list('footing_cost', flat=True).get(id=b)
    d = FootingSize.objects.values_list('footing_labor', flat=True).get(id=b)
    e = a * c
    f = a * d
    h = Bidpage.objects.filter(id=id).update(footinglabor=f)
    i = Bidpage.objects.filter(id=id).update(footingmat=e)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "i": i,
        "h": h,
    }
    return render(request, 'abs/bidpage.html', context)


def load_footingsize_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    footingsize_id = Bidpage.objects.values('footingsize_id').get(id=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "footingsize_id": footingsize_id,

    }
    return render(request, 'abs/load_footingsize_0.html', context)


def totalsfootingsize(request, id=None):
    instance = JobCost.objects.get(bidid=id)
    form = CostJob(request.POST or None, instance=instance)
    a = Bidpage.objects.values_list('footingqty_id', flat=True).get(id=id)
    h = Bidpage.objects.values_list('footingsize_id', flat=True).get(id=id)
    i = FootingSize.objects.values_list('footing_cost', flat=True).get(id=h)
    i2 = FootingSize.objects.values_list('footing_labor', flat=True).get(id=h)
    j = a * i
    j2 = a * i2
    k = Bidpage.objects.filter(id=id).update(footingmatcost=j)
    k2 = Bidpage.objects.filter(id=id).update(footinglaborcost=j2)

    l = Bidpage.objects.values_list('beamcost1', flat=True).get(id=id)
    m = Bidpage.objects.values_list('beamcost2', flat=True).get(id=id)
    n = Bidpage.objects.values_list('beamcost3', flat=True).get(id=id)
    o = Bidpage.objects.values_list('beamcost4', flat=True).get(id=id)
    p = Bidpage.objects.values_list('beamcost5', flat=True).get(id=id)
    q = Bidpage.objects.values_list('beamcost6', flat=True).get(id=id)
    r = Bidpage.objects.values_list('footingmatcost', flat=True).get(id=id)
    s = Bidpage.objects.values_list('miscmat1', flat=True).get(id=id)
    t = Bidpage.objects.values_list('miscmat2', flat=True).get(id=id)
    u = Bidpage.objects.values_list('miscmat3', flat=True).get(id=id)
    v = Bidpage.objects.values_list('miscmat4', flat=True).get(id=id)
    v1 = Bidpage.objects.values_list('lallycost1', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('lallycost2', flat=True).get(id=id)
    v3 = Bidpage.objects.values_list('lallycost3', flat=True).get(id=id)
    v4 = Bidpage.objects.values_list('lallycost4', flat=True).get(id=id)
    v5 = Bidpage.objects.values_list('lallycost5', flat=True).get(id=id)
    v6 = Bidpage.objects.values_list('lallycost6', flat=True).get(id=id)
    w = l + m + n + o + p + q + r + s + t + u + v + v1 + v2 + v3 + v4 + v5 + v6
    l2 = Bidpage.objects.values_list('lcost1', flat=True).get(id=id)
    m2 = Bidpage.objects.values_list('lcost2', flat=True).get(id=id)
    n2 = Bidpage.objects.values_list('lcost3', flat=True).get(id=id)
    o2 = Bidpage.objects.values_list('lcost4', flat=True).get(id=id)
    p2 = Bidpage.objects.values_list('lcost5', flat=True).get(id=id)
    q2 = Bidpage.objects.values_list('lcost6', flat=True).get(id=id)
    r2 = Bidpage.objects.values_list('footinglaborcost', flat=True).get(id=id)
    s2 = Bidpage.objects.values_list('misclabor1', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('misclabor2', flat=True).get(id=id)
    u2 = Bidpage.objects.values_list('misclabor3', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('misclabor4', flat=True).get(id=id)
    w2 = l2 + m2+ n2 + o2 + p2 + q2 + r2 + s2 + t2 + u2 + v2
    x = JobCost.objects.filter(bidid=id).update(materialcost=w, laborcost=w2)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "k": k,
        "k2": k2,
        "x": x,
    }
    return render(request, 'abs/bidpage.html', context)


def misc1qty(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_miscqty1']
    Bidpage.objects.filter(id=id).update(miscqty1_id=d, miscdescription1='', misclabor1=0, miscmat1=0, misclaborcost1=0,
                                         miscmatcost1=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def misc1descrip(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['miscdescription1']
    Bidpage.objects.filter(id=id).update(miscdescription1=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def misc1mat(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['miscmat1']
    Bidpage.objects.filter(id=id).update(miscmat1=d)
    a = Bidpage.objects.values_list('miscqty1_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('miscmat1', flat=True).get(id=id)
    c = a * b
    e = Bidpage.objects.filter(id=id).update(miscmatcost1=c)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'abs/bidpage.html', context)


def misc1labor(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['misclabor1']
    Bidpage.objects.filter(id=id).update(misclabor1=d)
    a = Bidpage.objects.values_list('miscqty1_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('misclabor1', flat=True).get(id=id)
    c = a * b
    e = Bidpage.objects.filter(id=id).update(misclaborcost1=c)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'abs/bidpage.html', context)


def misctotal(request, id=None):
    instance = JobCost.objects.get(bidid=id)
    form = CostJob(request.POST or None, instance=instance)
    l = Bidpage.objects.values_list('beamcost1', flat=True).get(id=id)
    m = Bidpage.objects.values_list('beamcost2', flat=True).get(id=id)
    n = Bidpage.objects.values_list('beamcost3', flat=True).get(id=id)
    o = Bidpage.objects.values_list('beamcost4', flat=True).get(id=id)
    p = Bidpage.objects.values_list('beamcost5', flat=True).get(id=id)
    q = Bidpage.objects.values_list('beamcost6', flat=True).get(id=id)
    r = Bidpage.objects.values_list('footingmatcost', flat=True).get(id=id)
    s = Bidpage.objects.values_list('miscmatcost1', flat=True).get(id=id)
    t = Bidpage.objects.values_list('miscmatcost2', flat=True).get(id=id)
    u = Bidpage.objects.values_list('miscmatcost3', flat=True).get(id=id)
    v = Bidpage.objects.values_list('miscmatcost4', flat=True).get(id=id)
    v1 = Bidpage.objects.values_list('lallycost1', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('lallycost2', flat=True).get(id=id)
    v3 = Bidpage.objects.values_list('lallycost3', flat=True).get(id=id)
    v4 = Bidpage.objects.values_list('lallycost4', flat=True).get(id=id)
    v5 = Bidpage.objects.values_list('lallycost5', flat=True).get(id=id)
    v6 = Bidpage.objects.values_list('lallycost6', flat=True).get(id=id)
    w = l + m + n + o + p + q + r + s + t + u + v + v1 + v2 + v3 + v4 + v5 + v6
    l2 = Bidpage.objects.values_list('lcost1', flat=True).get(id=id)
    m2 = Bidpage.objects.values_list('lcost2', flat=True).get(id=id)
    n2 = Bidpage.objects.values_list('lcost3', flat=True).get(id=id)
    o2 = Bidpage.objects.values_list('lcost4', flat=True).get(id=id)
    p2 = Bidpage.objects.values_list('lcost5', flat=True).get(id=id)
    q2 = Bidpage.objects.values_list('lcost6', flat=True).get(id=id)
    r2 = Bidpage.objects.values_list('footinglaborcost', flat=True).get(id=id)
    s2 = Bidpage.objects.values_list('misclaborcost1', flat=True).get(id=id)
    t2 = Bidpage.objects.values_list('misclaborcost2', flat=True).get(id=id)
    u2 = Bidpage.objects.values_list('misclaborcost3', flat=True).get(id=id)
    v2 = Bidpage.objects.values_list('misclaborcost4', flat=True).get(id=id)
    w2 = l2 + m2+ n2 + o2 + p2 + q2 + r2 + s2 + t2 + u2 + v2
    x = JobCost.objects.filter(bidid=id).update(materialcost=w, laborcost=w2)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "x": x,
    }
    return render(request, 'abs/bidpage.html', context)


def load_misc1descrip_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    miscdescription1A = Bidpage.objects.values('miscdescription1').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "miscdescription1A": miscdescription1A,

    }
    return render(request, 'abs/load_misc1descrip_0.html', context)


def load_misc1mat_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    miscmat1A = Bidpage.objects.values('miscmat1').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "miscmat1A": miscmat1A,

    }
    return render(request, 'abs/load_misc1mat_0.html', context)


def load_misc1labor_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    misclabor1A = Bidpage.objects.values('misclabor1').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "misclabor1A": misclabor1A,

    }
    return render(request, 'abs/load_misc1labor_0.html', context)


def misc2qty(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_miscqty2']
    Bidpage.objects.filter(id=id).update(miscqty2_id=d, miscdescription2='', misclabor2=0, miscmat2=0, misclaborcost2=0,
                                         miscmatcost2=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def misc2descrip(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['miscdescription2']
    Bidpage.objects.filter(id=id).update(miscdescription2=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def misc2mat(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['miscmat2']
    Bidpage.objects.filter(id=id).update(miscmat2=d)
    a = Bidpage.objects.values_list('miscqty2_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('miscmat2', flat=True).get(id=id)
    c = a * b
    e = Bidpage.objects.filter(id=id).update(miscmatcost2=c)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'abs/bidpage.html', context)


def misc2labor(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['misclabor2']
    Bidpage.objects.filter(id=id).update(misclabor2=d)
    a = Bidpage.objects.values_list('miscqty2_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('misclabor2', flat=True).get(id=id)
    c = a * b
    e = Bidpage.objects.filter(id=id).update(misclaborcost2=c)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'abs/bidpage.html', context)

def load_misc2descrip_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    miscdescription2A = Bidpage.objects.values('miscdescription2').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "miscdescription2A": miscdescription2A,

    }
    return render(request, 'abs/load_misc2descrip_0.html', context)


def load_misc2mat_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    miscmat2A = Bidpage.objects.values('miscmat2').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "miscmat2A": miscmat2A,

    }
    return render(request, 'abs/load_misc2mat_0.html', context)


def load_misc2labor_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    misclabor2A = Bidpage.objects.values('misclabor2').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "misclabor2A": misclabor2A,

    }
    return render(request, 'abs/load_misc2labor_0.html', context)


def misc3qty(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_miscqty3']
    Bidpage.objects.filter(id=id).update(miscqty3_id=d, miscdescription3='', misclabor3=0, miscmat3=0, misclaborcost3=0,
                                         miscmatcost3=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def misc3descrip(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['miscdescription3']
    Bidpage.objects.filter(id=id).update(miscdescription3=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def misc3mat(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['miscmat3']
    Bidpage.objects.filter(id=id).update(miscmat3=d)
    a = Bidpage.objects.values_list('miscqty3_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('miscmat3', flat=True).get(id=id)
    c = a * b
    e = Bidpage.objects.filter(id=id).update(miscmatcost3=c)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'abs/bidpage.html', context)


def misc3labor(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['misclabor3']
    Bidpage.objects.filter(id=id).update(misclabor3=d)
    a = Bidpage.objects.values_list('miscqty3_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('misclabor3', flat=True).get(id=id)
    c = a * b
    e = Bidpage.objects.filter(id=id).update(misclaborcost3=c)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'abs/bidpage.html', context)

def load_misc3descrip_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    miscdescription3A = Bidpage.objects.values('miscdescription3').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "miscdescription3A": miscdescription3A,

    }
    return render(request, 'abs/load_misc3descrip_0.html', context)


def load_misc3mat_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    miscmat3A = Bidpage.objects.values('miscmat3').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "miscmat3A": miscmat3A,

    }
    return render(request, 'abs/load_misc3mat_0.html', context)


def load_misc3labor_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    misclabor3A = Bidpage.objects.values('misclabor3').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "misclabor3A": misclabor3A,

    }
    return render(request, 'abs/load_misc3labor_0.html', context)


def misc4qty(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['id_miscqty4']
    Bidpage.objects.filter(id=id).update(miscqty4_id=d, miscdescription4='', misclabor4=0, miscmat4=0, misclaborcost4=0,
                                         miscmatcost4=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def misc4descrip(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['miscdescription4']
    Bidpage.objects.filter(id=id).update(miscdescription4=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/bidpage.html', context)


def misc4mat(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['miscmat4']
    Bidpage.objects.filter(id=id).update(miscmat4=d)
    a = Bidpage.objects.values_list('miscqty4_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('miscmat4', flat=True).get(id=id)
    c = a * b
    e = Bidpage.objects.filter(id=id).update(miscmatcost4=c)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'abs/bidpage.html', context)


def misc4labor(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    d = request.POST['misclabor4']
    Bidpage.objects.filter(id=id).update(misclabor4=d)
    a = Bidpage.objects.values_list('miscqty4_id', flat=True).get(id=id)
    b = Bidpage.objects.values_list('misclabor4', flat=True).get(id=id)
    c = a * b
    e = Bidpage.objects.filter(id=id).update(misclaborcost4=c)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'abs/bidpage.html', context)

def load_misc4descrip_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    miscdescription4A = Bidpage.objects.values('miscdescription4').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "miscdescription4A": miscdescription4A,

    }
    return render(request, 'abs/load_misc4descrip_0.html', context)


def load_misc4mat_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    miscmat4A = Bidpage.objects.values('miscmat4').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "miscmat4A": miscmat4A,

    }
    return render(request, 'abs/load_misc4mat_0.html', context)


def load_misc4labor_0(request, id=None):
    instance = get_object_or_404(Bidpage, id=id)
    form = BidPage(request.POST or None, instance=instance)
    misclabor4A = Bidpage.objects.values('misclabor4').get(bidid=id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "misclabor4A": misclabor4A,

    }
    return render(request, 'abs/load_misc4labor_0.html', context)


def contract(request, bidid):
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    a = Contract.objects.filter(bidid=bidid).values()
    b = Contract.objects.values_list('custid', flat=True).get(bidid=bidid)
    c = JobCost.objects.values_list('grandtotalcost', flat=True).get(bidid=bidid)
    d = Contract.objects.filter(bidid=bidid).update(grandtotalcost=c)
    queryset = CustomerInfo.objects.filter(custid=b)
    queryset2 = Contract.objects.filter(custid=b)
    instance3 = CustomerInfo.objects.order_by('id').get(custid=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute5_url())
    context = {
        "instance": instance,
        "form": form,
        "a": a,
        "object_list": queryset,
        "object_list2": queryset2,
        "d": d,
        "instance3": instance3,
    }
    return render(request, 'abs/contract.html', context)


def depositterms(request, bidid):
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['depositterms']
    e = Contract.objects.filter(bidid=bidid).update(depositterms_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'abs/contract.html', context)


def load_depositterms(request, bidid):
    a = Contract.objects.all()
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('depositterms_id').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/deposit_terms.html', context)


def terms2(request, bidid):
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['terms2']
    e = Contract.objects.filter(bidid=bidid).update(term2_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'abs/contract.html', context)


def load_terms2(request, bidid):
    a = Contract.objects.all()
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('term2_id').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/terms_2.html', context)


def terms3(request, bidid):
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['terms3']
    e = Contract.objects.filter(bidid=bidid).update(term3_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'abs/contract.html', context)


def load_terms3(request, bidid):
    a = Contract.objects.all()
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('term3_id').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/terms_3.html', context)


def termsfinal(request, bidid):
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['termsfinal']
    e = Contract.objects.filter(bidid=bidid).update(termsfinal=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'abs/contract.html', context)


def load_termsfinal(request, bidid):
    a = Contract.objects.all()
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('termsfinal_id').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/terms_final.html', context)


def depositperc(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['depositperc']
    e = Contract.objects.filter(bidid=bidid).update(depositperc_id=d)
    context = {
        "instance": instance,
        "form": form,
        "e": e,

    }
    return render(request, 'abs/contract.html', context)


def load_depositperc(request, bidid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    c = a.values('depositperc_id').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/deposit_perc.html', context)


def load_depositamount(request, bidid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    deposita = a.values('deposit').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "deposita": deposita,
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/deposit_amount.html', context)


def customdeposit(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_customdeposit']
    f = Contract.objects.filter(bidid=bidid).update(deposit=d)
    a = JobCost.objects.values_list('grandtotalcost', flat=True).get(bidid=bidid)
    b = Contract.objects.values_list('deposit', flat=True).get(bidid=bidid)
    c = a-b
    g = Contract.objects.filter(bidid=bidid).update(finalpayment=c)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "g": g,

    }
    return render(request, 'abs/contract.html', context)


def cdp(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_depositperc']
    f = Contract.objects.filter(bidid=bidid).update(depositperc_id=d)
    g = JobCost.objects.values_list('grandtotalcost', flat=True).get(bidid=bidid)
    h = Contract.objects.values_list('depositperc_id', flat=True).get(bidid=bidid)
    i = g * h
    j = Contract.objects.filter(bidid=bidid).update(deposit=i)
    k = Contract.objects.values_list('deposit', flat=True).get(bidid=bidid)
    l = g-k
    m = Contract.objects.filter(bidid=bidid).update(finalpayment=l)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "m": m,
        "j": j,
    }
    return render(request, 'abs/contract.html', context)


def seconddeposit(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_seconddeposit']
    f = Contract.objects.filter(bidid=bidid).update(payment2=d)
    a = JobCost.objects.values_list('grandtotalcost', flat=True).get(bidid=bidid)
    b = Contract.objects.values_list('deposit', flat=True).get(bidid=bidid)
    b2 = Contract.objects.values_list('payment2', flat=True).get(bidid=bidid)
    c = a-b-b2
    g = Contract.objects.filter(bidid=bidid).update(finalpayment=c)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "g": g,

    }
    return render(request, 'abs/contract.html', context)


def load_secondamount(request, bidid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    payment2a = a.values('payment2').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "payment2a": payment2a,
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/second_payment.html', context)


def secdp(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_pay2perc']
    f = Contract.objects.filter(bidid=bidid).update(pay2perc_id=d)
    g = JobCost.objects.values_list('grandtotalcost', flat=True).get(bidid=bidid)
    h = Contract.objects.values_list('pay2perc_id', flat=True).get(bidid=bidid)
    i = g * h
    j = Contract.objects.filter(bidid=bidid).update(payment2=i)
    k = Contract.objects.values_list('deposit', flat=True).get(bidid=bidid)
    k2 = Contract.objects.values_list('payment2', flat=True).get(bidid=bidid)
    l = g-k-k2
    m = Contract.objects.filter(bidid=bidid).update(finalpayment=l)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "m": m,
        "j": j,
    }
    return render(request, 'abs/contract.html', context)


def thirddeposit(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_thirddeposit']
    f = Contract.objects.filter(bidid=bidid).update(payment3=d)
    a = JobCost.objects.values_list('grandtotalcost', flat=True).get(bidid=bidid)
    b = Contract.objects.values_list('deposit', flat=True).get(bidid=bidid)
    b2 = Contract.objects.values_list('payment2', flat=True).get(bidid=bidid)
    b3 = Contract.objects.values_list('payment3', flat=True).get(bidid=bidid)
    c = a-b-b2-b3
    g = Contract.objects.filter(bidid=bidid).update(finalpayment=c)

    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "g": g,

    }
    return render(request, 'abs/contract.html', context)


def load_thirdamount(request, bidid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    payment3a = a.values('payment3').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "payment3a": payment3a,
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/third_payment.html', context)


def thirddp(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    d = request.POST['id_pay3perc']
    f = Contract.objects.filter(bidid=bidid).update(pay3perc_id=d)
    g = JobCost.objects.values_list('grandtotalcost', flat=True).get(bidid=bidid)
    h = Contract.objects.values_list('pay3perc_id', flat=True).get(bidid=bidid)
    i = g * h
    j = Contract.objects.filter(bidid=bidid).update(payment3=i)
    k = Contract.objects.values_list('deposit', flat=True).get(bidid=bidid)
    k2 = Contract.objects.values_list('payment2', flat=True).get(bidid=bidid)
    k3 = Contract.objects.values_list('payment3', flat=True).get(bidid=bidid)
    l = g-k-k2-k3
    m = Contract.objects.filter(bidid=bidid).update(finalpayment=l)
    context = {
        "instance": instance,
        "form": form,
        "f": f,
        "m": m,
        "j": j,
    }
    return render(request, 'abs/contract.html', context)


def load_finalpayment(request, bidid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    finalpayment = a.values('finalpayment').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "finalpayment": finalpayment,
        "instance": instance,
        "form": form,
    }
    return render(request, 'abs/final_payment.html', context)


def finalinvoice(request, bidid):
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    a = Contract.objects.filter(bidid=bidid).values()
    b = Contract.objects.values_list('custid', flat=True).get(bidid=bidid)
    c = JobCost.objects.values_list('grandtotalcost', flat=True).get(bidid=bidid)
    d = Contract.objects.filter(bidid=bidid).update(grandtotalcost=c)
    queryset = CustomerInfo.objects.filter(custid=b)
    queryset2 = Contract.objects.filter(custid=b)
    instance2 = CustomerInfo.objects.order_by('id').get(custid=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "a": a,
        "object_list": queryset,
        "object_list2": queryset2,
        "d": d,
        "instance2": instance2,
    }
    return render(request, 'abs/finalinvoice.html', context)

def proposal(request, bidid):
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ConTract(request.POST or None, instance=instance)
    a = Contract.objects.filter(bidid=bidid).values()
    b = Contract.objects.values_list('custid', flat=True).get(bidid=bidid)
    c = JobCost.objects.values_list('grandtotalcost', flat=True).get(bidid=bidid)
    d = Contract.objects.filter(bidid=bidid).update(grandtotalcost=c)
    queryset = CustomerInfo.objects.filter(custid=b)
    queryset2 = Contract.objects.filter(custid=b)
    instance2 = CustomerInfo.objects.order_by('id').get(custid=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "a": a,
        "object_list": queryset,
        "object_list2": queryset2,
        "d": d,
        "instance2": instance2,
    }
    return render(request, 'abs/proposal.html', context)


def photo(request, custid=None):
    if request.method == 'POST':
        instance = get_object_or_404(CustomerInfo, custid=custid)
        jobphotos = JobImages(request.POST, request.FILES)
        if jobphotos.is_valid():
            a = CustomerInfo.objects.values_list('custid', flat=True).get(custid=custid)
            handle_uploaded_file(request.FILES['photos'])
            model_instance = jobphotos.save(commit=False)
            model_instance.save()
            b = Photo.objects.values_list('id', flat=True).last()
            c = Photo.objects.filter(id=b).update(custid=a)
            return HttpResponseRedirect(instance.get_absolute5_url(), {"c": c})

    else:
        jobphotos = JobImages
        return render(request, 'abs/uploadphoto.html', {'form': jobphotos})


def PDF1(request, custid=None):
    if request.method == 'POST':
        instance = get_object_or_404(CustomerInfo, custid=custid)
        jobpdf = JobPdf(request.POST, request.FILES)
        if jobpdf.is_valid():
            a = CustomerInfo.objects.values_list('custid', flat=True).get(custid=custid)
            handle_uploaded_PDF_file(request.FILES['pdfs'])
            model_instance = jobpdf.save(commit=False)
            model_instance.save()
            b = PDF.objects.values_list('id', flat=True).last()
            c = PDF.objects.filter(id=b).update(custid=a)
            return HttpResponseRedirect(instance.get_absolute5_url(), {"c": c})

    else:
        jobpdf = JobPdf
        return render(request, 'abs/uploadPDF.html', {'form': jobpdf})


def gallery(request, custid):
    instance = CustomerInfo.objects.get(custid=custid)
    form = Custinfo(request.POST or None, instance=instance)
    a = Photo.objects.filter(custid=custid).annotate(idA=F('id'))
    b = list(a.values_list('id', flat=True))
    try:
        img1 = Photo.objects.filter(custid=custid, id=b[0])
    except Exception:
        img1 = Photo.objects.filter(custid=custid, id=0)
    try:
        img2 = Photo.objects.filter(custid=custid, id=b[1])
    except Exception:
        img2 = Photo.objects.filter(custid=custid, id=0)
    try:
        img3 = Photo.objects.filter(custid=custid, id=b[2])
    except Exception:
        img3 = Photo.objects.filter(custid=custid, id=0)
    try:
        img4 = Photo.objects.filter(custid=custid, id=b[3])
    except Exception:
        img4 = Photo.objects.filter(custid=custid, id=0)
    try:
        img5 = Photo.objects.filter(custid=custid, id=b[4])
    except Exception:
        img5 = Photo.objects.filter(custid=custid, id=0)
    try:
        img6 = Photo.objects.filter(custid=custid, id=b[5])
    except Exception:
        img6 = Photo.objects.filter(custid=custid, id=0)
    try:
        img7 = Photo.objects.filter(custid=custid, id=b[6])
    except Exception:
        img7 = Photo.objects.filter(custid=custid, id=0)
    try:
        img8 = Photo.objects.filter(custid=custid, id=b[7])
    except Exception:
        img8 = Photo.objects.filter(custid=custid, id=0)
    try:
        img9 = Photo.objects.filter(custid=custid, id=b[8])
    except Exception:
        img9 = Photo.objects.filter(custid=custid, id=0)
    try:
        img10 = Photo.objects.filter(custid=custid, id=b[9])
    except Exception:
        img10 = Photo.objects.filter(custid=custid, id=0)
    try:
        img11 = Photo.objects.filter(custid=custid, id=b[10])
    except Exception:
        img11 = Photo.objects.filter(custid=custid, id=0)
    try:
        img12 = Photo.objects.filter(custid=custid, id=b[11])
    except Exception:
        img12 = Photo.objects.filter(custid=custid, id=0)
    try:
        img13 = Photo.objects.filter(custid=custid, id=b[12])
    except Exception:
        img13 = Photo.objects.filter(custid=custid, id=0)
    try:
        img14 = Photo.objects.filter(custid=custid, id=b[13])
    except Exception:
        img14 = Photo.objects.filter(custid=custid, id=0)
    try:
        img15 = Photo.objects.filter(custid=custid, id=b[14])
    except Exception:
        img15 = Photo.objects.filter(custid=custid, id=0)

    context = {
        "instance": instance,
        "form": form,
        "img": img1,
        "img2": img2,
        "img3": img3,
        "img4": img4,
        "img5": img5,
        "img6": img6,
        "img7": img7,
        "img8": img8,
        "img9": img9,
        "img10": img10,
        "img11": img11,
        "img12": img12,
        "img13": img13,
        "img14": img14,
        "img15": img15,
    }
    return render(request, 'abs/gallery.html', context)


def gallery2(request, custid):
    instance = CustomerInfo.objects.get(custid=custid)
    form = Custinfo(request.POST or None, instance=instance)
    a = Photo.objects.filter(custid=custid).annotate(idA=F('id'))
    b = list(a.values_list('id', flat=True))
    try:
        img1 = Photo.objects.filter(custid=custid, id=b[0])
    except Exception:
        img1 = Photo.objects.filter(custid=custid, id=0)
    try:
        img2 = Photo.objects.filter(custid=custid, id=b[1])
    except Exception:
        img2 = Photo.objects.filter(custid=custid, id=0)
    try:
        img3 = Photo.objects.filter(custid=custid, id=b[2])
    except Exception:
        img3 = Photo.objects.filter(custid=custid, id=0)
    try:
        img4 = Photo.objects.filter(custid=custid, id=b[3])
    except Exception:
        img4 = Photo.objects.filter(custid=custid, id=0)
    try:
        img5 = Photo.objects.filter(custid=custid, id=b[4])
    except Exception:
        img5 = Photo.objects.filter(custid=custid, id=0)
    try:
        img6 = Photo.objects.filter(custid=custid, id=b[5])
    except Exception:
        img6 = Photo.objects.filter(custid=custid, id=0)
    try:
        img7 = Photo.objects.filter(custid=custid, id=b[6])
    except Exception:
        img7 = Photo.objects.filter(custid=custid, id=0)
    try:
        img8 = Photo.objects.filter(custid=custid, id=b[7])
    except Exception:
        img8 = Photo.objects.filter(custid=custid, id=0)
    try:
        img9 = Photo.objects.filter(custid=custid, id=b[8])
    except Exception:
        img9 = Photo.objects.filter(custid=custid, id=0)
    try:
        img10 = Photo.objects.filter(custid=custid, id=b[9])
    except Exception:
        img10 = Photo.objects.filter(custid=custid, id=0)
    try:
        img11 = Photo.objects.filter(custid=custid, id=b[10])
    except Exception:
        img11 = Photo.objects.filter(custid=custid, id=0)
    try:
        img12 = Photo.objects.filter(custid=custid, id=b[11])
    except Exception:
        img12 = Photo.objects.filter(custid=custid, id=0)
    try:
        img13 = Photo.objects.filter(custid=custid, id=b[12])
    except Exception:
        img13 = Photo.objects.filter(custid=custid, id=0)
    try:
        img14 = Photo.objects.filter(custid=custid, id=b[13])
    except Exception:
        img14 = Photo.objects.filter(custid=custid, id=0)
    try:
        img15 = Photo.objects.filter(custid=custid, id=b[14])
    except Exception:
        img15 = Photo.objects.filter(custid=custid, id=0)

    context = {
        "instance": instance,
        "form": form,
        "img": img1,
        "img2": img2,
        "img3": img3,
        "img4": img4,
        "img5": img5,
        "img6": img6,
        "img7": img7,
        "img8": img8,
        "img9": img9,
        "img10": img10,
        "img11": img11,
        "img12": img12,
        "img13": img13,
        "img14": img14,
        "img15": img15,
    }
    return render(request, 'abs/gallery2.html', context)


def PDFgallery(request, custid):
    instance = CustomerInfo.objects.get(custid=custid)
    form = Custinfo(request.POST or None, instance=instance)
    a = PDF.objects.filter(custid=custid).annotate(idA=F('id'))
    b = list(a.values_list('id', flat=True))
    try:
        pdf1 = PDF.objects.filter(custid=custid, id=b[0])
    except Exception:
        pdf1 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf2 = PDF.objects.filter(custid=custid, id=b[1])
    except Exception:
        pdf2 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf3 = PDF.objects.filter(custid=custid, id=b[2])
    except Exception:
        pdf3 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf4 = PDF.objects.filter(custid=custid, id=b[3])
    except Exception:
        pdf4 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf5 = PDF.objects.filter(custid=custid, id=b[4])
    except Exception:
        pdf5 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf6 = PDF.objects.filter(custid=custid, id=b[5])
    except Exception:
        pdf6 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf7 = PDF.objects.filter(custid=custid, id=b[6])
    except Exception:
        pdf7 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf8 = PDF.objects.filter(custid=custid, id=b[7])
    except Exception:
        pdf8 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf9 = PDF.objects.filter(custid=custid, id=b[8])
    except Exception:
        pdf9 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf10 = PDF.objects.filter(custid=custid, id=b[9])
    except Exception:
        pdf10 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf11 = PDF.objects.filter(custid=custid, id=b[10])
    except Exception:
        pdf11 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf12 = PDF.objects.filter(custid=custid, id=b[11])
    except Exception:
        pdf12 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf13 = PDF.objects.filter(custid=custid, id=b[12])
    except Exception:
        pdf13 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf14 = PDF.objects.filter(custid=custid, id=b[13])
    except Exception:
        pdf14 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf15 = PDF.objects.filter(custid=custid, id=b[14])
    except Exception:
        pdf15 = PDF.objects.filter(custid=custid, id=0)

    context = {
        "instance": instance,
        "form": form,
        "pdf1": pdf1,
        "pdf2": pdf2,
        "pdf3": pdf3,
        "pdf4": pdf4,
        "pdf5": pdf5,
        "pdf6": pdf6,
        "pdf7": pdf7,
        "pdf8": pdf8,
        "pdf9": pdf9,
        "pdf10": pdf10,
        "pdf11": pdf11,
        "pdf12": pdf12,
        "pdf13": pdf13,
        "pdf14": pdf14,
        "pdf15": pdf15,
    }
    return render(request, 'abs/PDFgallery.html', context)


def PDFgallery2(request, custid):
    instance = CustomerInfo.objects.get(custid=custid)
    form = Custinfo(request.POST or None, instance=instance)
    a = PDF.objects.filter(custid=custid).annotate(idA=F('id'))
    b = list(a.values_list('id', flat=True))
    try:
        pdf1 = PDF.objects.filter(custid=custid, id=b[0])
    except Exception:
        pdf1 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf2 = PDF.objects.filter(custid=custid, id=b[1])
    except Exception:
        pdf2 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf3 = PDF.objects.filter(custid=custid, id=b[2])
    except Exception:
        pdf3 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf4 = PDF.objects.filter(custid=custid, id=b[3])
    except Exception:
        pdf4 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf5 = PDF.objects.filter(custid=custid, id=b[4])
    except Exception:
        pdf5 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf6 = PDF.objects.filter(custid=custid, id=b[5])
    except Exception:
        pdf6 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf7 = PDF.objects.filter(custid=custid, id=b[6])
    except Exception:
        pdf7 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf8 = PDF.objects.filter(custid=custid, id=b[7])
    except Exception:
        pdf8 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf9 = PDF.objects.filter(custid=custid, id=b[8])
    except Exception:
        pdf9 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf10 = PDF.objects.filter(custid=custid, id=b[9])
    except Exception:
        pdf10 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf11 = PDF.objects.filter(custid=custid, id=b[10])
    except Exception:
        pdf11 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf12 = PDF.objects.filter(custid=custid, id=b[11])
    except Exception:
        pdf12 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf13 = PDF.objects.filter(custid=custid, id=b[12])
    except Exception:
        pdf13 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf14 = PDF.objects.filter(custid=custid, id=b[13])
    except Exception:
        pdf14 = PDF.objects.filter(custid=custid, id=0)
    try:
        pdf15 = PDF.objects.filter(custid=custid, id=b[14])
    except Exception:
        pdf15 = PDF.objects.filter(custid=custid, id=0)

    context = {
        "instance": instance,
        "form": form,
        "pdf1": pdf1,
        "pdf2": pdf2,
        "pdf3": pdf3,
        "pdf4": pdf4,
        "pdf5": pdf5,
        "pdf6": pdf6,
        "pdf7": pdf7,
        "pdf8": pdf8,
        "pdf9": pdf9,
        "pdf10": pdf10,
        "pdf11": pdf11,
        "pdf12": pdf12,
        "pdf13": pdf13,
        "pdf14": pdf14,
        "pdf15": pdf15,
    }
    return render(request, 'abs/PDFgallery2.html', context)