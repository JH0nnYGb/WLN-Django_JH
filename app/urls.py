from django.urls import path
from . import views
from usuarios.views import GerenciarConta
from django.urls import reverse

urlpatterns = [
    path('home/', views.home, name='home'),
    path('receitas/', views.Receitas, name='receitas'),
    path('criandoreceita/', views.CriandoReceita, name='criando-receita'),

    path('criandoreceita/getValoresIngrediente/<str:nome>/', views.getValoresIngredientes, name='get-valores-ingrediente'),
    path('criandoreceita/getAlergenicos/', views.GetAlergenicos, name='get-alergenicos'),  
    path('criandoreceita/getBaseIngredientes/', views.getBaseIngredientes, name='get-base-ingredientes'),
    
    path('criandoreceita/getMeusIngredientes/', views.GetMeusIngredientes, name='get-meus-ingredientes'),
    path('meusingredientes/', views.userIngredientes, name='meus-ingredientes'),
    path('criaringrediente/', views.CriarIngrediente , name='criar-ingrediente'),

    path('meusingredientes/editaringrediente/<int:Ingrediente_id>/', views.editar_ingrediente, name='editar-ingrediente'),

    path('contatenos/', views.ContateNos, name='contate-nos'),
    path('minhaconta/', views.MinhaConta, name='minha-conta'),
    
    path('gerenciarconta/', GerenciarConta, name='gerenciar-conta'), #import do app usuarios

    path('admin/app/alergenico/add/', views.CriarAlergenico),
]

