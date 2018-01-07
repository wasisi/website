from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .apps import AccountappConfig



def log_in(request):
    """
    Serves the log in view for a user
    :param request: request: the request that initiated this action
    :param template: template: the template that used for the rendering
    :return:
    """

    page_data={"page_title":AccountappConfig.index_page_name}

    if request.method == 'POST':
        return HttpResponseRedirect('../profile/')
    #    form = LoginForm(request.POST)
    #    if form.is_valid():
    #        cd = form.cleaned_data
    #        user = authenticate(username=cd['username'],password=cd['password'])
    #        if user is not None:
    #            if user.is_active:
    #                login(request, user)
                     #return HttpResponseRedirect('../profile/')
     #
     #           else:
     #               return HttpResponse('This account is disabled.')
     #       else:
     #           messages.error(request, "Your username or password did not match. Please try again.")
     #           error_data = get_errors_map_list(form)
     #           page_data.update(error_data)

      #          return render(request,template,page_data)
        #else:
    return render(request, AccountappConfig.login_view_tmpl , page_data)

@login_required
def user_profile(request):
    page_data={"page_title":AccountappConfig.account_page_name}
    return render(request,AccountappConfig.profile_view_tmpl,page_data)
