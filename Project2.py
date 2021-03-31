from bs4 import BeautifulSoup
import requests
import re
import os
import csv
import unittest


def get_titles_from_search_results(filename):
    """
    Write a function that creates a BeautifulSoup object on "search_results.htm". Parse
    through the object and return a list of tuples containing book titles (as printed on the Goodreads website) 
    and authors in the format given below. Make sure to strip() any newlines from the book titles and author names.

    [('Book title 1', 'Author 1'), ('Book title 2', 'Author 2')...]
    """
    o = open(filename)
    r = o.read()
    soup = BeautifulSoup(r, 'html.parser')
    titles = soup.find_all('a', class_ = "bookTitle")
    new_titles = []
    for i in titles:
        new_titles.append(i.text.strip())

    authors = soup.find_all("a", class_="authorName")
    new_authors = []
    for i in authors:
        new_authors.append(i.text.strip())

    new = []
    for i in range(len(new_titles)):
        ap = (new_titles[i], new_authors[i])
        new.append(ap)
    return new
    
#print(get_titles_from_search_results("search_results.htm"))


def get_search_links():
    """
    Write a function that creates a BeautifulSoup object after retrieving content from
    "https://www.goodreads.com/search?q=fantasy&qid=NwUsLiA2Nc". Parse through the object and return a list of
    URLs for each of the first ten books in the search using the following format:

    ['https://www.goodreads.com/book/show/84136.Fantasy_Lover?from_search=true&from_srp=true&qid=NwUsLiA2Nc&rank=1', ...]

    Notice that you should ONLY add URLs that start with "https://www.goodreads.com/book/show/" to 
    your list, and , and be sure to append the full path to the URL so that the url is in the format 
    “https://www.goodreads.com/book/show/kdkd".

    """

    url = "https://www.goodreads.com/search?q=fantasy&qid=NwUsLiA2Nc"  
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    new = soup.find_all("a", class_="bookTitle")
    lst = []
    for i in new:
        lst.append("https://www.goodreads.com" + i['href'])
    
    return lst[:10]

#print(get_search_links())

def get_book_summary(book_url):
    """
    Write a function that creates a BeautifulSoup object that extracts book
    information from a book's webpage, given the URL of the book. Parse through
    the BeautifulSoup object, and capture the book title, book author, and number 
    of pages. This function should return a tuple in the following format:

    ('Some book title', 'the book's author', number of pages)

    HINT: Using BeautifulSoup's find() method may help you here.
    You can easily capture CSS selectors with your browser's inspector window.
    Make sure to strip() any newlines from the book title and number of pages.
    """

    resp = requests.get(book_url)
    soup = BeautifulSoup(resp.text, "html.parser")
    name = soup.find("h1", class_="gr-h1--serif")
    name_good = name.text.strip()
    pages = soup.find("span", itemprop = "numberOfPages")
    pages_good = pages.text.strip()
    author = soup.find("span", itemprop="name")
    author_good = author.text.strip()
    return (name_good, pages_good, author_good)

#print(get_book_summary('https://www.goodreads.com/book/show/6542645-fantasy-in-death?from_search=true&from_srp=true&qid=NwUsLiA2Nc&rank=2'))

def summarize_best_books(filepath):
    """
    Write a function to get a list of categories, book title and URLs from the "BEST BOOKS OF 2020"
    page in "best_books_2020.htm". This function should create a BeautifulSoup object from a 
    filepath and return a list of (category, book title, URL) tuples.
    
    For example, if the best book in category "Fiction" is "The Testaments (The Handmaid's Tale, #2)", with URL
    https://www.goodreads.com/choiceawards/best-fiction-books-2020, then you should append 
    ("Fiction", "The Testaments (The Handmaid's Tale, #2)", "https://www.goodreads.com/choiceawards/best-fiction-books-2020") 
    to your list of tuples.
    """
    o = open(filepath)
    r = o.read()
    soup = BeautifulSoup(r, "html.parser")

    cat = soup.find_all('h4', class_ = 'category__copy')
    category = []
    for i in cat:
        category.append(i.text.strip())
    #print(category)

    name = soup.find_all("img", class_="category__winnerImage")
    names = []
    for i in name:
        names.append(i['alt'])
    #print(names)

    link = soup.find_all('div', class_ = 'category clearFix')
    url = []
    for i in link:
        new = i.find('a').get('href')
        url.append(new)
    #print(url)

    final = []
    for i in range(len(category)):
        c = category[i]
        n = names[i]
        u = url[i]
        final.append((c, n, u))
    return(final)


