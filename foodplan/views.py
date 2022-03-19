from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from recipes.models import Subscription
from recipes.models import SubscriptionTimeInterval
from recipes.models import RestrictTag
from recipes.models import MealTag
from recipes.models import User

from .forms import SubsForm


def render_start_page(request):
    return render(request, 'index.html')


def render_reg_page(request):
    return render(request, 'registration.html')


def render_auth_page(request):
    return render(request, 'auth.html')


@login_required(login_url='/')
def render_lk_page(request):
    current_user = User.objects.get(id=request.user.id)
    user_subscriptions = current_user.subscriptions.all()
    print(user_subscriptions)
    
    user_subsciptions_data = []
    for user_subsciption in user_subscriptions:
        user_subsciption_data = {
            'id': user_subsciption.id,
            'title': user_subsciption.__str__(),
            'meals_amount': user_subsciption.meals.count(),
            'persons_amount': user_subsciption.persons_num,
            'features': [tag.tag for tag in user_subsciption.restrict_tags.all()]
        }
        user_subsciptions_data.append(user_subsciption_data)
        
    context = {
        "subscriptions": user_subsciptions_data
    }

    return render(request, 'lk.html', context=context)


@login_required(login_url='/')
def render_order_page(request):
    if request.method == "POST":
        current_user = User.objects.get(id=request.user.id)
        subs_interval, created = SubscriptionTimeInterval.objects.get_or_create (
            time_intervals=int(request.POST.getlist('subs_period')[0])
        )

        meals_titles = request.POST.getlist('meals')
        meals_titles = [title for title in meals_titles if title]
        
        if len(meals_titles) == 0: return redirect('/order')

        meals = []
        for meal_title in meals_titles:
            meal, created = MealTag.objects.get_or_create (
                meal=meal_title
            )
            meals.append(meal)

        user_subscription, created = Subscription.objects.get_or_create (
            user=current_user,
            period=subs_interval,
            persons_num=int(request.POST.getlist('person_amount')[0])
        )

        for meal in meals:
            user_subscription.meals.add(meal)

        features_titles = request.POST.getlist('features')

        if features_titles:
            features_titles = [feature_title for feature_title in features_titles if feature_title]

            for feature_title in features_titles:
                feature, created = RestrictTag.objects.get_or_create (
                    tag=feature_title
                )
                user_subscription.restrict_tags.add(feature)

        return redirect('/lk')

    else:
        subsform = SubsForm()

        context = {
            'form': subsform
        }

        return render(request, 'order.html', context)