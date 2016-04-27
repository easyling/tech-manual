Site discovery
--------------

Discovery instructs Easyling to map out the structure of the site. It does so by scanning each page for link elements in the markup (the &lt;a href&gt; tags), and attempting to follow these. Any page that can be verified to exist (by the server returning the appropriate HTTP status, usually a HTTP200) is added to the list of pages with the “Discovered” status, while those that are known to exist only by the existence of a link are marked “Unvisited”. If the server returns anything other than a success message, the status code is displayed and the page remains “Unvisited”. This is most commonly seen with HTTP301 (Redirection) or HTTP404 (Not Found) errors.

Discovery uses up the pageRead quota for legacy accounts and costs €1 for one thousand pages for credit-based accounts. Discovery also does not extract content from the site. However, by assessing the text in memory, a preliminary word count may be established.

Exclusion rules may be added at this stage (or any stage), which prevent the crawler from visiting and crawling certain pages or paths. Links pointing into excluded ranges are still discovered, but their destinations are marked “Unvisited”, and further links in the chain are not assessed.

Discovery may be limited to assessing only resources (non-HTML entities) or pages using the checkboxes in the dialog. Additionally, if page or dictionary [freezing] is enabled, the appropriate warning will be displayed by the dialog before crawling is started.

