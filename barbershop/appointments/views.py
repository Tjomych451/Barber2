from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Master, Service
from .forms import VisitForm
from django.core.signals import request_finished
from django.dispatch import receiver
import telegram
import os
from dotenv import load_dotenv

load_dotenv()

def index(request):
    masters = Master.objects.all()
    form = VisitForm()
    return render(request, 'appointments/index.html', {
        'masters': masters,
        'form': form
    })

def thank_you(request):
    return render(request, 'appointments/thank_you.html')

def get_services(request, master_id):
    services = Service.objects.filter(master__id=master_id)
    return JsonResponse({
        'services': list(services.values('id', 'name', 'price'))
    })

@receiver(request_finished)
def notify_telegram(sender, **kwargs):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('ADMIN_CHAT_ID')
    
    bot = telegram.Bot(token=bot_token)
    bot.send_message(
        chat_id=chat_id,
        text=f"New appointment received!\nClient: {kwargs.get('name')}\nPhone: {kwargs.get('phone')}"
    )
