from django.shortcuts import render,HttpResponse
import requests
import threading
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.gzip import gzip_page 
""" explore this decorator """
from django.views.decorators.http import require_http_methods
# Create your views here.
@require_http_methods(["POST"]) 
# Oops Get request is not allowed so this view function can't be viewed 
def test(request):
    return HttpResponse("Not Allowed get Request here")
def make_api_request(url, all_data):
    response = requests.get(url)
    data = response.json()
    if data:
        all_data.append(data)


@cache_page(60*15) # this makes a big difference brother without this it taking upto 30 secs to load the api after that the time is reduced try unapply this
def market(request):
    try:
        state_filter='Rajasthan'
        district_filter='Jaipur'
        limit=1
        if request.method=='POST':
            state_filter=request.POST['state']
            district_filter=request.POST['district']
        all_data=[]
        api_urls=[f"https://api.data.gov.in/resource/e3f56f8b-d881-4850-b1fd-ee14480fce8e?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f"https://api.data.gov.in/resource/c94a4a82-b0cf-435a-ba4b-a6d8ee26b0c8?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f"https://api.data.gov.in/resource/78329234-2d42-4f71-867c-a376a3b10c45?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f"https://api.data.gov.in/resource/d2d6f030-b49b-417a-897a-5a0e41eb3fdd?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f"https://api.data.gov.in/resource/9442098e-9c72-4e41-bdd1-0ac3be157c07?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f"https://api.data.gov.in/resource/641dd73b-1c8e-4ddf-a8d2-a53741b34a2c?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f"https://api.data.gov.in/resource/61792629-e13b-46f0-850f-727c1f148a82?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f"https://api.data.gov.in/resource/73cd6b13-f480-436a-9347-9f81a2845909?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f"https://api.data.gov.in/resource/2191b45a-3a28-4f72-9942-dbc1cc7a91b5?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f"https://api.data.gov.in/resource/4e0dd1cf-98ac-4e78-9024-8e93f9737f56?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f"https://api.data.gov.in/resource/51c5b28a-d27b-4529-bdf8-007f67e9f347?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}",
        f'https://api.data.gov.in/resource/a2118264-db52-4cfd-b04f-6ce8b0f146a3?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/03db0d1e-39a4-46c7-9de8-77ad0c853475?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/7cb6ad9c-f8a9-4ce3-8db8-dc5b1a70de3a?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/766ddd21-e10c-4048-9289-1b4ec1ac058b?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/264eb10d-53c6-434c-afb2-d70ede0fb364?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/e863c509-81a9-4b55-aae3-685a01324b1c?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/a61861b2-fe5b-47ed-b373-930af0c0eb73?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/fb208485-bbdb-45c7-9a38-aefbfd4c596e?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/c7ae43c6-920d-483c-9f8e-974ac2d49c72?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/a7856635-c351-4b20-8333-1c826da5249c?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/8f618ca8-7c10-48f4-83b2-43e711d32109?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/1266b30e-ced4-4847-a504-c1cddfb0b85d?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/cf7c3c0e-7c5f-4d89-85dd-aaf5fa20e6ec?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}',
        f'https://api.data.gov.in/resource/8a11f00c-09ca-44eb-aea2-93961a548194?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit={limit}&filters%5B_state_%5D={state_filter}&filters%5Bdistrict%5D={district_filter}']
        
        threads = [threading.Thread(target=make_api_request, args=(url, all_data)) for url in api_urls]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        return JsonResponse(all_data,safe=False)
    except Exception as e:
        print(f"An error occurred: {e}")
        return HttpResponse("An error occurred while processing your request.")