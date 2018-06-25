from django.db import models
from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.core.signals import post_save

class Member(models.Model):
    '''
    cash : is the cash you're having
    '''
    user_now = models.OneToOneField(User, on_delete=models.CASCADE)
    cash = models.FloatField(verbose_name='Tiền mặt')
    def __str__(self):
        return '{} - {} '.format(self.user_now,self.cash)

    class Meta:
        verbose_name        = 'Người dùng'
        verbose_name_plural = 'Người dùng'


'''
INCOME and EXPENSE is to compute monthly finance only
borrow,lend,invest... is another model that take to compute asset
'''


class Income(models.Model):
    '''
    type : the type of a Income
    - fixed income : is your certain mone receive monthly
    - interests    : like interest from investment - each time receive need to add or setup auto adding for this
    - others       : like the money u receive from side project
    amount : the amount of a income
    '''
    INCOMETYPES = (
    ('f', 'Thu nhập cố định'),
    ('i','Tiền lãi'),
    ('b','Vay'),
    ('o', 'Khác'),

    )
    user_now   = models.ForeignKey(Member,on_delete = models.CASCADE,verbose_name = 'Id người dùng')
    type   = models.CharField(verbose_name      = 'Loại thu nhập',max_length  = 1,choices = INCOMETYPES,blank=False)
    amount = models.FloatField(verbose_name     = 'Số tiền',blank             = False)
    notes  = models.CharField(verbose_name      = 'Ghi chú',max_length        = 255,blank=True)
    time   = models.DateField(verbose_name      = 'Thời gian nhận',auto_now   = True)
    def __str__(self):
        return '{} - {}'.format(self.type,self.amount)
    # def save(self, *args, **kwargs):
    #     super(Member, self).save(*args, **kwargs)
    #     print('this is user_now',self.user_now.cash)
    #     self.user_now.cash=10000
    #     self.user_now.save()

    class Meta:
        verbose_name_plural= 'Thu nhập'

class Expense(models.Model):
    '''
    type :
    Ăn : Ăn uống hàng thực phẩm hàng ngày
    Dịch vụ : Tiền điện nước, tiền nhà, điện thoại ...
    Mua sắm : quần áo , thiết bị ...
    Giải trí : cafe , du lịch...
    Học tập : mua sách , học phí...
    Gia đình : Con cái , sửa chữa nhà cửa ...
    '''
    EXPENSEETYPES = (
    ('f','Ăn'),
    ('u','Dịch vụ'),
    ('b','Mua sắm'),
    ('e','Giải trí'),
    ('s','Học tập'),
    ('f','Gia đình')
    )
    user_now = models.ForeignKey(Member,on_delete = models.CASCADE,verbose_name = 'Id người dùng')
    type    = models.CharField(verbose_name    = 'Loại chi tiêu',max_length  = 1,choices = EXPENSEETYPES,blank=False)
    amount  = models.FloatField(verbose_name   = 'Số tiền',blank=False)
    notes   = models.CharField(verbose_name    = 'Ghi chú',max_length        = 255)
    time    = models.DateField(verbose_name    = 'Thời gian tiêu',auto_now   = True)
    def __str__(self):
        return '{} - {}'.format([type for type in self.EXPENSEETYPES if type[0]==self.type ][0][1],self.amount)
    class Meta:
        verbose_name_plural = 'Chi tiêu'
