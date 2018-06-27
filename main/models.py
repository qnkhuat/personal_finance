from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Member(models.Model):
    '''
    cash : is the cash you're having
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='member')
    cash = models.FloatField(verbose_name='Tiền mặt')
    def __str__(self):
        return '{} - {} '.format(self.user,self.cash)

    class Meta:
        verbose_name        = 'Người dùng'
        verbose_name_plural = 'Người dùng'

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            # NOTE:cash =1 is just for instance
            Member.objects.create(user=instance,cash=1)
        instance.user.save()



'''
INCOME and EXPENSE is for compute monthly finance only
borrow,lend,invest... is another model that take to compute asset
'''
class CashInAndOut(models.Model):
    user   = models.ForeignKey(Member,on_delete = models.CASCADE,verbose_name = 'Người dùng')
    amount = models.FloatField(verbose_name     = 'Số tiền',blank             = False)
    notes  = models.CharField(verbose_name      = 'Ghi chú',max_length        = 255,blank=True)
    time   = models.DateField(verbose_name      = 'Thời gian',auto_now   = True)
    def __str__(self):
        return '{} - {}'.format([type for type in self.TYPES if type[0]==self.type][0][1],self.amount)

class Income(CashInAndOut):
    '''
    type : the type of a Income
    - fixed income : is your certain mone receive monthly
    - interests    : like interest from investment - each time receive need to add or setup auto adding for this
    - others       : like the money u receive from side project
    '''
    TYPES = (
    ('f', 'Thu nhập cố định'),
    ('i','Tiền lãi'),
    ('b','Vay'),
    ('o', 'Khác'),
    )
    type = models.CharField(verbose_name = 'Loại thu nhập',max_length = 1,choices = TYPES,blank = False)
    class Meta:
        verbose_name_plural= 'Thu nhập'

class Expense(CashInAndOut):
    '''
    type :
    Ăn : Ăn uống hàng thực phẩm hàng ngày
    Dịch vụ : Tiền điện nước, tiền nhà, điện thoại ...
    Mua sắm : quần áo , thiết bị ...
    Giải trí : cafe , du lịch...
    Học tập : mua sách , học phí...
    Gia đình : Con cái , sửa chữa nhà cửa ...
    '''
    TYPES = (
    ('f','Ăn'),
    ('u','Dịch vụ'),
    ('b','Mua sắm'),
    ('e','Giải trí'),
    ('s','Học tập'),
    ('f','Gia đình')
    )
    type = models.CharField(verbose_name = 'Loại chi tiêu',max_length = 1,choices = TYPES,blank = False)
    class Meta:
        verbose_name_plural = 'Chi tiêu'
