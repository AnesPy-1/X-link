from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_management', '0002_customer_is_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitecontext',
            name='footer_enamad_badge',
            field=models.URLField(blank=True, help_text='eNamad badge URL/image', null=True),
        ),
        migrations.AddField(
            model_name='sitecontext',
            name='hero_active_users_label',
            field=models.CharField(default='کاربر فعال', help_text='Hero stat label for active users', max_length=100),
        ),
        migrations.AddField(
            model_name='sitecontext',
            name='hero_active_users_text',
            field=models.CharField(default='5,000+', help_text='Hero stat number for active users', max_length=50),
        ),
        migrations.AddField(
            model_name='sitecontext',
            name='hero_support_label',
            field=models.CharField(default='پشتیبانی', help_text='Hero stat label for support', max_length=100),
        ),
        migrations.AddField(
            model_name='sitecontext',
            name='hero_support_text',
            field=models.CharField(default='24/7', help_text='Hero stat number/text for support', max_length=50),
        ),
        migrations.AddField(
            model_name='sitecontext',
            name='hero_templates_label',
            field=models.CharField(default='قالب حرفه‌ای', help_text='Hero stat label for templates', max_length=100),
        ),
        migrations.AddField(
            model_name='sitecontext',
            name='hero_templates_text',
            field=models.CharField(default='20+', help_text='Hero stat number for templates', max_length=50),
        ),
        migrations.AddField(
            model_name='sitecontext',
            name='support_logo',
            field=models.ImageField(blank=True, help_text='Support logo icon for floating action button', null=True, upload_to='support'),
        ),
        migrations.AddField(
            model_name='sitecontext',
            name='support_url',
            field=models.URLField(blank=True, help_text='Support destination URL', null=True),
        ),
    ]
