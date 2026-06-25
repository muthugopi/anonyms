import authentication.managers
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_remove_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', authentication.managers.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('moderator', 'Moderator'), ('admin', 'Admin')], default='student', max_length=10, null=True),
        ),
    ]
