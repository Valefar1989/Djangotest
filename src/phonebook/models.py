from django.db import models

class Persona(models.Model):
    # pk/id
    name = models.CharField("Contack name", max_length=30)
    
    def __str__(self) -> str:
        return self.name

    def all_phones(self):
        return ", ".join([phone.phone for phone in self.phones.all()])

class Phone(models.Model):
    phone = models.CharField("Phone", max_length=100)
    contack = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="phones")

    def __str__(self):
        return self.phone

        