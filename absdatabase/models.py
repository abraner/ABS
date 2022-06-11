from django.db import models
from phone_field import PhoneField


class CustomerInfo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    custcompanytname = models.CharField(max_length=50, blank=True, null=True, verbose_name="Company Name:")
    custfirstname = models.CharField(max_length=45, verbose_name="First Name:")
    custlastname = models.CharField(max_length=45, verbose_name="Last Name:")
    custadd1 = models.CharField(max_length=45, verbose_name="Address #1:")
    custadd2 = models.CharField(max_length=45, blank=True, null=True, verbose_name="Address #2:")
    custcity = models.CharField(max_length=45, verbose_name="City:")
    custst = models.CharField(max_length=2, verbose_name="St:")
    custzipcode = models.CharField(max_length=15, verbose_name="Zip Code:")
    custwork1 = PhoneField(blank=True, null=True, verbose_name="Work Phone #1:")
    custwork2 = PhoneField(blank=True, null=True, verbose_name="Work Phone #2:")
    custcell1 = PhoneField(blank=True, null=True, verbose_name="Cell Phone #1:")
    custcell2 = PhoneField(blank=True, null=True, verbose_name="Cell Phone #2:")
    custhome = PhoneField(blank=True, null=True, verbose_name="Home Phone:")
    custemail1 = models.EmailField(max_length=254, blank=True, null=True, verbose_name="Email #1:")
    custemail2 = models.EmailField(max_length=254, blank=True, null=True, verbose_name="Email #2:")
    date = models.DateField(auto_now_add=False, auto_now=True, null=True, blank=True, verbose_name="")
    photos = models.ImageField(null=True, blank=True, upload_to="jobimg/")

    class Meta:
        unique_together = ["custfirstname", "custlastname", "custadd1", "custcity", "custst"]

    def get_absolute2_url(self):
        return f"/absdatabase/{self.id}/newcust/"

    def get_absolute4_url(self):
        return f"/absdatabase/{self.custid}/scheduledappt"

    def get_absolute6_url(self):
        return f"/absdatabase/{self.id}/appointment/"

    def get_absolute45_url(self):
        return f"/absdatabase/{self.id}/deletecust2/"

    def get_absolute5_url(self):
        return f"/absdatabase/{self.id}/custinfo/"

    def get_absolute7_url(self):
        return f"/absdatabase/{self.custid}/deletecust/"

    def get_absolute8_url(self):
        return f"/absdatabase/{self.id}/photo/"

    def get_absolute9_url(self):
        return f"/absdatabase/{self.id}/PDF1/"

    def get_absolute10_url(self):
        return f"/absdatabase/cust_info_existing"



