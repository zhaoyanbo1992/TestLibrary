# Generated by Django 2.1 on 2018-11-04 09:46

from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.CharField(max_length=13, primary_key=True, serialize=False, verbose_name='ISBN')),
                ('title', models.CharField(max_length=128, verbose_name='书名')),
                ('author', models.CharField(max_length=32, verbose_name='作者')),
                ('press', models.CharField(max_length=64, verbose_name='出版社')),
                ('description', models.CharField(default='', max_length=1024, verbose_name='详细')),
                ('price', models.CharField(max_length=20, null=True, verbose_name='价格')),
                ('category', models.CharField(default='文学', max_length=64, verbose_name='分类')),
                ('cover', models.ImageField(blank=True, upload_to=library.models.custom_path, verbose_name='封面')),
                ('index', models.CharField(max_length=16, null=True, verbose_name='索引')),
                ('location', models.CharField(default='图书馆1楼', max_length=64, verbose_name='位置')),
                ('quantity', models.IntegerField(default=1, verbose_name='数量')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
            },
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(verbose_name='借出时间')),
                ('date_due_to_returned', models.DateField(verbose_name='应还时间')),
                ('date_returned', models.DateField(null=True, verbose_name='还书时间')),
                ('amount_of_fine', models.FloatField(default=0.0, verbose_name='欠款')),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book', verbose_name='ISBN')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Reader', verbose_name='读者')),
            ],
            options={
                'verbose_name': '借阅',
                'verbose_name_plural': '借阅',
            },
        ),
    ]
