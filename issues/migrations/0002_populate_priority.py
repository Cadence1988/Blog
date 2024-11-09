from django.db import migrations

def populate_priorities(apps, schema_editor):
    Priority = apps.get_model('issues', 'Priority')
    Priority.objects.bulk_create([
        Priority(name='low', description='A low priority issue'),
        Priority(name='medium', description='An issue of medium priority'),
        Priority(name='high', description='A high priority issue'),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_priorities),
    ]
