from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from . import views

# Tic-Tac-Toe app urls
urlpatterns = patterns('',
    # url(r'^$', views.index, name='index'), # TODO: change back when there are more games
    url(r'^$', views.normal_game, name='index'),
    url(r'^game/normal$', views.normal_game, name='normal_game'),
    #TODO: url(r'^game/ajax$', TemplateView.as_view(template_name='tictactoe/game/ajax.html'), name='ajax_game'),
    #TODO: url(r'^game/angular$', TemplateView.as_view(template_name='tictactoe/game/angular.html'), name='angular_game'),
)

