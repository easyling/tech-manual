URL List manipulation
---------------------

By default, the Proxy Application crawls every single URL in the target domain. For certain sites, this can mean tens of thousands of individual pages if the crawler is not restricted by page number. To avoid premature depletion of quotas, a path restriction system was implemented, allowing users to limit the crawler to certain paths on the site.

If the site’s structure is known in advance, it is possible to specify these path prefixes before Discovery is initiated. If the structure is unknown, a restricted Discovery scan will create a rudimentary map of the site’s structure, providing a basis for manipulating the URL lists.

Restriction rules may have three forms:

-   Inclusion rules: the crawler is restricted to the specified path prefix, and everything outside that is ignored (excluded)

-   Exclusion rules: everything with the given prefix is ignored, but everything else is included in the scan

-   Manual exclusion (“cherry-picking”): only the selected page is excluded from content extraction

These rules can be used in any combination, and without limit. The only illegal rule is including the root directory (“/”), which is equivalent to no rules being specified, therefore this is not permitted, and the Proxy Application will not save such an inclusion rule.

The path prefixes can be entered after opening the Rules editor. Prefixes must be entered starting with the domain’s root (“/”), and should ideally end on a / as well. Also note that the rules you enter are prefixes only, any path beginning with the strings you set will match them, and setting post-fixes (rules matching the *end* of the path) are not possible.

It is also possible to force a set of pages into the Proxy Application’s scope, by using the appropriate function in the page list. Depending on the list is called from, the resulting dialog will either only discover the URLs pasted, or it will extract content right away and process it for translation.

The same dialog can be used to crawl only the publicly accessible parts of the site by giving the Proxy Application the link to the site’s sitemap.xml[^1] file. Once the link is entered, the Proxy Application will parse the XML, and crawl the site accordingly, making sure that only the publicly accessible pages are crawled and extracted.

