from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField(verbose_name='Path')),
                ('datetime', models.DateField(verbose_name='Create Date Time')),
                ('extra', models.JSONField(blank=True, null=True, verbose_name='Extra Information')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_code', models.PositiveSmallIntegerField(default=200, verbose_name='Status Code')),
                ('datetime', models.DateField(verbose_name='Created Date Time')),
                ('extra', models.JSONField(blank=True, null=True, verbose_name='Extra Information')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangolin.request', verbose_name='Request')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, verbose_name='Key')),
                ('value', models.TextField(blank=True, null=True, verbose_name='Value')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangolin.response', verbose_name='Response')),
            ],
        ),
        migrations.CreateModel(
            name='RequestProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, verbose_name='Key')),
                ('value', models.TextField(blank=True, null=True, verbose_name='Value')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangolin.request', verbose_name='Request')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=15, verbose_name='Type')),
                ('msg', models.TextField(verbose_name='Message')),
                ('datetime', models.DateField(verbose_name='Created Date Time')),
                ('extra', models.JSONField(blank=True, null=True, verbose_name='Extra Information')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangolin.request', verbose_name='Request')),
            ],
        ),
    ]
