


def index(request):
    products = Product.objects.all
    return render(request, 'store/index.html.html', context={"products": products})

