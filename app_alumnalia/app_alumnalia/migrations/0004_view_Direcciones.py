# Generated by Django 5.1.3 on 2024-12-18 03:46

from django.db import migrations 

class Migration(migrations.Migration): 
    dependencies = [("app_alumnalia", "0003_alter_comarca_pk_com_and_more"), ] 
    operations = [ 
        migrations.RunSQL( 
            sql=''' CREATE VIEW view_Direcciones AS
            SELECT pk_com , nom_com, pk_pro, nom_pro, pk_mun, nom_mun   
            from Municipios as mun
            inner join Comarca as co
            on mun.fk_com_id = co.pk_com
            inner join Comarca_provincias as cop
            on co.pk_com=cop.fk_com_id
            inner join Provincias AS pr 
            on cop.fk_pro_id=pr.pk_pro; ''', 
            reverse_sql='DROP VIEW IF EXISTS view_Direcciones;' 
        ),
]
