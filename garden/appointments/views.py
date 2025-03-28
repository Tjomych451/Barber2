from django.shortcuts import render, redirect
from .models import Master, Service, Visit
from .forms import VisitForm
from django.http import JsonResponse
from .models import Master, Service
from .forms import VisitForm
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Visit
import telegram
import os
from dotenv import load_dotenv
import asyncio
from telegram import Bot



load_dotenv()

def index(request):
    masters = Master.objects.all()
    form = VisitForm()
    return render(request, 'appointments/index.html', {
        'masters': masters,
        'form': form
    })

def thank_you(request):
    """
    Отображает страницу благодарности после успешной отправки заявки
    """
    return render(request, 'appointments/thank_you.html')

def get_services(request, master_id):
    services = Service.objects.filter(master__id=master_id)
    return JsonResponse({
        'services': list(services.values('id', 'name', 'price'))
    })

@receiver(request_finished)
# async def send_telegram_message(token, chat_id, text):
#     bot = Bot(token=token)
#     await bot.send_message(chat_id=chat_id, text=text)

# def notify_telegram(sender, **kwargs):
#     bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
#     chat_id = os.getenv('ADMIN_CHAT_ID')
#     text = f"New appointment received!\nClient: {kwargs.get('name')}\nPhone: {kwargs.get('phone')}"
    
#     try:
#         asyncio.run(send_telegram_message(bot_token, chat_id, text))
#         print("Message sent successfully!")
#     except Exception as e:
#         print(f"Error sending message: {e}")
def notify_telegram(sender, **kwargs):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('ADMIN_CHAT_ID')
    
    print(f"Attempting to send message with token: {bot_token[:5]}... to chat_id: {chat_id}")
    
    try:
        bot = telegram.Bot(token=bot_token)
        bot.send_message(
            chat_id=chat_id,
            text=f"New appointment received!\nClient: {kwargs.get('name')}\nPhone: {kwargs.get('phone')}"
        )
        print("Сообщение о новой заявки успешно отправлено!")
    except Exception as e:
        print(f"Error sending message: {e}")

@receiver(post_save, sender=Visit)
def notify_telegram_on_visit(sender, instance, created, **kwargs):
    if created:
        from .views import notify_telegram
        notify_telegram(sender, name=instance.name, phone=instance.phone)