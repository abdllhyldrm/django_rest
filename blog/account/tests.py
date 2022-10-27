from rest_framework.test import APITestCase
from django.urls import reverse

# doğru veriler ile kayıt işlemi yap
# şifre invalid olabilir
# kullanıcı adı kayıtlı olabilir
# üye girişi yaptıysak o sayfa gözükmemeli
# token ile giriş işlemi yapıldığında 403 hatası

class UserRegistirationTestCase(APITestCase):
  url = reverse("account : register")
  
  def test_user_registiration(self):
    """
    doğru veriler ile kayıt işlemi yap
    
    """
    data = {
      "username" : "user",
      "password" : "Abd*0589"
    }
    
    response = self.client.post(self.url, data)
    self.assertEqual(200, response.status_code)
    
