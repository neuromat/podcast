# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-31 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170411_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='podcastfile',
            field=models.FileField(default='', max_length=150, upload_to='uploads', verbose_name='Carregue o arquivo de audio'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='transcription',
            field=mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Insira a transcrição ou algum conteúdo extra'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Vídeo (Material extra ou relacionado ao Podcast'),
        ),
    ]
