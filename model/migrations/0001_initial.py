# Generated by Django 4.0.5 on 2022-06-28 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_A', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('Direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('Pos_Geo', models.CharField(max_length=50, verbose_name='Posicion Geografica')),
            ],
        ),
        migrations.CreateModel(
            name='Arribo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_Mat', models.CharField(max_length=30, verbose_name='No. Matricula')),
                ('Fecha_in', models.DateTimeField(verbose_name='Fecha de Entrada')),
                ('Caracter', models.CharField(max_length=50, verbose_name='Caracter')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_C', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('Nacionalidad', models.CharField(max_length=50, verbose_name='Nacionalidad')),
                ('Tipo_C', models.CharField(max_length=75, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_I', models.CharField(max_length=40, verbose_name='Nombre')),
                ('Tipo_I', models.CharField(max_length=50, verbose_name='Tipo')),
                ('Ubicacion', models.CharField(max_length=50, verbose_name='Ubicacion')),
                ('Id_A', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.aeropuerto', verbose_name='ID Aeropuerto')),
            ],
        ),
        migrations.CreateModel(
            name='Nave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_Mat', models.CharField(max_length=30, unique=True, verbose_name='No. Matricula')),
                ('Clasific', models.CharField(max_length=50, verbose_name='Clasificacion')),
                ('Capacidad', models.SmallIntegerField(verbose_name='Capacidad')),
                ('No_Trip', models.SmallIntegerField(verbose_name='No. Tripulantes')),
                ('Total_P', models.SmallIntegerField(verbose_name='Total de Plazas')),
                ('Id_D', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.cliente', verbose_name='ID Dueño')),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_I', models.IntegerField(verbose_name='ID Instalacion')),
                ('Codigo', models.IntegerField(verbose_name='Codigo')),
                ('Tipo', models.CharField(max_length=40, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.IntegerField(verbose_name='Codigo')),
                ('Precio', models.FloatField(verbose_name='Precio')),
                ('Descripcion', models.CharField(max_length=250, verbose_name='Descripcion')),
                ('Id_I', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.instalacion', verbose_name='ID Instalacion')),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_in', models.DateTimeField(verbose_name='Fecha de Entrada')),
                ('Fecha_out', models.DateTimeField(verbose_name='Fecha de Salida')),
                ('EstadoNave', models.CharField(max_length=50, verbose_name='Estado')),
                ('Id_A', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.aeropuerto', verbose_name='ID Aeropuerto')),
                ('No_Mat', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='model.nave', verbose_name='No. Matricula')),
            ],
        ),
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_I', models.IntegerField(verbose_name='ID Instalacion')),
                ('Codigo', models.IntegerField(verbose_name='Codigo')),
                ('No_Mat', models.CharField(max_length=30, verbose_name='No. Matricula')),
                ('Fecha_in', models.DateTimeField(verbose_name='Fecha de Entrada')),
                ('Id_C', models.IntegerField(verbose_name='ID Cliente')),
                ('Valoracion', models.CharField(max_length=100, verbose_name='Valoracion')),
                ('Id_Ar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.arribo', verbose_name='ID Arribo')),
                ('Id_S', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.servicio', verbose_name='ID Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='ReparaNave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_I', models.IntegerField(verbose_name='ID Instalacion')),
                ('Codigo', models.IntegerField(verbose_name='Codigo')),
                ('Tipo', models.CharField(max_length=40, verbose_name='Tipo')),
                ('No_Mat', models.CharField(max_length=30, verbose_name='No. Matricula')),
                ('Fecha_in', models.DateTimeField(verbose_name='Fecha de Entrada')),
                ('Fecha_Ini', models.DateTimeField(verbose_name='Fecha Inicial')),
                ('Tiempo_P', models.DateTimeField(verbose_name='Tiempo Planificado')),
                ('Fecha_Fin', models.DateTimeField(verbose_name='Fecha Final')),
                ('Id_Rep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.reparacion', verbose_name='ID Reparacion')),
                ('Id_V', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.vuelo', verbose_name='ID Vuelo')),
            ],
        ),
        migrations.CreateModel(
            name='ReparacionesDependientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_I', models.IntegerField(verbose_name='ID Instalacion')),
                ('Codigo', models.IntegerField(verbose_name='Codigo')),
                ('Tipo', models.CharField(max_length=40, verbose_name='Tipo')),
                ('Id_IDep', models.IntegerField(verbose_name='ID Instalacion Dep')),
                ('Codigo_Dep', models.IntegerField(verbose_name='Codigo Dep')),
                ('Tipo_Dep', models.CharField(max_length=40, verbose_name='Tipo Dep')),
                ('Id_Rep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reparacion', to='model.reparacion', verbose_name='ID Reparacion')),
                ('Id_RepDep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependiente', to='model.reparacion', verbose_name='ID Reparacion Dep')),
            ],
        ),
        migrations.AddField(
            model_name='reparacion',
            name='Id_S',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.servicio', verbose_name='ID Servicio'),
        ),
        migrations.AddField(
            model_name='arribo',
            name='Id_C',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.cliente', verbose_name='ID Cliente'),
        ),
        migrations.AddField(
            model_name='arribo',
            name='Id_V',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.vuelo', verbose_name='ID Vuelo'),
        ),
        migrations.AddConstraint(
            model_name='vuelo',
            constraint=models.UniqueConstraint(fields=('No_Mat', 'Fecha_in'), name='Id del Vuelo'),
        ),
        migrations.AddConstraint(
            model_name='valoracion',
            constraint=models.UniqueConstraint(fields=('Id_I', 'Codigo', 'No_Mat', 'Fecha_in', 'Id_C'), name='Id de Valoracion'),
        ),
        migrations.AddConstraint(
            model_name='servicio',
            constraint=models.UniqueConstraint(fields=('Id_I', 'Codigo'), name='Id del Servicio'),
        ),
        migrations.AddConstraint(
            model_name='reparanave',
            constraint=models.UniqueConstraint(fields=('Id_I', 'Codigo', 'Tipo', 'No_Mat', 'Fecha_in', 'Fecha_Ini'), name='Id de Repara Nave'),
        ),
        migrations.AddConstraint(
            model_name='reparacionesdependientes',
            constraint=models.UniqueConstraint(fields=('Id_I', 'Codigo', 'Tipo', 'Id_IDep', 'Codigo_Dep', 'Tipo_Dep'), name='Id de Reparaciones Dep'),
        ),
        migrations.AddConstraint(
            model_name='reparacion',
            constraint=models.UniqueConstraint(fields=('Id_I', 'Codigo', 'Tipo'), name='Id de Reparacion'),
        ),
        migrations.AddConstraint(
            model_name='arribo',
            constraint=models.UniqueConstraint(fields=('No_Mat', 'Fecha_in', 'Id_C'), name='Id del Arribo'),
        ),
    ]
