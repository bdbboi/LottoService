from django.db import models

class LottoTicket(models.Model):
    CHOICES = [
        ('manual', '수동'),
        ('auto', '자동'),
    ]
    purchase_type = models.CharField(max_length=10, choices=CHOICES)
    numbers = models.JSONField(blank=True, null=True)  # 로또 번호 저장 (수동 입력)
    user_name = models.CharField(max_length=100, default='unknown')  # 사용자 이름
    created_at = models.DateTimeField(auto_now_add=True)
    is_winner = models.BooleanField(default=False)  # 당첨 여부

    def __str__(self):
        return f"Ticket {self.id} ({self.purchase_type})"

class WinningNumbers(models.Model):
    numbers = models.JSONField()  # 당첨 번호 저장
    draw_date = models.DateField(auto_now_add=True)  # 추첨 날짜

    def __str__(self):
        return f"Winning Numbers ({self.draw_date}): {self.numbers}"
    