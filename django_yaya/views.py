from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from .models import YayaWallet
import hmac
import hashlib


# Create your views here.
@csrf_exempt
def yaya_webhook(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            signature = request.headers.get('YAYA-SIGNATURE')
            yaya_secret = settings.YAYA_SECRET_KEY

            # verifying signature
            data = "".join(str(value) for value in payload.values())
            signed_payload = data.encode('utf-8')
            expected_signature = hmac.new(yaya_secret.encode(
                "utf-8"), signed_payload, hashlib.sha256).hexdigest()

            if signature == expected_signature:
                YayaWallet.objects.create(**payload)
                return JsonResponse(data, {"status": 200})
        except json.decoder.JSONDecodeError:
            return JsonResponse({'error': "Invalid Json Body"}, status=400)
        except YayaWallet.DoesNotExist:
            return JsonResponse({'error': 'Object does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"})
