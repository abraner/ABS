from django import forms
from .models import CustomerInfo, Appointment, AppQueueCount, AppQueue, Bidpage, BeamInfo, JobCost, Contract, Photo, PDF

class DateInput2(forms.DateInput):
    input_type = 'date'


class JobImages(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
                  'photos',
                  ]


class JobPdf(forms.ModelForm):
    class Meta:
        model = PDF
        fields = [
                  'pdfs',
                  ]


class Custinfo(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = [
            'id',
            'custid',
            'custcompanytname',
            'custfirstname',
            'custlastname',
            'custadd1',
            'custadd2',
            'custcity',
            'custst',
            'custzipcode',
            'custwork1',
            'custwork2',
            'custcell1',
            'custcell2',
            'custhome',
            'custemail1',
            'custemail2',
            'photos',

        ]

        widgets = {'custwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }


class CustinfoC(forms.ModelForm):

    class Meta:
        model = CustomerInfo
        fields = [
            'custcompanytname',
            'custfirstname',
            'custlastname',
            'custadd1',
            'custadd2',
            'custcity',
            'custst',
            'custzipcode',
            'custwork1',
            'custwork2',
            'custcell1',
            'custcell2',
            'custhome',
            'custemail1',
            'custemail2',

        ]

        widgets = {'custwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }


class AppointMent(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'custid',
            'appdate',
            'apptime',
            'appdescrip',
        ]

    appointmentdate = forms.DateField(
        widget=DateInput2(format='%Y-%m-%d', attrs={'onblur': 'AppointmentDateFunction()'}),
        required=False,
    )

    appdescrip = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, 'onblur': 'NotesFunction()'}),
        required=False,
    )


class AppointMent1(forms.ModelForm):
    class Meta:
        model = AppQueue
        fields = [
            'custid',
            'appdate',
            'apptime',
            'appdescrip',
        ]

    appdate = forms.DateField(
        widget=DateInput2(format='%Y-%m-%d'),
        required=False,
    )

    appdescrip = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5}),
        required=False
    )


class QueueCount(forms.ModelForm):
    class Meta:
        model = AppQueueCount
        fields = ['count']


class BidPage(forms.ModelForm):
    class Meta:
        model = Bidpage
        fields = [
            'custid',
            'bidid',
            'worktype',
            'chfeet1',
            'chinches1',
            'beamtype1',
            'qty1',
            'beamlength1ft',
            'beamlength1in',
            'beamsize1',
            'lcqty1',
            'lclength1',
            'lctransition1',
            'beamcost1',
            'lcost1',
            'qty2',
            'beamlength2ft',
            'beamlength2in',
            'lcqty2',
            'lclength2',
            'lctransition2',
            'qty3',
            'beamlength3ft',
            'beamlength3in',
            'lcqty3',
            'lclength3',
            'lctransition3',
            'qty4',
            'beamlength4ft',
            'beamlength4in',
            'lcqty4',
            'lclength4',
            'lctransition4',
            'qty5',
            'beamlength5ft',
            'beamlength5in',
            'lcqty5',
            'lclength5',
            'lctransition5',
            'qty6',
            'beamlength6ft',
            'beamlength6in',
            'lcqty6',
            'lclength6',
            'lctransition6',
            'footingqty',
            'footingsize',
            'miscqty1',
            'miscdescription1',
            'miscmat1',
            'misclabor1',
            'miscqty2',
            'miscdescription2',
            'miscmat2',
            'misclabor2',
            'miscqty3',
            'miscdescription3',
            'miscmat3',
            'misclabor3',
            'miscqty4',
            'miscdescription4',
            'miscmat4',
            'misclabor4',
            'prodqueue',
            'beamselect',
            'disabled',

        ]


    miscdescription1 = forms.CharField(
        widget=forms.TextInput(
            attrs={'onblur': 'MiscDescrip1Function()'}),
        required=False,
    )


    miscmat1 = forms.CharField(
        widget=forms.TextInput(
            attrs={'onblur': 'MiscMat1Function()'}),
        required=False,
    )


    misclabor1 = forms.CharField(
        widget=forms.TextInput(
            attrs={'onblur': 'MiscLabor1Function1(); MiscLabor1Function2(); MiscLabor1Function3();'
                             ' MiscLabor1Function4(); MiscLabor1Function5()'}),
        required=False,
    )


class BeamTypeChoiceField(forms.Form):
    beamtype1 = forms.ModelChoiceField(
        BeamInfo.objects.values_list('beam_type', flat=True).distinct(),
        required=False,
        empty_label='Select Beam Type',
        label="")


class BeamSizeChoiceField(forms.Form):
    beamsize1 = forms.ModelChoiceField(
        BeamInfo.objects.values_list('beam_size', flat=True).distinct(),
        required=False,
        empty_label='',
        label="")


class CostJob(forms.ModelForm):
    class Meta:
        model = JobCost
        fields = [
            'bidid',
            'custid',
            'materialcost',
            'laborcost',
            'totalcost',
            'increase',
            'grandtotalcost',

        ]


class ConTract(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'bidid',
            'custid',
            'grandtotalcost',
            'workorderdate',
            'depositperc',
            'depositterms',
            'deposit',
            'depositdate',
            'term2',
            'payment2',
            'pay2perc',
            'payment2date',
            'term3',
            'payment3',
            'pay3perc',
            'payment3date',
            'termsfinal',
            'finalpayment',
            'finalpaymentdate',
            'customdeposit',
            'seconddeposit',
            'thirddeposit',

        ]

