from django.test import TestCase
from django.contrib.auth import get_user_model
from bizzfuzz.forms import RegistrationForm, ChangeForm
from django.urls import reverse
from django.shortcuts import get_object_or_404



class UserModelCreationTests(TestCase):

    def test_user_creation(self):
        userModel = get_user_model()
        user_1 = userModel(username='user_1', birth_date='1993-01-15', random_number=3)
        user_1.save()
        self.assertEqual(len(userModel.objects.all()), 1)


    def test_user_creation_valid_birth_date(self):
        form_data = {
            "username" : 'user_1', 
            "birth_date" : '2000-01-01', 
            "password1" : 'zaqxsw123',
            "password2" : 'zaqxsw123',
            }
        
        form = RegistrationForm(form_data)
        self.assertTrue(form.is_valid())


    def test_user_creation_future_birth_date(self):
        form_data = {
            "username" : 'user_1', 
            "birth_date" : '2100-01-01', 
            "password1" : 'zaqxsw123',
            "password2" : 'zaqxsw123',
            }

        form = RegistrationForm(data = form_data)
        self.assertFalse(form.is_valid())



class IndexViewTests(TestCase):

    def test_index_view_no_users(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No users are available.', html=True)
        self.assertQuerysetEqual(response.context["users_list"], [])


    def test_index_view_with_user(self):
        userModel = get_user_model()
        user_1 = userModel(username='user_1', birth_date='1993-01-15', random_number=3)
        user_1.save()

        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context["users_list"], 
            ['<CustomUser: user_1>']
        )


    def test_index_view_with_user_bizz(self):
        userModel = get_user_model()
        user_1 = userModel(username='user_1', birth_date='1993-01-15', random_number=3)
        user_1.save()

        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Bizz', html=True)


    def test_index_view_with_user_fuzz(self):
        userModel = get_user_model()
        user_1 = userModel(username='user_1', birth_date='1993-01-15', random_number=5)
        user_1.save()

        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Fuzz', html=True)



class EditViewTests(TestCase):

    def test_equals_edited_user(self):
        userModel = get_user_model()
        user_1 = userModel(id = 1, username='user_1', birth_date='1993-01-15', random_number=5)
        user_1.save()
        userInstance = get_object_or_404(userModel, pk=1)
        edit_data = {
            "username" : 'user_2', 
            "birth_date" : '2000-10-10', 
            }

        form = ChangeForm(edit_data, instance = userInstance)
        user = form.save()
        user.save()

        id_valid = False
        random_number_valid = False
        username_valid = False
        birth_date_valid = False

        if user_1.id == user.id :
            id_valid = True
        if user_1.random_number == user.random_number:
            random_number_valid = True
        if user_1.username != user.username:
            username_valid = True
        if user_1.birth_date != user.birth_date:
            birth_date_valid = True

        self.assertTrue(id_valid and random_number_valid and username_valid and birth_date_valid)