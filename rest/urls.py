# from django.contrib import admin
from django.urls import path
from rest.views import *
urlpatterns = [
   # modelmixin url start from here----------------------------------
   path('', home, name= "home"),
#    path('stugetapi',GetPostAPI.as_view(), name=  "stugetapi"),
   path('studapi/<int:pk>', RUDAPI.as_view(), name="studapi"),


   # concrete api view start from here which extends Generic view and ModelMixin--------------
    path('studlist', StudList.as_view(), name='studlist'),
    path('student/', StudCreate.as_view(), name='student'),
    path('studretrive/<int:pk>', StudRetrive.as_view(), name='studretrive'),
    path('studupdate/<int:pk>', StudUpdate.as_view(), name='studupdate'),
    path('studdestory/<int:pk>', StudDestroy.as_view(), name='studdestroy'),


    # url for require pk and not mixed APIVIEW-------------------------
    path('studlistcreate', StudListCreate.as_view(), name='studlistcreate'),
    path('studrud/<int:pk>', StudRUD.as_view(), name='studrud'),

    # url using class method ------------------------------------------------------
    path('studapi ', StudAPI.as_view(), name= 'studapi'),
    path('studapi/<int:pk>', StudAPI.as_view(), name= 'studapi'),
    # path('studcreate', )
]