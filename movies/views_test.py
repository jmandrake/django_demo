import django
from django.urls import reverse
from django.test import RequestFactory
from movies.models import Movie
from movies.views import add_movie
import pytest

def test_django_version():
    assert django.get_version() == '4.2.11'

""" Note:
The error message RuntimeError: Database access not allowed, use the "django_db" mark, or the "db" or "transactional_db" fixtures to enable it indicates that pytest is attempting to access the database during the test, but database access is not enabled by default.

To resolve this issue, you need to enable database access for your test using one of the following methods:

Use the django_db mark: The django_db mark is provided by the pytest-django plugin and enables database access for the test. You can use it by adding the @pytest.mark.django_db decorator to your test function or class.
"""
@pytest.mark.django_db
def test_add_movie_view():
    factory = RequestFactory()
    url = reverse('add_movie')  # Assuming the URL name for add_movie view is 'add_movie'
    data = {
        'title': 'Test Movie',
        'director': 'Test Director',
        'year': '2022',
        'description': 'Test description',
        'actors': 'Actor 1, Actor 2'
    }

    # Create a POST request
    request = factory.post(url, data)

    # Call the view function directly
    response = add_movie(request)

    # Check that the response is a redirect to /movies
    assert response.status_code == 302
    assert response.url == '/movies'

    # Check that the movie was created in the database
    assert Movie.objects.filter(title='Test Movie', director='Test Director', year='2022').exists()


def test_raise_error():
    with pytest.raises(ValueError):
        raise ValueError