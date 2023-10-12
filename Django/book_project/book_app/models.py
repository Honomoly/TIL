from django.db import models

# Create your models here.
# 책 정보
class Book(models.Model):
    book_no = models.IntegerField(db_column='bookNo', primary_key=True)  # Field name made lowercase.
    book_name = models.CharField(db_column='bookName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    book_author = models.CharField(db_column='bookAuthor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    book_price = models.IntegerField(db_column='bookPrice', blank=True, null=True)  # Field name made lowercase.
    book_date = models.DateField(db_column='bookDate', blank=True, null=True)  # Field name made lowercase.
    book_stock = models.IntegerField(db_column='bookStock', blank=True, null=True)  # Field name made lowercase.
    pub_no = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='pubNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'

# 출판사 정보
class Publisher(models.Model):
    pub_no = models.IntegerField(db_column='pubNo', primary_key=True)  # Field name made lowercase.
    pub_name = models.CharField(db_column='pubName', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publisher'

    def __str__(self):
        return self.pub_name