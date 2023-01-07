from django.shortcuts import render,redirect,HttpResponse
def login_req(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        name=request.session.get('user_dt')
        if name is None:
           return redirect('service_provider_login')

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware