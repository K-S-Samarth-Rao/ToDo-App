
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todo_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='duedate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
