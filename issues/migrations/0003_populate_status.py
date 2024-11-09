from django.db import migrations

def populate_status(apps, schemaeditor):
    Status = apps.get_model('issues', 'Status')
    statuses = [
        ("new", "A new issue"),
        ("in_progress", "An issue that is currently in progress"),
        ("resolved", "An issue that has been resolved"),
        ("closed", "An issue that has been closed"),
    ]
    for code, description in statuses:
        Status.objects.create(code=code, description=description)

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_populate_priority'),
    ]

    operations = [
        migrations.RunPython(populate_status),
    ]

