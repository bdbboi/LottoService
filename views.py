import random
from django.shortcuts import render, redirect
from .models import LottoTicket, WinningNumbers
from django.contrib.auth.decorators import user_passes_test

def generate_random_numbers():
    return sorted(random.sample(range(1, 46), 6))  

def buy_lotto(request):
    if request.method == "POST":
        purchase_type = request.POST.get('purchase_type')
        
        if purchase_type == 'manual':
            numbers = request.POST.getlist('numbers[]')  # 사용자가 입력한 번호
            try:
                numbers = list(map(int, numbers))  
                if len(numbers) != 6 or not all(1 <= num <= 45 for num in numbers):
                    raise ValueError("Invalid numbers")
            except ValueError:
                return render(request, 'lotto/buy_lotto.html', {
                    'error': '번호는 1~45 사이의 숫자 6개를 입력해야 합니다.'
                })
        else:  # 자동
            numbers = generate_random_numbers()

        # 저장
        ticket = LottoTicket.objects.create(
            purchase_type=purchase_type,
            numbers=numbers,
        )
        return redirect('lotto:confirmation', ticket_id=ticket.id)
    
    return render(request, 'lotto/buy_lotto.html')

def confirmation(request, ticket_id):
    try:
        ticket = LottoTicket.objects.get(id=ticket_id)  # ticket_id로 LottoTicket 조회
    except LottoTicket.DoesNotExist:
        ticket = None  
    return render(request, 'lotto/confirmation.html', {'ticket': ticket})

def is_admin(user):
    return user.is_superuser  # 관리자 권한 확인

@user_passes_test(is_admin)  # 관리자만 접근 가능
def draw_winning_numbers(request):
    if request.method == "POST":
        numbers = sorted(random.sample(range(1, 46), 6))  
        WinningNumbers.objects.create(numbers=numbers)
        return redirect('lotto:winning_numbers')  # 추첨 결과 페이지로 리다이렉트

    return render(request, 'lotto/draw_winning_numbers.html')

def winning_numbers(request):
    winning_numbers = WinningNumbers.objects.order_by('-draw_date')  # 최신 순으로 정렬
    return render(request, 'lotto/winning_numbers.html', {'winning_numbers': winning_numbers})

def home(request):
    return render(request, 'lotto/home.html')

def lotto_sales(request):
    tickets = LottoTicket.objects.all()  
    return render(request, 'lotto/lotto_sales.html', {'tickets': tickets})

def winning_statistics(request):
    winning_numbers = WinningNumbers.objects.all() 
    tickets = LottoTicket.objects.all()   

    statistics = []
    for winning in winning_numbers:
        winning_ticket = tickets.filter(numbers=winning.numbers)
        statistics.append({
            'winning_numbers': winning.numbers,
            'count': winning_ticket.count(),
        })

    return render(request, 'lotto/winning_statistics.html', {'statistics': statistics})
