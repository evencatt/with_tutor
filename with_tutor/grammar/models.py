from django.db import models

class GrammarTheme(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        'Image',
        upload_to='grammar_theme',
        blank=True
    )


class GrammarSubsections(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        'Image',
        upload_to='grammar_subsections',
        blank=True,

    )
    theme = models.ForeignKey(
        GrammarTheme,
        on_delete=models.CASCADE,
        related_name='grammar_subsection',
    )


class GrammarMaterial(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        'Image',
        upload_to='grammar_material',
        blank=True
    )
    subsection = models.ForeignKey(
        GrammarSubsections,
        on_delete=models.CASCADE,
        related_name='grammar_material',
    )


class GrammarVoices(models.Model):
    voice = models.FileField(upload_to='grammar_voices')
    material = models.ForeignKey(
        GrammarMaterial,
        on_delete=models.CASCADE,
        related_name='material_voices'
    )
