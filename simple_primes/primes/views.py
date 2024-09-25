from django.shortcuts import render

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def input_page(request):
    return render(request, 'input_page.html')

def primes_output(request):
    if request.method == 'POST':
        number = int(request.POST.get('number'))
        primes_list = [i for i in range(2, number + 1) if is_prime(i)]
        return render(request, 'output_page.html', {'primes': primes_list, 'number': number})
    return render(request, 'input_page.html')

