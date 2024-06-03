# Generated by Django 5.0.6 on 2024-06-02 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('uso', models.CharField(max_length=50, null=True)),
                ('descripcion', models.TextField(null=True)),
                ('tipo_und', models.CharField(max_length=50, null=True)),
                ('tipo_producto', models.CharField(max_length=50, null=True)),
                ('tiempo_rp', models.CharField(max_length=50, null=True)),
                ('nro_parte', models.CharField(max_length=50, null=True)),
                ('compania', models.CharField(max_length=50, null=True)),
                ('clase_articulo', models.CharField(max_length=50, null=True)),
                ('renglon', models.CharField(max_length=50, null=True)),
                ('cod_renglon', models.CharField(max_length=50, null=True)),
                ('ubicacion', models.CharField(max_length=50, null=True)),
                ('inv_max', models.IntegerField(null=True)),
                ('inv_min', models.IntegerField(null=True)),
                ('fecha_revision', models.DateField(null=True)),
                ('pto_pedido', models.CharField(max_length=50, null=True)),
                ('equipos', models.CharField(max_length=50, null=True)),
                ('costo_inicial', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('costo_promedio', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True, null=True)),
                ('usuario', models.CharField(max_length=50, null=True)),
                ('clasificacion', models.CharField(max_length=50, null=True)),
                ('articulo_solicitado', models.CharField(max_length=50, null=True)),
                ('comentario', models.TextField(null=True)),
                ('codigo_arancelario', models.CharField(max_length=50, null=True)),
                ('contractual', models.BooleanField(default=False)),
                ('auxiliar', models.BooleanField(default=False)),
                ('controlado', models.BooleanField(default=False)),
                ('cicpc', models.BooleanField(default=False)),
                ('darfa', models.BooleanField(default=False)),
                ('sada', models.BooleanField(default=False)),
                ('fecha_desde_cicpc', models.DateField(null=True)),
                ('fecha_desde_darfa', models.DateField(null=True)),
                ('fecha_desde_sada', models.DateField(null=True)),
                ('fecha_venc_cicpc', models.DateField(null=True)),
                ('fecha_venc_darfa', models.DateField(null=True)),
                ('fecha_venc_sada', models.DateField(null=True)),
                ('cant_controlada', models.IntegerField(null=True)),
            ],
        ),
    ]
