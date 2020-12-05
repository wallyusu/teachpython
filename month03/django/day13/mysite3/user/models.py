from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField('姓名',max_length=20)
    age = models.IntegerField('年龄')
    salary = models.DecimalField('工资',max_digits=7,decimal_places=2,default=0.0)
    # 新增属性
    email = models.EmailField('邮箱',null=True)
    class Meta:
        db_table = 'user'  # 修改表名称
