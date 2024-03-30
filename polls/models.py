from django.db import models

# Create your models here.


class s(models.Model):
    stuno = models.CharField(max_length=10)
    stuname = models.CharField(max_length=10)
    stuclass = models.CharField(max_length=10)
    stuage = models.CharField(max_length=10)
    stusex = models.CharField(max_length=10)
    stuphone = models.CharField(max_length=20)
    stuaddress = models.CharField(max_length=10)

    # class Meta:
    #     indexex = []


# new_student = s(
#     stuno="001",
#     stuname="张三",
#     stuclass="一班",
#     stuage="18",
#     stusex="男",
#     stuphone="12345678901",
#     stuaddress="北京",
# )
# new_student.save()
class student(models.Model):
    stuno = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=3)
    sex = models.CharField(max_length=3)
    birthdate = models.DateField(blank=True)


class scores(models.Model):
    id = models.BigIntegerField(max_length=20, primary_key=True)
    stuno = models.CharField(max_length=12)
    cno = models.CharField(max_length=3)
    grade = models.SmallIntegerField(max_length=6)


# new_score = scores(id=12, stuno="112208020307", cno="010", grade=80)
# new_score.save()
