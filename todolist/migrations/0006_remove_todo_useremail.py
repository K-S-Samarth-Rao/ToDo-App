
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_todo_useremail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='useremail',
        ),
    ]
