# webSpider

## Project background
Scanning through web page is tedious and repeatitive. 
The webSpider.py will automatically visit all underlying pages with a given starter URL.

#### Design
(Links) = URLs (both image tag or a tag for the interest of this project)

The main program loop through each elmement (url) from a visited page and re-compute links for the next crawling acitivities. 
(Level) stores and tells the deepth of the webspider drilling to.

Once page is visited it will store into visited list to prevent webspider from getting into a endless loop.

HTML # are skipped and will be treated if its corresponding anchor link is already in (visited) list.

#### Implementation & Dependencies
Python has been chosen over other OOP programming tools. 
Beautiful soup and requests library has been used to meet this specific requirement.



#### Execution
python webspider.py start_url

(i.e.) python webspider.py "www.yahoo.com"




#### Testing
At console, it displays from parent page to all child pages and at the end it shows totally number of pages that the webspider has been visited.



#### Enhancement if time allow
Visualization of the produced result perhelps in **graphical tree structure** similiar to site map
Data analytics on the result of *webspider.py*




