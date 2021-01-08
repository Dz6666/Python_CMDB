from django.db import models  # 调用django的models类
# Create your models here.
class User(models.Model):     # 创建一个user表,建立创建表类
    SEX = (
        ('0', '男'),
        ('1', '女'),
    )
    # 创建name字段，字符串类型，最大长度不能超过20，添加帮助注释为"用户名"
    name = models.CharField(max_length = 20,
                            help_text="用户名")
    # 创建password字段，字符串类型，最大长度不能超过32，添加帮助注释为"密码"
    password = models.CharField(max_length = 32,
                                help_text="密码")
   
    # 性别字段为一个int整形，仅能从上面定义的SEX中选择（男/女），null=True数据库验证允许为空，blank=True添加时允许为空（django字段表单验证允许为空）
    sex = models.IntegerField(choices = SEX, null=True, blank=True)  # 数据库存0，1，展示男女
   
    # 当对象以字符串返回时，把name返回
    def __str__(self):  
        return self.name