from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path("", views.index, name='home'),  # http://127.0.0.1:8000
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('addpage', views.addpage, name='addpage'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    # path("cats/<int:cat_id>/", views.categories, name='cats_id'),  # http://127.0.0.1:8000/cats/123/
    # path("cats/<slug:cat_slug>/", views.categories_by_slug, name='cats'),  # http://127.0.0.1:8000/cats/asdf/
    # path("archive/<year4:year>/", views.archive, name='archive')
]
