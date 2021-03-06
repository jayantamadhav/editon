# Generated by Django 2.2.6 on 2019-11-20 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorOfTheMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Author Name')),
                ('author_desg', models.CharField(blank=True, max_length=500, null=True, verbose_name='Author Designation')),
                ('author_dp', models.ImageField(blank=True, null=True, upload_to='author_of_the_month/')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=500, verbose_name='Article')),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('article_type', models.CharField(max_length=40, verbose_name='Type')),
                ('article_abbr', models.CharField(blank=True, max_length=100, null=True, verbose_name='Abbr')),
                ('article', models.FileField(blank=True, upload_to='features_articles/')),
                ('abstract', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Abstract')),
                ('doi', models.CharField(blank=True, max_length=100, null=True, verbose_name='DOI')),
                ('publish_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_name', models.CharField(max_length=100, verbose_name='Journal')),
                ('abbr_title', models.CharField(max_length=100, verbose_name='Abbr. Title')),
                ('journal_url', models.CharField(max_length=50, verbose_name='Journal URL')),
                ('subject', models.CharField(blank=True, max_length=50, null=True, verbose_name='subject')),
                ('issn_print', models.CharField(max_length=50, verbose_name='ISSN Print')),
                ('issn_online', models.CharField(max_length=50, verbose_name='ISSN Online')),
                ('frequency', models.CharField(blank=True, default='N/A', max_length=50, verbose_name='Frequency')),
                ('chief_editor', models.CharField(max_length=50, verbose_name='chief editor')),
                ('origin_country', models.CharField(blank=True, default='N/A', max_length=50, verbose_name='Origin')),
                ('language', models.CharField(blank=True, default='N/A', max_length=50, verbose_name='Language')),
                ('publisher', models.CharField(blank=True, default='N/A', max_length=50, verbose_name='Publisher')),
                ('journal_info', models.TextField(max_length=2000, verbose_name='Info')),
                ('journal_scope', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Scope')),
                ('journal_cover', models.ImageField(upload_to='journals/', verbose_name='Cover')),
                ('journal_thumb', models.ImageField(upload_to='journals/', verbose_name='Thumbnail')),
            ],
        ),
        migrations.CreateModel(
            name='MemberIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(blank=True, upload_to='membersin/')),
                ('company_name', models.CharField(blank=True, max_length=200, verbose_name='Company name')),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimony', models.TextField(max_length=2000, verbose_name='testimony')),
                ('testimony_name', models.CharField(max_length=200, verbose_name='Name')),
                ('testimony_desg', models.CharField(blank=True, max_length=200, null=True, verbose_name='Designation(if any)')),
                ('testimony_dp', models.ImageField(blank=True, null=True, upload_to='testimony_dp/')),
            ],
        ),
        migrations.CreateModel(
            name='TopEditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=200, verbose_name='Designation')),
                ('editor_name', models.CharField(max_length=200, verbose_name='Name')),
                ('editor_info', models.CharField(max_length=1000, verbose_name='Info')),
                ('profile', models.ImageField(blank=True, null=True, upload_to='editors/')),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_name', models.CharField(max_length=100, verbose_name='Volume name')),
                ('volume_year', models.PositiveIntegerField(verbose_name='Year')),
                ('issue_name', models.CharField(max_length=100, verbose_name='Issue')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Journal')),
            ],
        ),
        migrations.CreateModel(
            name='JournalFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.PositiveIntegerField(verbose_name='USD')),
                ('inr', models.PositiveIntegerField(verbose_name='INR')),
                ('kes', models.PositiveIntegerField(verbose_name='KES')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Journal')),
            ],
        ),
        migrations.CreateModel(
            name='Indexing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Indexing Name')),
                ('index_picture', models.ImageField(blank=True, null=True, upload_to='indexing/')),
                ('index_url', models.CharField(blank=True, max_length=500, null=True, verbose_name='Indexing URL')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Journal')),
            ],
        ),
        migrations.CreateModel(
            name='ImpactFactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impact_factor', models.CharField(blank=True, max_length=300, null=True, verbose_name='Impact Factor')),
                ('impact_year', models.CharField(blank=True, max_length=500, null=True, verbose_name='Impact Factor Year')),
                ('impact_url', models.CharField(blank=True, max_length=500, null=True, verbose_name='Impact URL')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Journal')),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=200, verbose_name='Designation')),
                ('editor_name', models.CharField(max_length=200, verbose_name='Name')),
                ('editor_info', models.CharField(max_length=1000, verbose_name='Info')),
                ('profile', models.ImageField(blank=True, null=True, upload_to='editors/')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Journal')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_type', models.CharField(max_length=40, verbose_name='Type')),
                ('article_name', models.CharField(max_length=500, verbose_name='Article')),
                ('article_abbr', models.CharField(blank=True, max_length=100, null=True, verbose_name='Abbr')),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('article', models.FileField(upload_to='articles/')),
                ('abstract', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Abstract')),
                ('doi', models.CharField(max_length=100, verbose_name='DOI')),
                ('publish_date', models.DateField()),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Volume')),
            ],
        ),
    ]
