from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('', views.analysis_view, name='analysis_page'),  # Corresponds to /analysis/
    path('run-benchmark/', views.run_benchmark_view, name='run_benchmark'), # Corresponds to /analysis/run-benchmark/
]