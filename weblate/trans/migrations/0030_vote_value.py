# Generated by Django 2.2.1 on 2019-05-21 18:16

from django.db import migrations

from weblate.utils.db import table_has_row


class RemoveFieldOptional(migrations.RemoveField):
    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        if not table_has_row(schema_editor.connection, "trans_vote", "positive"):
            return
        super().database_forwards(app_label, schema_editor, from_state, to_state)


class Migration(migrations.Migration):

    dependencies = [("trans", "0029_vote_value")]

    operations = [RemoveFieldOptional(model_name="vote", name="positive")]