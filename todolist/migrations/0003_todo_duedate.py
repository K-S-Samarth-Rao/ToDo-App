
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20200329_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='duedate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]