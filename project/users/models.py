import uuid

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, UUIDField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """Overriding the default User model with our own fields."""

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
