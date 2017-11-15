# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.views.generic import View
from .models import Produce
from Users.models import UsersProfile
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class ProductListView(View):
    """
    产品列表
    """
    def get(self, request):
        all_products = Produce.objects.all()
        all_users = UsersProfile.objects.all()
        hot_products = all_products.order_by('click_nums')[:3]
        #对产品进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1



        p = Paginator(all_products, 6, request=request)

        products = p.page(page)

        return render(request,"course-list.html", {
            "all_products":products,
            "all_users":all_users,
            "hot_products":hot_products,
        })

class ProductDetailView(View):
    def get(self, request, product_id):

        produce = Produce.objects.get(id=int(product_id))

        return render(request, "course-detail.html", {
                "produce":produce,

        })