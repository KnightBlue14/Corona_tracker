import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests

url_cases= 'https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=cumCasesByPublishDate&format=csv'
url_deaths='https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=cumDeaths28DaysByPublishDate&format=csv'
url_first='https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=cumPeopleVaccinatedFirstDoseByPublishDate&format=csv'
url_second='https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=cumPeopleVaccinatedSecondDoseByPublishDate&format=csv'
url_beds='https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=covidOccupiedMVBeds&format=csv'
url_hospital='https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=hospitalCases&format=csv'

r_cases = requests.get(url_cases, allow_redirects=True)
open('CumCases.csv', 'wb').write(r_cases.content)
r_deaths = requests.get(url_deaths, allow_redirects=True)
open('CumDeaths.csv', 'wb').write(r_deaths.content)
r_first = requests.get(url_first, allow_redirects=True)
open('CumFirst.csv', 'wb').write(r_first.content)
r_second = requests.get(url_second, allow_redirects=True)
open('CumSecond.csv', 'wb').write(r_second.content)
r_beds = requests.get(url_beds, allow_redirects=True)
open('Beds.csv', 'wb').write(r_beds.content)
r_hospital = requests.get(url_hospital, allow_redirects=True)
open('Hospital.csv', 'wb').write(r_hospital.content)

df = pd.read_csv('CumCases.csv')
cases=df['cumCasesByPublishDate']
cases=cases.reindex(index=cases.index[::-1])
grad_cases=np.gradient(cases)

df = pd.read_csv('CumDeaths.csv')
deaths=df['cumDeaths28DaysByPublishDate']
deaths=deaths.reindex(index=deaths.index[::-1])
grad_deaths=np.gradient(deaths)


fig, axs = plt.subplots(2,1,sharex=True)
fig.suptitle('Covid-19 infections', fontsize=16)

days = list(range(len(cases)))
axs[0].plot(days, cases)
axs[0].set_title('Raw count')
axs[0].set_ylabel('Number of cases (Million)')
axs[1].plot(days, grad_cases)
axs[1].set_title('Rate of infection')
axs[1].set_ylabel('Rate')
axs[1].set_xlabel('Days after lockdown began')
plt.show()

fig, axs = plt.subplots(2,1,sharex=True)
fig.suptitle('Covid-19 deaths', fontsize=16)

days = list(range(len(deaths)))
axs[0].plot(days, deaths)
axs[0].set_title('Raw count')
axs[0].set_ylabel('Number of deaths')
axs[1].plot(days, grad_deaths)
axs[1].set_title('Rate of deaths')
axs[1].set_ylabel('Rate')
axs[1].set_xlabel('Days after lockdown began')
plt.show()

df = pd.read_csv('Hospital.csv')
beds=df['hospitalCases']
beds=beds.reindex(index=beds.index[::-1])
grad_beds=np.gradient(beds)

fig, axs = plt.subplots(2,1,sharex=True)
fig.suptitle('Covid-19 Hospitalisations', fontsize=16)

days = list(range(len(beds)))
axs[0].plot(days, beds)
axs[0].set_title('Number of hospitalisations')
axs[0].set_ylabel('Beds')
axs[1].plot(days, grad_beds)
axs[1].set_title('Rate of use')
axs[1].set_ylabel('Rate')
axs[1].set_xlabel('Days after lockdown began')
plt.show()

df = pd.read_csv('Beds.csv')
beds=df['covidOccupiedMVBeds']
beds=beds.reindex(index=beds.index[::-1])
grad_beds=np.gradient(beds)

fig, axs = plt.subplots(2,1,sharex=True)
fig.suptitle('Covid-19 MV Beds', fontsize=16)

days = list(range(len(beds)))
axs[0].plot(days, beds)
axs[0].set_title('Raw count')
axs[0].set_ylabel('Number of Ventilators')
axs[1].plot(days, grad_beds)
axs[1].set_title('Rate of use')
axs[1].set_ylabel('Rate')
axs[1].set_xlabel('Days after lockdown began')
plt.show()

df = pd.read_csv('CumFirst.csv')
df2 = pd.read_csv('CumSecond.csv')
f=df['cumPeopleVaccinatedFirstDoseByPublishDate']
s=df2['cumPeopleVaccinatedSecondDoseByPublishDate']
F=f.reindex(index=f.index[::-1])
S=s.reindex(index=s.index[::-1])
grad_Rmax=np.gradient(F)
grad_Rmin=np.gradient(S)

fig, axs = plt.subplots(2,1,sharex=True)
fig.suptitle('Vaccinations', fontsize=16)

days = list(range(len(F)))
axs[0].plot(days, F,label='First Dose')
axs[0].plot(days, S,label='Second Dose')
axs[0].legend()
axs[1].plot(days, grad_Rmax)
axs[1].plot(days, grad_Rmin)
plt.show()

ratio=deaths/cases
av_ratio=np.gradient(ratio)
fig, axs = plt.subplots(2,1,sharex=True)
fig.suptitle('Mortality', fontsize=16)

days = list(range(len(ratio)))
axs[0].plot(days, ratio)
axs[1].plot(days, av_ratio)
plt.show()
