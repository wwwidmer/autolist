WILLIAM WIDMER
Autolist assignment 6/25

Created using:
React (create-react-app)
Python3 django

Getting started:

0.  Install dependencies (node, npm. python3, pip3)
1.  Boot up a virtualenv for python3 (`virtualenv -p python3 venv`) and activate it `source venv/bin/activate`
1.  Install requirements located at auto_list_lite_api/requirements.txt (pip install -r auto_list_lite_api/requirements.txt)
1.  Install node_modules, `cd auto_list_lite_webapp && npm install`
1.  Run everything with $COMMAND

Objective

    Build a very basic "Autolist Lite" app in the web framework(s) of your choosing (e.g. Ruby on Rails, Django, React.js, etc.), showing us how you think as an engineer.

Requirements
Use the latest version of your chosen framework, and any database to back it.
For the front end, use any Javascript framework you wish (or vanilla JS if you want)

Create three pages: a “Home” page, a “Search Results” page and a “Vehicle Details” page.

The Home page contains a simple search form containing a price filter.

The user can filter by price min and price max on the Home page.

The Search Results page contains a paginated list of search results, loaded in real time via API.

Clicking a vehicle search result should open a basic “Vehicle Details” page, displaying a photo and basic info such as Year/Make/Model, populated using data from the search result. Feel free to add any other details you want to display!

In the database, keep track of how many times each result (by VIN) is shown on the “Vehicle Details” page. Treat VIN as a unique identifier for vehicles.

On the “Search Results” page, indicate how many times each result has been viewed on the “Vehicle Details” page. For example each result on the “Search Results” page could have a text area saying “Viewed X times”

API Usage

Our test API requires an API Key, which should be passed in the x-api-key header.

To run a search against our test API, use the following URL pattern:

https://qa878qmgjk.execute-api.us-east-1.amazonaws.com/dev?page=1

Each page contains 20 hits, and you can fetch the next page by incrementing the page param.

To filter by price, pass price_min and price_max params to the url, for example:

https://qa878qmgjk.execute-api.us-east-1.amazonaws.com/dev?page=1&price_min=5000&price_max=9000

Notes

We crafted this exercise for you to spend about 4 hours on, and don’t expect for you to finish everything. Whatever you don’t get to, you’ll continue working on together with an Autolist engineer while pair-programming in the event that you come on-site. That said, you can use whatever resources you like, and take as long as you need. We really value testing as well, so please take that into consideration when managing your time.

Please make sure to include a README file detailing setup instructions, how much time you spend on the exercise, and any pertinent information about the approach you took and the design decisions you made. For any items you were unable to finish, explain the approach you were planning on taking.
