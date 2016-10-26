__author__ = 'Will'

import pandas
import urllib.parse
import requests
from bs4 import BeautifulSoup


def zillow_hood_lookup(address):
    # returns a dictionary containing address and neighborhood

    # encode the address to make it URL friendly for the Zillow API
    encoded_address = urllib.parse.quote(address)
    print(encoded_address)

    # lookup
    response = requests.get('http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=X1-ZWz1ffkz4wphjf_3fm17&address='+encoded_address+'&citystatezip=Washington%2C%20DC')

    # parse - example: <region id="121779" name="Riggs Park" type="neighborhood">
    response_bsObj = BeautifulSoup(response.text, "html.parser")
    hood = {}
    hood[address] = response_bsObj.find(name='region', attrs={'type':'neighborhood'})['name']
    return hood


def great_schools_nearby(address, radius, limit):
    # Uses the nearby schools API http://www.greatschools.org/api/docs/nearbySchools.page
    # Returns a list of dictionaries, each dictionary being a nearby school for the given address


    # encode the address to make it URL friendly for the API
    encoded_address = urllib.parse.quote(address)

    # lookup nearby schools
    response = requests.get('http://api.greatschools.org/schools/nearby?key=zwobdwe32swx4uvowdyldaxx&address='+encoded_address+'&city=Washington%2C%20DC&schoolType=public-charter&levelCode=elementary-schools&radius='+radius+'&limit='+limit)

    # parse
    response_bsObj = BeautifulSoup(response.text, "html.parser")
    schools = response_bsObj.findAll(name='school')

    nearby_schools = []
    for s in schools:
        s_dic = {}
        s_dic['address'] = address
        s_dic['gsId'] = s.find(name='gsId').get_text()
        s_dic['name'] = s.find(name='name').get_text()
        s_dic['s_type'] = s.find(name='type').get_text()
        s_dic['grade_range'] = s.find(name='gradeRange').get_text()
        s_dic['enrollment'] = s.find(name='enrollment').get_text()
        s_dic['city'] = s.find(name='city').get_text()
        s_dic['state'] = s.find(name='state').get_text()
        s_dic['address'] = s.find(name='address').get_text()
        s_dic['lat'] = s.find(name='lat').get_text()
        s_dic['lon'] = s.find(name='lon').get_text()
        s_dic['distance'] = s.find(name='distance').get_text()
        nearby_schools.append(s_dic)

    return nearby_schools
    

def great_schools_tests(gsId, state):
    # Uses the tests API http://www.greatschools.org/api/docs/schoolTestScores.page
    # Returns a tuple of two lists, each containing dictionaries for tests/rankings for the given school

    # encode the address to make it URL friendly for the API

    # lookup school
    response = requests.get('http://api.greatschools.org/school/tests/'+state+'/1?key=zwobdwe32swx4uvowdyldaxx')

    # parse
    response_bsObj = BeautifulSoup(response.text, "html.parser")
    tests = response_bsObj.findAll(name='test')
    rankings = response_bsObj.findAll(name='ranking')
    school_tests = []
    for t in tests:
        test_data={}
        test_data['gsId'] = gsId
        test_data['name'] = t.find(name='name').get_text()
        test_data['id'] = t.find(name='id').get_text()
        test_data['abbreviation'] = t.find(name='abbreviation').get_text()
        test_data['scale'] = t.find(name='scale').get_text()
        test_data['levelCode'] = t.find(name='levelCode').get_text()
        test_data['scale'] = t.find(name='scale').get_text()
        results = tests.findAll(name='testResult')
        for r in results:
            test_data[grade] = result.find(name='gradeName').get_text()
            test_data[score] = result.find(name='score').get_text()
            test_data[subjectName] = result.find(name='subjectName').get_text()
            test_data[testId] = result.find(name='testId').get_text()
            test_data[year] = result.find(name='year').get_text()
            school_tests.append(test_data)

    school_rankings = []
    for r in rankings:
        rank_data={}
        rank_data['name'] = rankings.find(name='name').get_text()
        rank_data['scale'] = rankings.find(name='scale').get_text()
        rank_data['year'] = rankings.find(name='year').get_text()
        rank_data['description'] = rankings.find(name='description').get_text()
        rank_data['score'] = rankings.find(name='score').get_text()
        school_rankings.append(rank_data)

    return([school_tests, school_rankings])
