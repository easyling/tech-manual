# The Crawler

## Overview

The Translation Proxy employs a highly configurable crawler algorithm to map out sites, establish word counts, and extract content. It does so by requesting pages from the remote server, traversing the deserialized DOM scanning for link elements in the markup (the `<a>` and `<src>` elements), and attempting to follow these. Any page that can be verified to exist (by the server returning the appropriate HTTP status, usually a HTTP200, in response to a `HEAD` request) is added to the list of pages with the appropriate status, while those that are known to exist only by the existence of a link are marked “Unvisited”. If the server returns anything other than a success message, the status code is displayed and the page remains “Unvisited”. This is most commonly seen with HTTP301 (Redirection) or HTTP404 (Not Found) errors.

The crawler operates on an unprocessed DOM, generated from the HTML source. JavaScript code is not executed (but their contents may be parsed if the project is configured to do so), nor is any content depending on user interaction discovered. Unpaired HTML elements are normalized, and invalid elements are discarded.

Requests are sent via Google's URLFetch service. Therefore, requests will come from Google-controlled IPs (unless specific configuration is applied). The user-agent will always contain the string "Appengine Google" due to Google's enforcement of this header - this may cause undesired behavior in certain caching/access-control systems, such as WPEngine's anti-bot algorithm.  
If required, all proxy requests (crawler and page serving) may be routed through a fixed IP address outside of Google's IP range. This may be used to circumvent access control restrictions.

## Modes of operation

The crawler distinguishes two main modes of operation, based on whether content is being extracted from the target site and stored as `SourceEntry` entities: if content is not being stored, the crawl is deemed a "dry" crawl (named Discovery on the UI), otherwise, it is "non-dry" (named Content Scan).  
When a dry crawl is executed, content is assessed in-memory and word counts are generated based on the current state of the project - the statistics table is re-initialized for each run, and nothing carries over to subsequent runs.  
During a non-dry crawl, the text content of DOM nodes and attributes (based on project configuration) is extracted and stored in the Datastore as `SourceEntry` entities. Content is then analyzed based on the available dictionary, meaning word counts reflect the statistics and state of the project since its creation - pre-existing content, possibly no longer on the page, is also assessed and factored into repetitions and unique word counts.

Both crawl types may be further subdivided based on scope: it is possible to start the crawl by restricting it to a predefined list of URLs or allowing it to traverse the site as directed by internal links.  
When the crawler operates on a known list of pages (termed the "Add Pages" function on the UI), page number limitations are ignored and pages referenced by the scanned items are not added to the project, unless explicitly specified when starting the crawl.  
When the crawler traverses the site by following internal links, by default, it does so by sending plain `HEAD` or `GET` requests to the remote server. Based on project and crawl configuration, it is possible to include custom headers or cookie data in the crawl requests. Crawl depth limits and page exclusions/skipping may be configured on a per-crawl basis (these options are not saved *by design*, though their individual configurations persist across sessions) before the crawl is created. Once the crawl begins, the `CrawlJob` entity associated with the crawl creates a snapshot of the current path prefixes on the project, as well as other crawl data - once the crawl begins, the options are committed, and can not be changed without stopping and re-starting the crawl!

Exclusion rules may be added at this stage (or any stage), which prevent the crawler from visiting and crawling certain pages or paths. Links pointing into excluded ranges are still discovered, but their destinations are marked “Unvisited”, and further links in the chain are not assessed.

Discovery may be limited to assessing only resources (non-HTML entities) or pages using the checkboxes in the dialog. Additionally, if page or dictionary freezing is enabled, the appropriate warning will be displayed by the dialog before crawling is started.
