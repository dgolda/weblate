# Generated by Django 2.2 on 2019-05-10 13:01

from django.db import migrations


def migrate_flags(apps, schema_editor):
    """Update the repo_scope flag."""
    Addon = apps.get_model("addons", "Addon")
    db_alias = schema_editor.connection.alias
    Addon.objects.using(db_alias).filter(
        name__in=("weblate.discovery.discovery", "weblate.git.squash")
    ).update(repo_scope=True)
    Addon.objects.using(db_alias).filter(
        name__in=("weblate.removal.comments", "weblate.removal.suggestions")
    ).update(project_scope=True)


class Migration(migrations.Migration):

    dependencies = [("addons", "0014_auto_20190510_1325")]

    operations = [
        migrations.RunPython(migrate_flags, migrations.RunPython.noop, elidable=True)
    ]