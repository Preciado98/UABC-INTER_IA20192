# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 09:38:35 2019

@author: preci
"""

from FuzzySystem.FuzzySet import  FuzzySet
from FuzzySystem.FuzzyVariable import  FuzzyVariable
from FuzzySystem.FuzzyInferenceSystem import  FuzzyInferenceSystem, Antecedent,Consequent, FuzzyRule 
from FuzzySystem.Defuzzifier import Centroid
from FuzzySystem.MembershipFunction import Trimf, Gaussmf, GBellmf, Logmf, Tanhmf, Trapmf, Sigmoidmf, Cauchymf

#INPUTS

service_poor = FuzzySet('poor', Gaussmf([1.5, 0]))
service_good = FuzzySet('good', Gaussmf([1.5, 5]))
service_excellent = FuzzySet('excellent', Gaussmf([1.5, 10]))
#service_excellent.show()
service = FuzzyVariable('service',[service_poor, service_good, service_excellent], universe=[0, 10])
#service.show()

food_rancid = FuzzySet('rancid', Trapmf([0,0,1,3]))
food_delicious = FuzzySet('delicious', Trapmf([7,9,10,10]))
food = FuzzyVariable('food', [food_rancid, food_delicious], universe=[0, 10])
#food.show()

#OUTPUT

tip_cheap = FuzzySet('cheap', Trimf([0,5,10]))
tip_avg = FuzzySet('average', Trimf([10,15,20]))
tip_generous = FuzzySet('generous', Trimf([20,25,30]))
tip = FuzzyVariable('tip', [tip_cheap, tip_avg, tip_generous], universe=[0, 30])
tip.show()

#RULES


#ant1  = Antecedent(service['poor'], conector=max)
#ant1.add(food['rancid'])
ant1  = Antecedent(service['poor'] | food['rancid'])
cont1 = Consequent([tip['cheap']])
rule1 = FuzzyRule(ant1, cont1)

ant2  = Antecedent(service['good'] | food['delicious'])
cont2 = Consequent([tip['average']])
rule2 = FuzzyRule(ant2, cont2)


#ant3  = Antecedent(service['excellent'], conector=min)
#ant3.add(food['delicious'])
#cont3 = Consequent([tip['generous']])


rule3 = FuzzyRule(Antecedent(service['excellent'] & food['delicious']), 
                  Consequent([tip['generous']]))

#Building the FIS

fis = FuzzyInferenceSystem([rule1, rule2, rule3], and_op='prod', or_op='sum')

#FIS Evaluation

inputs = {'service':8.183, 'food':8.59}
result = fis.eval(inputs)