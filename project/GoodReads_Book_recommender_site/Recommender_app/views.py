# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from GoodReads_Book_recommender_site import settings
from django.template.loader import render_to_string
from models import ImageUpload
from .models import UserRating
import graphlab
import pickle
import csv
import pandas as pd
# Create your views here.
def index(request):
	print("hello")
	image_data=image_uploaded()
	context={}
	context['images_data']=image_data
	print(".........................done")
	return render(request, "index.html", context)

#To load images to get rated
def image_uploaded():
	print("images uploading")
	image_dict= ImageUpload.objects.all().order_by('?').values('book_id','book_title','image_url')[:100]
	return image_dict


def recommend(request):
	if request.method=="POST":
		UserRating.objects.all().delete()
		for i in range(0,100):
			rating=request.POST.get('rating'+str(i)+'')
			if(rating!=None):
				print(request.POST.get('rating'+str(i)+''),"....",request.POST.get('book'+str(i)+''))
				userratingmodel=UserRating()
				userratingmodel.rating=(request.POST.get('rating'+str(i)+''))
				userratingmodel.book_id=(request.POST.get('book'+str(i)+''))
				userratingmodel.save()
		print("done saving ..........")	
	return render(request, "recommend.html", locals())

def collaborative(request):
	print("collla.................")
	Collaborative=graphlab.load_model('C:/Users/SONY/Desktop/3rdsem/Machine Learning/project/Models/Collaborative')
	books_rated=UserRating.objects.all().values('book_id','user_id','rating')
	print(books_rated)
	df = pd.DataFrame(list(books_rated))
	print(df)
	test_data= graphlab.SFrame(df)
	print(Collaborative.predict(test_data))
	#Collaborative.predict(test_data)
	r = Collaborative.recommend(users=['1'])
	r.print_rows(num_rows=10)
	print("done collab.............")
	return render(request, "show.html")


def content(request):
	print("collla.................")
	Context_based=graphlab.load_model('C:/Users/SONY/Desktop/3rdsem/Machine Learning/project/Models/Content based')
	books_rated=UserRating.objects.all().values('book_id','user_id','rating')
	print(books_rated)
	df = pd.DataFrame(list(books_rated))
	print(df)
	test_data= graphlab.SFrame(df)
	Context_based.predict(test_data)
	r = Context_based.recommend(users=['1'],k=100)
	r.print_rows(num_rows=100)
	print("done collab.............")
	return render(request, "show.html")


def matrix(request):
	print("collla.................")
	Matrix_factorization=graphlab.load_model('C:/Users/SONY/Desktop/3rdsem/Machine Learning/project/Models/Matrix Facorization')
	books_rated=UserRating.objects.all().values('book_id','user_id','rating')
	print(books_rated)
	df = pd.DataFrame(list(books_rated))
	print(df)
	test_data= graphlab.SFrame(df)
	Matrix_factorization.predict(test_data)
	r = Matrix_factorization.recommend(users=['60000'])
	r.print_rows(num_rows=50)
	print("done collab.............")
	return render(request, "show.html")

def popularity(request):
	print("collla.................")
	popularity=graphlab.load_model('C:/Users/SONY/Desktop/3rdsem/Machine Learning/project/Models/Popularity')
	books_rated=UserRating.objects.all().values('book_id','user_id','rating')
	print(books_rated)
	df = pd.DataFrame(list(books_rated))
	print(df)
	test_data= graphlab.SFrame(df)
	popularity.predict(test_data)
	r = popularity.recommend(users=['60000'])
	r.print_rows(num_rows=10)
	print("done collab.............")
	book_ids=(r.select_columns([str('book_id')]))
	print(book_ids)
	#books_to_show=ImageUpload.objects.raw('SELECT * FROM ImageUpload WHERE id IN %s', params=[book_ids]).values('book_id','image_url','book_title')
	books_to_show=ImageUpload.objects.filter(book_id__in=book_ids).values('book_id','image_url','book_title' )
	print(books_to_show)
	print("ddddddddddddddddddddddd")
	return render(request, "show.html")


#def to_show_recommended_books(r):


