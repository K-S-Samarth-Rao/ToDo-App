
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20200330_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='useremail',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
