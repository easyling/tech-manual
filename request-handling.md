# Request Handling

Easyling operates over Google's AppEngine infrastructure, split into frontend and backend modules. Each module encompasses variable numbers of instances, scaling automatically in response to demand.

Frontend instances serve requests from visitors to translated pages (in addition to serving the Dashboard and providing user-facing functionality).  
Requests are routed to Easyling via the CNAME records created during the publishing process.

+ The incoming requests, based on the domain name, reach the Google Cloud (rerouted via DNS record CNAME, pointing to `ghs.domainverify.net`.
+ Based on the domain name and the deployed Proxy application, AppEngine decides that this specific request should be routed to the Proxy AppEngine deployment.
+ The request reaches the Proxy Application internally; the application does a lookup against the domain for the associated project. There are special domain names, and the final serving domain, for which caching is activated.
+ Based on the URL, the Proxy application determines the matching Page in the Proxy database. The database has a list of segments, pointing to our internal Translation Memory (TM). We retrieve all these existing Database entries, including the translations for the given target language.
+ The Proxy application processes the incoming URL request, and transforms it to point back to the original site's domain. Then, the source content of the translation is sourced, according to cache settings in effect on the project.
    - If source caching is *disabled*, the application issues a request, and retrieves the result from the original web server, which is hosting the original website language. If source caching is enabled, a local copy (a previously stored version of the source HTML) is used, instead of issuing a request to the original web server.
    - If binary caching is *disabled*, the application then builds the Document Object Model (DOM) tree of the result, finally iterates through all the block level elements, and matches them against the segments loaded from the database. If there's a match, we replace the text with the translation. If not, we 'report' it as a missing translation.
    - If binary caching is *enabled* and the checksum of the source HTML *matches* the one stored in the cache, a previously prepared and stored translated HTML is served.
    - If binary caching and keep cache are *both enabled*, and the checksum of the source HTML *doesn’t match* the one stored in the cache, the proxy translates the page using the TM. If the number of translated segments is higher than the previously prepared and stored translated HTML, the new version is served; otherwise the old one. (Keep cache can be thought of as a “poor man’s staging server”).
+ During the process Proxy change some of the URLs so that it points to our domain name, instead of the original. (e.g. translated resources uploaded to Language Solutions Proxy).
+ The application serializes the translated DOM tree, and serves it as an HTML5 stream, as a response to the original request.
