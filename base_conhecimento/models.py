from django.db import models

class Defeito(models.Model):
    maquina = models.CharField(max_length=100, db_index=True)
    descricao = models.TextField(max_length=250, null = False, blank = False)
    solucao = models.TextField(max_length=250, null=False, blank=False)
    causa_possivel = models.TextField(max_length=250)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Defeito'

    def __str__(self):
        return f"{self.maquina}: {self.descricao} | solucao: {self.solucao} | causa_possivel: {self.causa_possivel}"

    @classmethod
    def buscar_por_maquina(cls, nome_maquina):
        return cls.objects.filter(maquina__icontains=nome_maquina)
