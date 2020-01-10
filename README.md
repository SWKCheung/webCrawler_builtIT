# webCrawler_builtIT

Scanning through web page is tedious and repeatitive. 
The webSpider.py will automatically visit all underlying pages with a given starter URL.


(Links) = URLs (both image tag or a tag for the interest of this project)

The main program loop through each elmement (url) from a visited page and re-compute links for the next crawling acitivities. 
(Level) stores and tells the deepth of the webspider drilling to.

Once page is visited it will store into visited list to prevent webspider from getting into a endless loop.

HTML # are skipped and will be treated if its corresponding anchor link is already in (visited) list.
