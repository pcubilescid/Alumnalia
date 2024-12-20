# Generated by Django 5.1.2 on 2024-12-15 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "app_alumnalia",
            "0009_familia_profesion_rename_pk_com_comarca_pk_com_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Estudio_Profesion",
            fields=[
                (
                    "pk_est_pro",
                    models.CharField(
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                        verbose_name="id de Estudio Profecional",
                    ),
                ),
                (
                    "desc_est_pro",
                    models.CharField(
                        max_length=200,
                        verbose_name="Descripcion de la Estudoi Profesional",
                    ),
                ),
            ],
            options={
                "db_table": "Estudio_Profecional",
            },
        ),
        migrations.CreateModel(
            name="OfertaEstudio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom_Ofe_est", models.CharField(max_length=200)),
                ("inst_Ofe_est", models.CharField(max_length=200)),
                (
                    "niv_Ofe_est",
                    models.CharField(
                        choices=[
                            ("BACH", "Bachillerato"),
                            ("LIC", "Licenciatura"),
                            ("MAST", "Máster"),
                            ("DOC", "Doctorado"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "mod_Ofe_est",
                    models.CharField(
                        choices=[
                            ("PRESENCIAL", "Presencial"),
                            ("ONLINE", "Online"),
                            ("MIXTO", "Mixto"),
                        ],
                        max_length=10,
                    ),
                ),
                ("dur_Ofe_est", models.IntegerField(help_text="Duración en meses")),
                ("desc_Ofe_est", models.TextField(blank=True, null=True)),
                ("fecha_inicio", models.DateField()),
                ("fecha_fin", models.DateField()),
                ("url_Ofe_est", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="dat_per",
            name="sex_per",
            field=models.IntegerField(
                choices=[
                    ("", "Seleccione una opción"),
                    (1, "Mujer"),
                    (2, "Hombre"),
                    (3, "Prefiero no específicar"),
                    (4, "Otro"),
                ],
                default="",
                verbose_name="Género de la persona",
            ),
        ),
        migrations.AlterField(
            model_name="inf_prof",
            name="cert_inf_pro",
            field=models.IntegerField(
                choices=[
                    ("", "Seleccione una opción"),
                    (1, "Sí"),
                    (2, "No"),
                    (3, "Especificar"),
                ],
                default="",
                verbose_name="¿Tienes alguna certificación docente?",
            ),
        ),
        migrations.AlterField(
            model_name="inf_prof",
            name="comp_dig_inf_pro",
            field=models.IntegerField(
                choices=[
                    ("", "Seleccione una opción"),
                    (1, "Sí"),
                    (2, "No"),
                    (3, "Especificar"),
                ],
                default="",
                verbose_name="¿Posees competencias digitales específicas (ej. DigCompEdu)?",
            ),
        ),
        migrations.AlterField(
            model_name="inf_prof",
            name="exp_inf_pro",
            field=models.IntegerField(
                choices=[
                    ("", "Seleccione una opción"),
                    (1, "Menos de 1 año"),
                    (2, "De 1 a 3 años"),
                    (3, "De 4 a 6 años"),
                    (4, "Más de 6 años"),
                ],
                default="",
                verbose_name="¿Cuántos años de experiencia tienes como formador/a?",
            ),
        ),
        migrations.AlterField(
            model_name="inf_prof",
            name="for_imp_inf_pro",
            field=models.IntegerField(
                choices=[
                    ("", "Seleccione una opción"),
                    (1, "Formación profesional"),
                    (2, "Formación universitaria"),
                    (3, "Formación empresarial"),
                    (4, "Cursos en línea"),
                    (5, "Otros"),
                ],
                default="",
                verbose_name="Qué tipo de formación has impartido",
            ),
        ),
        migrations.AlterField(
            model_name="inf_prof",
            name="franja_inf_pro",
            field=models.IntegerField(
                choices=[
                    ("", "Seleccione una opción"),
                    (1, "Mañana (8:00-14:00)"),
                    (2, "Tarde (14:00-20:00)"),
                    (3, "Noche (20:00-23:00)"),
                ],
                default="",
                verbose_name="En qué franjas horarias estás disponible para impartir clases?",
            ),
        ),
        migrations.AlterField(
            model_name="inf_prof",
            name="herr_inf_pro",
            field=models.IntegerField(
                choices=[
                    ("", "Seleccione una opción"),
                    (1, "Moodle"),
                    (2, "Microsoft Teams"),
                    (3, "Zoom"),
                    (4, "Google Classroom"),
                    (5, "Otros"),
                ],
                default="",
                verbose_name="¿Qué herramientas tecnológicas utilizas en tus clases?",
            ),
        ),
        migrations.AlterField(
            model_name="inf_prof",
            name="mod_inf_pro",
            field=models.IntegerField(
                choices=[
                    ("", "Seleccione una opción"),
                    (1, "Presencial"),
                    (2, "En línea"),
                    (3, "Mixta"),
                ],
                default="1",
                verbose_name="Qué modalidades de enseñanza prefieres impartir",
            ),
        ),
        migrations.AlterField(
            model_name="inf_prof",
            name="tipo_alu_inf_pro",
            field=models.IntegerField(
                choices=[
                    ("", "Seleccione una opción"),
                    (1, "Jóvenes"),
                    (2, "Adultos"),
                    (3, "Empresas"),
                    (4, "Otros"),
                ],
                default="",
                verbose_name="Qué tipo de alumnado prefieres formar",
            ),
        ),
        migrations.AlterField(
            model_name="inf_prof",
            name="tit_inf_pro",
            field=models.IntegerField(
                choices=[
                    ("", "Seleccione una opción"),
                    (1, "Técnico/a"),
                    (2, "Grado universitario"),
                    (3, "Máster"),
                    (4, "Doctorado"),
                    (5, "Otros"),
                ],
                default="",
                verbose_name="Título académico más alto obtenido",
            ),
        ),
    ]
