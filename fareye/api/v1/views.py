from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from rest_framework.views import APIView
from got.models import Battles,King
from django.http import Http404
from django.conf import settings

def CalculateEloRating(battle,attacker,defender):
    n = 400 #given
    k = 32 #k-factor given
    R1 = 10**(attacker.rating/400)
    R2 = 10**(defender.rating/400)
    E1 = R1/(R1+R2)
    E2 = R2/(R1+R2)
    r1 = attacker.rating
    r2 = defender.rating
    S1 = 1 if battle.attacker_outcome == 'win' else 0 if battle.attacker_outcome == 'loss' else 0.5
    S2 = 1 if battle.attacker_outcome == 'loss' else 0 if battle.attacker_outcome == 'win' else 0.5
    r1new = r1 + k*(S1-E1)
    r2new = r2 + k*(S2-E2)
    return [r1new,r2new]
class KingsListView(APIView):

    def get(self, request, *args, **kwargs):
        """Return results list."""
        try:
            minlisting = 0
            maxlisting = settings.LISTING_ON_PAGE
            if request.GET.get('page'):
                minlisting = maxlisting * (int(request.GET.get('page')))
                maxlisting = maxlisting + maxlisting * (int(request.GET.get('page')))

            kinglist = King.objects.all().order_by('-rating')[minlisting:maxlisting]
        except Exception as e:
            raise Http404
        # First time calculate rating using this
        # for b in Battles.objects.all():
        #     try:
        #         attacker = King.objects.get(name=b.attacker_king)
        #         defender = King.objects.get(name=b.defender_king)
        #         newrating = CalculateEloRating(b,attacker,defender)
        #         attacker.rating = newrating[0]
        #         defender.rating = newrating[1]
        #         attacker.save()
        #         defender.save()
        #     except:
        #         pass

        kingdetails = []
        for king in kinglist:
            d = {
                'name':king.name,
                'slug':king.slug,
                'rating':king.rating,
            }
            kingdetails.append(d)
        data = {
            'kings': kingdetails,
        }
        return Response(data)
