from django.db import models
from libs.ionic_radii_functions import get_ionic_radii
from django.contrib.postgres.fields import ArrayField
import more_itertools

#import json

#ions=get_ionic_radii(r"C:\Users\juhL-laptop\Dropbox\web\radii\extend_sp_radii\src\add_radii\radii_updated_win.dat")
ions=get_ionic_radii(r"C:\Users\juhL-laptop\Dropbox\web\radii\extend_sp_radii\src\add_radii\radii_updated.dat")

# Create your models here.

class db_ions(models.Model):
	label=models.CharField(max_length=5)

	ox=ArrayField(models.IntegerField(null=True, blank=True))
	cn=ArrayField(ArrayField(models.FloatField(),size=20),size=20)
	r_ir=ArrayField(ArrayField(models.FloatField(),size=20),size=20)
	errors=ArrayField(ArrayField(models.CharField(max_length=255),size=20),size=20)


	def __str__(self):
		return str(self.label)


for i in ions:
	print('here',ions[i].label)
	#this fucks shit up when initializing the database for the first time (e.g. after killing it for some errors), uncomment and use only the else block in those cases. also, find way of checking this ... 
	if db_ions.objects.filter(label = ions[i].label).exists():
		print('old element')
		add=db_ions.objects.get(label = ions[i].label)
	else:
		print('new element')
		add=db_ions(label=ions[i].label)

#	for j in ions[i].ox:
#		ox_idx=ions[i].ox.index(j)
	print('adding ox:', ions[i].ox)
	add.ox=ions[i].ox

	ions[i].cn=list(more_itertools.padded(ions[i].cn,[],20))
	print(ions[i].cn)
	for j in range(20):
		ions[i].cn[j]=list(more_itertools.padded(ions[i].cn[j],None,20))
		
	print('adding cn:', ions[i].cn)
	add.cn=ions[i].cn

	ions[i].r_ir=list(more_itertools.padded(ions[i].r_ir,[],20))
	print(ions[i].r_ir)
	for j in range(20):
		ions[i].r_ir[j]=list(more_itertools.padded(ions[i].r_ir[j],None,20))
		
	print('adding r_ir:', ions[i].r_ir)
	add.r_ir=ions[i].r_ir

	ions[i].errors=list(more_itertools.padded(ions[i].errors,[],20))
	print(ions[i].errors)
	for j in range(20):
		ions[i].errors[j]=list(more_itertools.padded(ions[i].errors[j],None,20))
		
	print('adding errors:', ions[i].errors)
	add.errors=ions[i].errors
	#add=db_ions(ox = json.dumps(ions[i].ox))
#	print(json.dumps(ions[i].ox))
	print('added this ')
	print(add.label)
	print(add.cn)
	print(add.r_ir)
	print(add.errors)
	add.save()
