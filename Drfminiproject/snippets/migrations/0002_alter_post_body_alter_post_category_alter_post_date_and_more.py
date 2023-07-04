# Generated by Django 4.2.3 on 2023-07-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="body",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.IntegerField(
                choices=[
                    (1, "월"),
                    (2, "화"),
                    (3, "수"),
                    (4, "목"),
                    (5, "금"),
                    (6, "토"),
                    (7, "일"),
                ],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]