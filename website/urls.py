from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path("", views.index, name="index_new"),
    path("sections/<int:num>", views.section, name="section"),
    path('form.html', views.form_page_view, name='form'),
    path('about_colors.html', views.teoria_page_view, name='about_colors'),
    path('about_site.html', views.about_site_page_view, name='about_site'),
    path('quizz.html', views.new_quizz_view, name='quizz'),
    path('show_quizz.html', views.show_quizz_page_view, name='show_quizz'),
    path('contatos.html', views.new_contato_view, name='contatos'),
    path('show_contato.html', views.show_contato_page_view, name='show_contato'),
    path('edita_contato.html/<int:contato_id>', views.edita_contato_view, name='edita_contato'),
    path('apaga_contato/<int:contato_id>', views.apaga_contato_view, name='apaga_contato'),
    path('comentarios.html', views.new_comentario_view, name='comentarios'),
    path('color-pages/color-page-001.html', views.color_page_001, name='color_001'),
    path('color-pages/color-page-002.html', views.color_page_002, name='color_002'),
    path('color-pages/color-page-004.html', views.color_page_004, name='color_004'),
    path('color-pages/color-page-008.html', views.color_page_008, name='color_008'),
    path('color-pages/color-page-010.html', views.color_page_010, name='color_010'),
]