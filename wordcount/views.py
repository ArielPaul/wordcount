from django.http import HttpResponse

from django.shortcuts import render

import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['enteredtext']

    wordlist = fulltext.split()

    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            # Increase the COUNT
            word_dictionary[word] += 1
        else:
            # add to the word_dictionary
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sorted_words':sorted_words})
# The below line also works to pass the complete dictionary
#    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'word_dictionary':word_dictionary})


def bookhome(request):
    return render(request, 'adbook.html')

def book(request):
    FullName = request.GET['fname'] + " " + request.GET['lname'] + " " + request.GET['address']
    return render(request, 'adproc.html', { 'FullName':FullName})

def About(request):
    return render(request, 'About.html')
