from django.shortcuts import render


def main_page(request):
    context = {
        # content later
    }
    return render(request, 'landing/main.html', context=context)


def apartment_page(request):
    context = {
        # content later
    }
    return render(request, 'landing/apartment.html', context=context)
