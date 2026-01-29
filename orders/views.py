from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import OrderForm
from django.core.mail import send_mail
from .models import Order
from django.conf import settings


def order_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order: Order = form.save()

            # Send confirmation email
            messge_client = render_to_string(
                "orders/email/confirmation.html", {"order": order}
            )
            send_mail(
                subject="дякуємо за ваше замовлення!",
                message="",
                from_email=settings.ADMIN_EMAIL,
                recipient_list=[order.email],
                html_message=messge_client,
            )

            # Send admin notification email
            message_admin = render_to_string(
                "orders/email/admin_notification.html", {"order": order}
            )
            send_mail(
                subject=f"Нове замовлення №{order.pk} від {order.name}",
                message="",
                from_email=settings.ADMIN_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                html_message=message_admin,
            )

            return redirect("order:success_view")

    form = OrderForm()
    return render(request, "orders/order_form.html", {"form": form})


def success_view(request):
    return render(request, "orders/success.html")
