from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Mascota


User = get_user_model()


class MascotaTests(TestCase):

    # Create two different users
    def setUp(self):
        self.usuario1 = User.objects.create_user(
            username="usuario1",
            password="test12345"
        )

        self.usuario2 = User.objects.create_user(
            username="usuario2",
            password="test12345"
        )

        # Create one pet for each user
        self.mascota1 = Mascota.objects.create(
            nombre="Luna",
            especie="Perro",
            sexo="H",
            dueño=self.usuario1
        )

        self.mascota2 = Mascota.objects.create(
            nombre="Milo",
            especie="Gato",
            sexo="M",
            dueño=self.usuario2
        )

    """Checks that a pet is correctly linked to its owner."""
    def test_mascota_tiene_dueño(self):
        self.assertEqual(self.mascota1.dueño, self.usuario1)

    """Checks that a user only sees their own pets."""
    def test_usuario_solo_ve_sus_mascotas(self):
        self.client.force_login(self.usuario1)

        response = self.client.get(
            reverse("mascotas:mis_mascotas")
        )

        self.assertContains(response, "Luna")
        self.assertNotContains(response, "Milo")

    """Checks that a user cannot access another user's pet."""
    def test_usuario_no_puede_ver_mascota_ajena(self):
        self.client.force_login(self.usuario1)

        response = self.client.get(
            reverse(
                "mascotas:detalle_mascota",
                args=[self.mascota2.pk]
            )
        )

        self.assertEqual(response.status_code, 404)