from django.urls import path, include
from blog import views
from django.views.generic.base import RedirectView


app_name = "blog"

urlpatterns = [
    path("cbv-index", views.IndexView.as_view(), name="cbv-index"),
    # path(
    #     "go-to-django/",
    #     RedirectView.as_view(url="https://www.djangoproject.com/"),
    #     name="go-to-django",
    # ),
    path(
        "go-to-index/",
        RedirectView.as_view(pattern_name="blog:index"),
        name="redirect-to-index",
    ),
    path(
        "go-to-maktabkhooneh/",
        views.RedirectToMaktab.as_view(),
        name="redirect-to-maktabkhooneh",
    ),
    # for PostList url must like this with '/' at the end
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    # for FormView
    # path('post/create/', views.PostCreateView.as_view(), name="post-create"),
    # for CreateView
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("api/v1/", include("blog.api.v1.urls")),
]
