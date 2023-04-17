from django.db import models

class SaveModelIdMixin(models.Model):
    id = models.Charfield(primary_key=True, max_length=50, default=uuid.uuid4())
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super("%(app_label)s_%(class)s_created", self).save()