#print(summarize_best_books("best_books_2020.htm"))


def write_csv(data, filename):
    """
    Write a function that takes in a list of tuples (called data, i.e. the
    one that is returned by get_titles_from_search_results()), writes the data to a 
    csv file, and saves it to the passed filename.

    The first row of the csv should contain "Book Title" and "Author Name", and
    respectively as column headers. For each tuple in data, write a new
    row to the csv, placing each element of the tuple in the correct column.

    When you are done your CSV file should look like this:

    Book title,Author Name
    Book1,Author1
    Book2,Author2
    Book3,Author3
    ......

    This function should not return anything.
    """
    with open(filename, 'w') as f:
        write = csv.writer(f)
        write.writerow('Book title', 'Author Name')
        for i in data:
            name = i[0]
            author = i[1]
            write.writerow(name, author)


def extra_credit(filepath):
    """
    EXTRA CREDIT

    Please see the instructions document for more information on how to complete this function.
    You do not have to write test cases for this function.
    """
    pass

class TestCases(unittest.TestCase):

    # call get_search_links() and save it to a static variable: search_urls


    def test_get_titles_from_search_results(self):
        # call get_titles_from_search_results() on search_results.htm and save to a local variable

        # check that the number of titles extracted is correct (20 titles)

        # check that the variable you saved after calling the function is a list

        # check that each item in the list is a tuple

        # check that the first book and author tuple is correct (open search_results.htm and find it)

        # check that the last title is correct (open search_results.htm and find it)
        pass

    def test_get_search_links(self):
        # check that TestCases.search_urls is a list

        # check that the length of TestCases.search_urls is correct (10 URLs)


        # check that each URL in the TestCases.search_urls is a string
        # check that each URL contains the correct url for Goodreads.com followed by /book/show/
        pass

    def test_get_book_summary(self):
        # create a local variable – summaries – a list containing the results from get_book_summary()
        # for each URL in TestCases.search_urls (should be a list of tuples)

        # check that the number of book summaries is correct (10)

            # check that each item in the list is a tuple

            # check that each tuple has 3 elements

            # check that the first two elements in the tuple are string

            # check that the third element in the tuple, i.e. pages is an int

            # check that the first book in the search has 337 pages
        pass

    def test_summarize_best_books(self):
        # call summarize_best_books and save it to a variable

        # check that we have the right number of best books (20)

            # assert each item in the list of best books is a tuple

            # check that each tuple has a length of 3

        # check that the first tuple is made up of the following 3 strings:'Fiction', "The Midnight Library", 'https://www.goodreads.com/choiceawards/best-fiction-books-2020'

        # check that the last tuple is made up of the following 3 strings: 'Picture Books', 'Antiracist Baby', 'https://www.goodreads.com/choiceawards/best-picture-books-2020'

        pass

    def test_write_csv(self):
        # call get_titles_from_search_results on search_results.htm and save the result to a variable

        # call write csv on the variable you saved and 'test.csv'

        # read in the csv that you wrote (create a variable csv_lines - a list containing all the lines in the csv you just wrote to above)


        # check that there are 21 lines in the csv

        # check that the header row is correct

        # check that the next row is 'Harry Potter and the Deathly Hallows (Harry Potter, #7)', 'J.K. Rowling'

        # check that the last row is 'Harry Potter: The Prequel (Harry Potter, #0.5)', 'J.K. Rowling'
        pass


#if __name__ == '__main__':
    print(extra_credit("extra_credit.htm"))
    unittest.main(verbosity=2)



