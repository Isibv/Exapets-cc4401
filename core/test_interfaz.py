"""Pruebas de la interfaz de usuario: registro, login, logout y navegación."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import RegistroForm

Usuario = get_user_model()

# Contraseña que cumple todos los validadores de Django (larga, no común, no numérica)
CLAVE = "Gato-Feliz-2026"


class RegistroTests(TestCase):
    """Flujo de creación de cuenta."""

    def datos_validos(self, **cambios):
        datos = {"username": "luciano", "password1": CLAVE, "password2": CLAVE}
        datos.update(cambios)
        return datos

    def test_el_formulario_de_registro_usa_el_modelo_usuario(self):
        self.assertIs(RegistroForm._meta.model, Usuario)

    def test_pagina_de_registro_carga(self):
        response = self.client.get(reverse("core:registro"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], RegistroForm)

    def test_registro_valido_crea_usuario_y_redirige_al_login(self):
        response = self.client.post(reverse("core:registro"), self.datos_validos())
        self.assertRedirects(response, reverse("core:login"))
        self.assertTrue(Usuario.objects.filter(username="luciano").exists())

    def test_registro_valido_muestra_mensaje_de_exito(self):
        response = self.client.post(reverse("core:registro"), self.datos_validos(), follow=True)
        self.assertContains(response, "Cuenta creada exitosamente")

    def test_contrasenas_distintas_muestran_error_y_no_crean_usuario(self):
        datos = self.datos_validos(password2="Otra-Clave-Distinta-9")
        response = self.client.post(reverse("core:registro"), datos)
        self.assertEqual(response.status_code, 200)
        self.assertIn("password2", response.context["form"].errors)
        self.assertFalse(Usuario.objects.filter(username="luciano").exists())

    def test_contrasena_debil_muestra_error_y_no_crea_usuario(self):
        datos = self.datos_validos(password1="123", password2="123")
        response = self.client.post(reverse("core:registro"), datos)
        self.assertEqual(response.status_code, 200)
        self.assertIn("password2", response.context["form"].errors)
        self.assertFalse(Usuario.objects.filter(username="luciano").exists())

    def test_nombre_de_usuario_repetido_muestra_error(self):
        Usuario.objects.create_user(username="luciano", password=CLAVE)
        response = self.client.post(reverse("core:registro"), self.datos_validos())
        self.assertEqual(response.status_code, 200)
        self.assertIn("username", response.context["form"].errors)
        self.assertEqual(Usuario.objects.count(), 1)

    def test_usuario_con_sesion_es_enviado_a_sus_mascotas(self):
        usuario = Usuario.objects.create_user(username="ana", password=CLAVE)
        self.client.force_login(usuario)
        response = self.client.get(reverse("core:registro"))
        self.assertRedirects(response, reverse("mascotas:mis_mascotas"))


class LoginLogoutTests(TestCase):
    """Inicio y cierre de sesión."""

    def setUp(self):
        self.usuario = Usuario.objects.create_user(username="ana", password=CLAVE)

    def test_login_valido_lleva_a_mis_mascotas(self):
        response = self.client.post(reverse("core:login"), {"username": "ana", "password": CLAVE})
        self.assertRedirects(response, reverse("mascotas:mis_mascotas"))

    def test_login_respeta_la_pagina_pedida_antes_de_iniciar_sesion(self):
        destino = reverse("mascotas:crear_mascota")
        datos = {"username": "ana", "password": CLAVE, "next": destino}
        response = self.client.post(reverse("core:login"), datos)
        self.assertRedirects(response, destino)

    def test_credenciales_incorrectas_muestran_error_y_no_inician_sesion(self):
        response = self.client.post(reverse("core:login"), {"username": "ana", "password": "incorrecta"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].non_field_errors())
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_pagina_protegida_sin_sesion_redirige_al_login(self):
        destino = reverse("mascotas:mis_mascotas")
        response = self.client.get(destino)
        self.assertRedirects(response, f"{reverse('core:login')}?next={destino}")

    def test_usuario_con_sesion_en_el_login_es_enviado_a_sus_mascotas(self):
        self.client.force_login(self.usuario)
        response = self.client.get(reverse("core:login"))
        self.assertRedirects(response, reverse("mascotas:mis_mascotas"))

    def test_logout_por_post_cierra_la_sesion_y_vuelve_al_login(self):
        self.client.force_login(self.usuario)
        response = self.client.post(reverse("core:logout"))
        self.assertRedirects(response, reverse("core:login"))
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_logout_por_get_no_esta_permitido(self):
        self.client.force_login(self.usuario)
        response = self.client.get(reverse("core:logout"))
        self.assertEqual(response.status_code, 405)


class NavegacionTests(TestCase):
    """Barra de navegación compartida por todas las vistas."""

    def test_visitante_ve_enlaces_de_login_y_registro(self):
        response = self.client.get(reverse("core:home"))
        self.assertContains(response, reverse("core:login"))
        self.assertContains(response, reverse("core:registro"))
        self.assertNotContains(response, "Cerrar sesión")

    def test_usuario_con_sesion_ve_su_nombre_el_cierre_de_sesion_y_sus_mascotas(self):
        usuario = Usuario.objects.create_user(username="ana", password=CLAVE)
        self.client.force_login(usuario)
        response = self.client.get(reverse("core:home"))
        self.assertContains(response, "Hola, ana")
        self.assertContains(response, "Cerrar sesión")
        self.assertContains(response, reverse("mascotas:mis_mascotas"))

    def test_las_vistas_de_mascotas_usan_la_navegacion_global(self):
        usuario = Usuario.objects.create_user(username="ana", password=CLAVE)
        self.client.force_login(usuario)
        response = self.client.get(reverse("mascotas:mis_mascotas"))
        self.assertContains(response, "Hola, ana")
        self.assertContains(response, "Cerrar sesión")