class DeleteCust(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    deletecust = models.IntegerField(null=True, default=None, verbose_name="")
    deletecon = models.IntegerField(null=True, default=None, verbose_name="")

    def get_absolute_url(self):
        return f"/absdatabase/{self.deletecust}/coninfo"


class Photo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    photos = models.ImageField(null=True, blank=True, upload_to="img/")



class PDF(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    pdfs = models.ImageField(null=True, blank=True, upload_to="pdf/")



class Time(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    appointmenttime = models.CharField(max_length=10, blank=True, unique=True, verbose_name="")

    def __str__(self):
        return str(self.appointmenttime)


class Appointment(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    appdate = models.DateField(blank=True, null=True)
    apptime = models.ForeignKey(Time, to_field="appointmenttime", related_name='apptime', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    appdescrip = models.CharField(max_length=1000, blank=True, verbose_name="")
    callindate = models.DateField(blank=True, null=True)
    date = models.DateField(auto_now_add=False, auto_now=True, null=True, blank=True, verbose_name="")
    mainid = models.IntegerField(null=True, default=None, verbose_name="")

    def get_absolute6_url(self):
        return f"/absdatabase/{self.custid}/appointment"

    def get_absolute3_url(self):
        return f"/absdatabase/{self.mainid}/main"

    def get_absolute4_url(self):
        return f"/absdatabase/{self.custid}/scheduledappt"

    def get_absolute7_url(self):
        return f"/absdatabase/{self.custid}/bidpage"




class AppQueue(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    appdate = models.DateField(blank=True, null=True)
    apptime = models.CharField(max_length=10, blank=True, null=True, verbose_name="")
    appdescrip = models.CharField(max_length=1000, blank=True, verbose_name="")
    callindate = models.DateField(blank=True, null=True)
    date = models.DateField(auto_now_add=False, auto_now=True, null=True, blank=True, verbose_name="")

    class Meta:
        ordering = ["appdate",
                    "apptime"]


class AppQueueCount(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    count = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")

    def get_absolute3_url(self):
        return f"/absdatabase/{self.id}/main"


class WorkType(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    type = models.CharField(max_length=60, unique=True, blank=True, verbose_name="")

    def __str__(self):
        return str(self.type)


class HeightFt(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    feet = models.IntegerField(null=True, unique=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.feet)


class HeightIn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    inches = models.DecimalField(decimal_places=2, unique=True, max_digits=7, default='0.00', verbose_name="")

    def __str__(self):
        return str(self.inches)


class Qty(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    quantity = models.IntegerField(null=True, unique=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.quantity)


class BeamFt(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    feet = models.IntegerField(null=True, unique=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.feet)


class BeamIn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    inches = models.DecimalField(decimal_places=2, unique=True, max_digits=7, default='0.00', verbose_name="")

    def __str__(self):
        return str(self.inches)


class BeamType(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    beam_type = models.CharField(max_length=20, unique=True, blank=True, verbose_name="")

    def __str__(self):
        return str(self.beam_type)


class LallyColumn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    lally_size = models.CharField(max_length=20, unique=False, blank=True, verbose_name="")
    lally_return = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    lally_cost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")

    def __str__(self):
        return str(self.lally_size)


class LallyColumnReturn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    lally_return = models.CharField(max_length=20, unique=True, blank=True, verbose_name="")

    def __str__(self):
        return str(self.lally_return)


class FootingSize(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    footingdim = models.CharField(max_length=20, blank=True, verbose_name="")
    footing_cost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    footing_labor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")

    def __str__(self):
        return str(self.footingdim)


class ProdQueue(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    production = models.CharField(max_length=50, blank=True, unique=True, verbose_name="Production")
    increase = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=True, verbose_name="Increase / Decrease")

    def __str__(self):
        return str(self.increase)


class Bidpage(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    bidid = models.IntegerField(null=True, default=None, verbose_name="Bid ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    chfeet1 = models.ForeignKey(HeightFt, to_field="id", related_name='chfeet1', null=True, blank=True, default=None,
                                on_delete=models.CASCADE, verbose_name="")
    chinches1 = models.ForeignKey(HeightIn, to_field="id", related_name='chinches1', null=True, blank=True,
                                  default=None, on_delete=models.CASCADE, verbose_name="")
    beamtype1 = models.CharField(max_length=10, blank=True, null=True, verbose_name="")
    beamsize1 = models.CharField(max_length=50, blank=True, null=True, verbose_name="")
    worktype = models.ForeignKey(WorkType, to_field="id", related_name='worktype1', null=True, blank=True, default=None,
                                on_delete=models.CASCADE, verbose_name="")
    qty1 = models.ForeignKey(Qty, to_field="quantity", related_name='row1qty', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    beamlength1ft = models.ForeignKey(BeamFt, to_field="feet", related_name='beamlength1ft', null=True, blank=True, default=0,
                                on_delete=models.CASCADE, verbose_name="")
    beamlength1in = models.ForeignKey(HeightIn, to_field="inches", related_name='beamlength1in', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    lcqty1 = models.ForeignKey(Qty, to_field="quantity", related_name='lcqty1', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    lclength1 = models.ForeignKey(Qty, to_field="quantity", related_name='lclength1', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    lctransition1 = models.ForeignKey(LallyColumnReturn, to_field="id", related_name='lctransition1', null=True, blank=True,
                                  default=1, on_delete=models.CASCADE, verbose_name="")
    beamcost1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True, verbose_name="")
    lcost1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True, verbose_name="")
    lallycost1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True, verbose_name="")
    qty2 = models.ForeignKey(Qty, to_field="quantity", related_name='row2qty', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    beamlength2ft = models.ForeignKey(BeamFt, to_field="feet", related_name='beamlength2ft', null=True, blank=True,
                                      default=0,
                                      on_delete=models.CASCADE, verbose_name="")
    beamlength2in = models.ForeignKey(HeightIn, to_field="inches", related_name='beamlength2in', null=True, blank=True,
                                      default=0, on_delete=models.CASCADE, verbose_name="")
    lcqty2 = models.ForeignKey(Qty, to_field="quantity", related_name='lcqty2', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    lclength2 = models.ForeignKey(Qty, to_field="quantity", related_name='lclength2', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    lctransition2 = models.ForeignKey(LallyColumnReturn, to_field="id", related_name='lctransition2', null=True, blank=True,
                                  default=1, on_delete=models.CASCADE, verbose_name="")
    beamcost2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                    verbose_name="")
    lcost2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True, verbose_name="")
    lallycost2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    qty3 = models.ForeignKey(Qty, to_field="quantity", related_name='row3qty', null=True, blank=True,
                             default=0, on_delete=models.CASCADE, verbose_name="")
    beamlength3ft = models.ForeignKey(BeamFt, to_field="feet", related_name='beamlength3ft', null=True, blank=True,
                                      default=0,
                                      on_delete=models.CASCADE, verbose_name="")
    beamlength3in = models.ForeignKey(HeightIn, to_field="inches", related_name='beamlength3in', null=True, blank=True,
                                      default=0, on_delete=models.CASCADE, verbose_name="")
    lcqty3 = models.ForeignKey(Qty, to_field="quantity", related_name='lcqty3', null=True, blank=True,
                               default=0, on_delete=models.CASCADE, verbose_name="")
    lclength3 = models.ForeignKey(Qty, to_field="quantity", related_name='lclength3', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    lctransition3 = models.ForeignKey(LallyColumnReturn, to_field="id", related_name='lctransition3', null=True,
                                      blank=True,
                                      default=1, on_delete=models.CASCADE, verbose_name="")
    beamcost3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                    verbose_name="")
    lcost3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True, verbose_name="")
    lallycost3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    qty4 = models.ForeignKey(Qty, to_field="quantity", related_name='row4qty', null=True, blank=True,
                             default=0, on_delete=models.CASCADE, verbose_name="")
    beamlength4ft = models.ForeignKey(BeamFt, to_field="feet", related_name='beamlength4ft', null=True, blank=True,
                                      default=0,
                                      on_delete=models.CASCADE, verbose_name="")
    beamlength4in = models.ForeignKey(HeightIn, to_field="inches", related_name='beamlength4in', null=True, blank=True,
                                      default=0, on_delete=models.CASCADE, verbose_name="")
    lcqty4 = models.ForeignKey(Qty, to_field="quantity", related_name='lcqty4', null=True, blank=True,
                               default=0, on_delete=models.CASCADE, verbose_name="")
    lclength4 = models.ForeignKey(Qty, to_field="quantity", related_name='lclength4', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    lctransition4 = models.ForeignKey(LallyColumnReturn, to_field="id", related_name='lctransition4', null=True,
                                      blank=True,
                                      default=1, on_delete=models.CASCADE, verbose_name="")
    beamcost4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                    verbose_name="")
    lcost4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True, verbose_name="")
    lallycost4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    qty5 = models.ForeignKey(Qty, to_field="quantity", related_name='row5qty', null=True, blank=True,
                             default=0, on_delete=models.CASCADE, verbose_name="")
    beamlength5ft = models.ForeignKey(BeamFt, to_field="feet", related_name='beamlength5ft', null=True, blank=True,
                                      default=0,
                                      on_delete=models.CASCADE, verbose_name="")
    beamlength5in = models.ForeignKey(HeightIn, to_field="inches", related_name='beamlength5in', null=True, blank=True,
                                      default=0, on_delete=models.CASCADE, verbose_name="")
    lcqty5 = models.ForeignKey(Qty, to_field="quantity", related_name='lcqty5', null=True, blank=True,
                               default=0, on_delete=models.CASCADE, verbose_name="")
    lclength5 = models.ForeignKey(Qty, to_field="quantity", related_name='lclength5', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    lctransition5 = models.ForeignKey(LallyColumnReturn, to_field="id", related_name='lctransition5', null=True,
                                      blank=True,
                                      default=1, on_delete=models.CASCADE, verbose_name="")
    beamcost5 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                    verbose_name="")
    lcost5 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True, verbose_name="")
    lallycost5 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    qty6 = models.ForeignKey(Qty, to_field="quantity", related_name='row6qty', null=True, blank=True,
                             default=0, on_delete=models.CASCADE, verbose_name="")
    beamlength6ft = models.ForeignKey(BeamFt, to_field="feet", related_name='beamlength6ft', null=True, blank=True,
                                      default=0,
                                      on_delete=models.CASCADE, verbose_name="")
    beamlength6in = models.ForeignKey(HeightIn, to_field="inches", related_name='beamlength6in', null=True, blank=True,
                                      default=0, on_delete=models.CASCADE, verbose_name="")
    lcqty6 = models.ForeignKey(Qty, to_field="quantity", related_name='lcqty6', null=True, blank=True,
                               default=0, on_delete=models.CASCADE, verbose_name="")
    lclength6 = models.ForeignKey(Qty, to_field="quantity", related_name='lclength6', null=True, blank=True,
                                  default=0, on_delete=models.CASCADE, verbose_name="")
    lctransition6 = models.ForeignKey(LallyColumnReturn, to_field="id", related_name='lctransition6', null=True,
                                      blank=True,
                                      default=1, on_delete=models.CASCADE, verbose_name="")
    beamcost6 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                    verbose_name="")
    lcost6 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True, verbose_name="")
    lallycost6 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    footingqty = models.ForeignKey(Qty, to_field="quantity", related_name='footingqty', null=True, blank=True,
                             default=0, on_delete=models.CASCADE, verbose_name="")
    footingsize = models.ForeignKey(FootingSize, to_field="id", related_name='footingsize', null=True, blank=True,
                             default=1, on_delete=models.CASCADE, verbose_name="")
    footingmat = models.IntegerField(null=True, default=0.00, verbose_name="")
    footinglabor = models.IntegerField(null=True, default=0.00, verbose_name="")
    footinglaborcost = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True, verbose_name="")
    footingmatcost = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    miscqty1 = models.ForeignKey(Qty, to_field="quantity", related_name='miscqty1', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    miscdescription1 = models.CharField(max_length=400, blank=True, null=True, verbose_name="")
    miscmat1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    misclabor1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    miscmatcost1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    misclaborcost1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                       verbose_name="")
    miscqty2 = models.ForeignKey(Qty, to_field="quantity", related_name='miscqty2', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    miscdescription2 = models.CharField(max_length=400, blank=True, null=True, verbose_name="")
    miscmat2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    misclabor2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    miscmatcost2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                       verbose_name="")
    misclaborcost2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                         verbose_name="")
    miscqty3 = models.ForeignKey(Qty, to_field="quantity", related_name='miscqty3', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    miscdescription3 = models.CharField(max_length=400, blank=True, null=True, verbose_name="")
    misclabor3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    miscmat3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    miscmatcost3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                       verbose_name="")
    misclaborcost3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                         verbose_name="")
    miscqty4 = models.ForeignKey(Qty, to_field="quantity", related_name='miscqty4', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    miscdescription4 = models.CharField(max_length=400, blank=True, null=True, verbose_name="")
    misclabor4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    miscmat4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                     verbose_name="")
    miscmatcost4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                       verbose_name="")
    misclaborcost4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.00, blank=True,
                                         verbose_name="")
    prodqueue = models.ForeignKey(ProdQueue, to_field="increase", related_name='prodqueue', null=True, blank=True,
                                  default=0.00, on_delete=models.CASCADE, verbose_name="")
    beamselect = models.IntegerField(null=True, default=0.00, verbose_name="")
    disabled = models.IntegerField(null=True, default=0.00, verbose_name="")

    def get_absolute5_url(self):
        return f"/absdatabase/{self.id}/bidpage"

    def get_absolute6_url(self):
        return f"/absdatabase/{self.custid}/custinfo"


class BeamInfo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    beam_type = models.CharField(max_length=20, blank=True, verbose_name="")
    beam_size = models.CharField(max_length=20, blank=True, verbose_name="", unique=True)
    beam_cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    beam_labor = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class TaxRate(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    tax = models.DecimalField(decimal_places=4, max_digits=7, unique=True, default=0.0000, verbose_name="")
    taxperc = models.CharField(max_length=50, blank=True, verbose_name="")

    def __str__(self):
        return self.taxperc


class JobCost(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    materialcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    laborcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    totalcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    increase = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    grandtotalcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


    def get_absolute5_url(self):
        return f"/absdatabase/{self.bidid}/bidpage"


class DownPayTerms(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    terms = models.CharField(max_length=150, blank=True, verbose_name="")

    def __str__(self):
        return str(self.terms)


class FinalPayTerms(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    terms = models.CharField(max_length=150, blank=True, verbose_name="")

    def __str__(self):
        return str(self.terms)


class Percentage(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    percent = models.CharField(max_length=50, blank=True, verbose_name="")
    multiplier = models.DecimalField(decimal_places=2, unique=True, max_digits=7, default='0.00', verbose_name="")

    def __str__(self):
        return str(self.percent)


class Contract(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    workorderdate = models.DateField(blank=True, null=True)
    date = models.DateField(auto_now_add=False, auto_now=True, blank=True)
    grandtotalcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    depositperc = models.ForeignKey(Percentage, to_field="multiplier", related_name='depositperc', null=True,
                                    blank=True, default=None, on_delete=models.CASCADE, verbose_name="")
    depositterms = models.ForeignKey(DownPayTerms, to_field="id", related_name='term1', null=True, blank=True,
                               default=None, on_delete=models.CASCADE, verbose_name="")
    deposit = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    depositdate = models.DateField(blank=True, null=True)
    term2 = models.ForeignKey(DownPayTerms, to_field="id", related_name='term2', null=True, blank=True,
                              default=None, on_delete=models.CASCADE, verbose_name="")
    pay2perc = models.ForeignKey(Percentage, to_field="multiplier", related_name='pay2perc', null=True, blank=True,
                                 default=None, on_delete=models.CASCADE, verbose_name="")
    payment2 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    payment2date = models.DateField(blank=True, null=True)
    term3 = models.ForeignKey(DownPayTerms, to_field="id", related_name='term3', null=True, blank=True,
                              default=None, on_delete=models.CASCADE, verbose_name="")
    pay3perc = models.ForeignKey(Percentage, to_field="multiplier", related_name='pay3perc', null=True, blank=True,
                                 default=None, on_delete=models.CASCADE, verbose_name="")
    payment3 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    payment3date = models.DateField(blank=True, null=True)
    finalpayment = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    finalpaymentdate = models.DateField(blank=True, null=True)
    termsfinal = models.ForeignKey(DownPayTerms, to_field="id", related_name='termfinal', null=True, blank=True,
                              default=None, on_delete=models.CASCADE, verbose_name="")
    customdeposit = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    seconddeposit = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")
    thirddeposit = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="")



    def get_absolute4_url(self):
        return f"/absdatabase/{self.custid}/custinfo"


    def get_absolute5_url(self):
        return f"/absdatabase/{self.bidid}/contract"


    def get_absolute6_url(self):
        return f"/absdatabase/{self.bidid}/finalinvoice"

