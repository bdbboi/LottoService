from django.urls import path
from . import views

app_name = 'lotto'

urlpatterns = [
    path('', views.home, name='home'),  # 기본 페이지 경로
    path('buy/', views.buy_lotto, name='buy_lotto'),
    path('confirmation/<int:ticket_id>/', views.confirmation, name='confirmation'),  # confirmation URL 추가
    path('draw/', views.draw_winning_numbers, name='draw_winning_numbers'),
    path('winning-numbers/', views.winning_numbers, name='winning_numbers'),  # 당첨 결과 페이지
    path('sales/', views.lotto_sales, name='lotto_sales'),  # 로또 판매 통계 페이지
    path('winning-statistics/', views.winning_statistics, name='winning_statistics'),  # 당첨자 통계 페이지
]
