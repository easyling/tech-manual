Easyling Users Manual
=====================

Table of Contents
-----------------

[Table of Contents 1]

[Changelog 2]

[Project generation 3]

[Site discovery 3]

[Content scanning 4]

[URL List manipulation 5]

[The Workbench 7]

[The List View 7]

[The Highlight View 9]

[Resources 10]

[Page modifiers 11]

[Publishing 12]

[Collaboration 12]

[Translation Memories 14]

[Caching 15]

[Advanced capabilities 17]

[Tweaks 21]

[Trigger classes 23]

[Manual Publishing 23]

[Default segment state 24]

Changelog
---------

  ***Date***   ***Changes***
  ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------
  2015.08.30   Integrate changes for credit-based accounts; more specific descriptions; added Increase Usage Alarm
  2015.12.27   Add changes for JSON path translation; multicache; new Tweaks and Advanced Settings; HTML-formatted HTML attribute translation; Workbench SEO filter

Project generation
------------------

While Easyling is capable of processing almost any format of domains, it will automatically process the URL given to use the TLD and any subdomains specified. Additional path structures will be stripped from the initial URL, and must be added back as pages (either by adding via URL or by using the discovery function).

Site discovery
--------------

Discovery instructs Easyling to map out the structure of the site. It does so by scanning each page for link elements in the markup (the &lt;a href&gt; tags), and attempting to follow these. Any page that can be verified to exist (by the server returning the appropriate HTTP status, usually a HTTP200) is added to the list of pages with the “Discovered” status, while those that are known to exist only by the existence of a link are marked “Unvisited”. If the server returns anything other than a success message, the status code is displayed and the page remains “Unvisited”. This is most commonly seen with HTTP301 (Redirection) or HTTP404 (Not Found) errors.

Discovery uses up the pageRead quota for legacy accounts and costs €1 for one thousand pages for credit-based accounts. Discovery also does not extract content from the site. However, by assessing the text in memory, a preliminary word count may be established.

Exclusion rules may be added at this stage (or any stage), which prevent the crawler from visiting and crawling certain pages or paths. Links pointing into excluded ranges are still discovered, but their destinations are marked “Unvisited”, and further links in the chain are not assessed.

Discovery may be limited to assessing only resources (non-HTML entities) or pages using the checkboxes in the dialog. Additionally, if page or dictionary [freezing] is enabled, the appropriate warning will be displayed by the dialog before crawling is started.

Content scanning
----------------

Scanning extracts content from the pages in the allowed range by attempting to read it into the database, using up the pageWrite quota for legacy accounts, and deducting €2 from the balance of credit-based accounts for every thousand source words. The scanning crawler obeys the same inclusion-exclusion rules as the discovery crawler, but will attempt to copy the page’s content into Google’s Datastore. If the page can be copied successfully, Easyling will process the content once all selected pages have been extracted.

If a link serves content that is not textual (usually HTML), it will be added to the Resources menu instead. This enables the localization of various other types of content, including, but not limited to, inline images, CSS files, and downloadables.

Once all the selected pages have been extracted, Easyling analyzes the extracted content, mapping out the textual structure and searching for repetitions source segments. These repetitions are factored into the final word count. Repetitions of the same source segment are then linked, so that modification of one is replicated across all the other instances of the same segment.

Scanning may be limited to assessing only resources (non-HTML entities) or pages using the checkboxes in the dialog. Additionally, if page or dictionary [freezing] is enabled, the appropriate warning will be displayed by the dialog before crawling is started.

Additionally, Scanning may be used to build up the [Source cache] by ticking the option in the dialog, or can be instructed to use the source cache’s contents (if it exists) instead of the server’s actual response.

Once a project is scanned, there may be suspicions of content inserted by JavaScript (i.e. untranslated content appears that is not available on the Workbench for translation). In such cases, it is advisable to run Easyling’s *JavaScript-generated content check*. This opens each page in turn, checking for JavaScript-inserted content, which may take a long time. Once the scan runs its course, an email is sent to the initiator, with the JS-generated content, as well as the source file (that needs to be added from the Resources list to translate) and suggestions for the search paths that need to be entered into the JavaScript search on the Advanced Settings menu to capture the content for translation.

URL List manipulation
---------------------

By default, Easyling crawls every single URL in the target domain. For certain sites, this can mean tens of thousands of individual pages if the crawler is not restricted by page number. To avoid premature depletion of quotas, a path restriction system was implemented, allowing users to limit the crawler to certain paths on the site.

If the site’s structure is known in advance, it is possible to specify these path prefixes before Discovery is initiated. If the structure is unknown, a restricted Discovery scan will create a rudimentary map of the site’s structure, providing a basis for manipulating the URL lists.

Restriction rules may have three forms:

-   Inclusion rules: the crawler is restricted to the specified path prefix, and everything outside that is ignored (excluded)

-   Exclusion rules: everything with the given prefix is ignored, but everything else is included in the scan

-   Manual exclusion (“cherry-picking”): only the selected page is excluded from content extraction

These rules can be used in any combination, and without limit. The only illegal rule is including the root directory (“/”), which is equivalent to no rules being specified, therefore this is not permitted, and Easyling will not save such an inclusion rule.

The path prefixes can be entered after opening the Rules editor. Prefixes must be entered starting with the domain’s root (“/”), and should ideally end on a / as well. Also note that the rules you enter are prefixes only, any path beginning with the strings you set will match them, and setting post-fixes (rules matching the *end* of the path) are not possible.

It is also possible to force a set of pages into Easyling’s scope, by using the appropriate function in the page list. Depending on the list is called from, the resulting dialog will either only discover the URLs pasted, or it will extract content right away and process it for translation.

The same dialog can be used to crawl only the publicly accessible parts of the site by giving Easyling the link to the site’s sitemap.xml[^1] file. Once the link is entered, Easyling will parse the XML, and crawl the site accordingly, making sure that only the publicly accessible pages are crawled and extracted.

The Workbench
-------------

The Workbench is the online editing view of Easyling. It can be used to edit segments, as well as to execute mass operations on large numbers of segments during the proofreading and the publishing phases. The main view of the Workbench is the List View, a simple two-up listing of all the content on the page, the secondary is the Highlight View, which renders the page as-is and allows in-context editing of its contents

The Workbench is opened using the Pages list: each line in the list reveals a toolbar when hovered over, including the “Translate in Workbench” button, which will load the Workbench for the desired page. Once opened, the Workbench can be navigated to other pages using the Page dropdown in the upper left area. The Page dropdown can be searched to locate specific pages. Also in the header is the target language selector, allowing the user to switch to other target languages, if more than one exists on the project. The page can also be previewed using the Eye Icon.

### The List View

The List View is a simple two-up editor to edit translations without the requirement of creating an XLIFF-export. It also allows various filtering options and mass operations, as well as pre-translations and translation clearing.

The user can execute Bulk Operations on the List View’s contents. Bulk Operations include mass-confirming or unconfirming segments, moving them between exclusion states, or publishing them as one.

In the List View, the segment list may be filtered or searched along multiple criteria. The search bar accepts various modifier tokens, which are listed in the placeholder.

-   A simply entered search term will execute a text search in both the source and target content

-   Prefacing the term with source: or target: will restrict the search to the designated content

-   Encapsulating the term into “quotation marks” will execute a case-sensitive search for the exact term entered

-   Entering a /pair of forward slashes/ instructs the Workbench to treat their contents as a regular expression, allowing regex searches. Also, clicking the magnifying glass in this mode allows the user to delete source segments matching the pattern

-   Prefacing the term with a \~ will stem the search term and use Google’s Search API to execute the search in order to return more results.

Also available in the list view are the segment filters. These filters allow the user to narrow down the segments according to various criteria, from the presence or absence of comments through presence of target content to the level of TM-based pre-translation confidence. Additionally, filtering is also possible based on the source location of the segment in the original document. The document path filter section contains a pre-loaded SEO-preset (activated by clicking the link), which only retains the most relevant elements for SEO.

From the same toolbar, the user can either remove the translations of all segments on the page (CAUTION: this erasure does not obey the currently active filtering settings, all segments will be erased on the page!), or conduct automated pre-translations by applying a TM assigned to the project or using a machine translation engine (including a quick pseudo-translation that reverses the content).

The right sidebar contains the suggestions for the currently selected segment, coming from either any assigned TMs on the project or active machine translation engines; and the segment history, including the segment creation date as the very first item. Clicking any of the suggestions will enter its contents into the target editor, preparing the translation for submission.

Also on this toolbar, the user can select a Work Package to filter the contents (or create one). This allows you to view the contents for a given work package, a “snapshot” of the site at a given time. If the user is assigned more than one workflow role in the [Sharing Settings], they can be switched here.

In the target editor, apart from entering translations manually, the user has the option of copying the source content verbatim, copying only the tags, or resetting the segment to mark it as “missing its translation”. Further, the editor can be configured to retain manually inserted line breaks using the button on its right. Any XLIFF tags that are displayed in the editor can be drag-and-dropped to their rightful places, useful for “fixing” 98% or lower TM-matches that have the tags in the wrong places.

### The Highlight View

The Highlight View is the secondary view mode of the Workbench. It renders the page fully and allows in-context verification and modification of the target content. While filtering options work in the Highlight View as well, they do not produce visible results.

Some sites may interfere with the Highlight View’s operation via their internal JavaScript and render it inoperable. In some cases, it is possible to inject custom JavaScript into the page to override any defense mechanisms that may be attempting to redirect the page or hide its contents, in other cases, it may take prohibitive amounts of time and resources to achieve this.

Regardless of the Highlight View’s state, the list view, as a separate component, remains operational in all cases.

Resources
---------

Easyling is also capable of localizing binary resources (images, CSS and JS files, PDFs, etc.) found on pages. Such resources are identified during content extraction (any file that is not HTML by content will be treated as a resource), and are placed into the Resources menu under Content. Here they can be selected for replacement, with the localized version uploaded by language.

Additionally, .js files may be added to the translatable pages list from here. This enables the localization of JavaScripts. In order to take advantage of this feature, the file must first be selected for placing into the page list, after which one or more search terms must be entered in the Advanced settings menu. These search terms restrict Easyling to extracting certain variable names during the subsequent content extraction scan. After this, the .js file will be made available as a translatable page, with the variable values being entered into the translation memory. These values can be replaced like any translatable text, after which the file is recompiled in real-time with the new values, and loaded along with the page.

The feature depends heavily on the JavaScript being structured properly and having properly named variables and data structures which can be interpreted and whose values can be replaced to achieve changes in the loaded page. Also, careless modification of the variable values can have unknown consequences on the page’s operation and may cause the site to stop working altogether if a vital value is modified improperly.

Page modifiers
--------------

Due to the way Easyling operates, it becomes fairly easy to modify the pages as they are being served. Because the datastream must pass through the proxy to have the translation embedded, Easyling can insert JavaScript modifiers, modify style sheets, and even embed whole new pages. These features can be found under the Page Modifiers menu.

CSS Editor: Easyling can be used to insert locale-specific CSS rules into the site being served. The most common use of this feature is to alter the writing direction for non-Latin scripts, such as Arabic.

JavaScript Editor: the JavaScript edited here is inserted into the &lt;head&gt; element of every page being served through Easyling. By default, it does not replace any previously present &lt;script&gt; elements, being inserted as its own element, but can be used to modify the page behavior in many ways.

Page Replacement: Easyling can create a “virtual” page in the site or override an existing one with custom code. The new code can be entered in a fully featured HTML editor. After saving, the new page will appear in the Pages list, ready for translation, with the corresponding translation memory entries already created.

Publishing
----------

To be able to serve the translations, Easyling needs the serving domain mapped into the Google AppEngine system. Due to Google’s update of their domain mapping architecture, it is now possible to push domains into the system by the simple insertion of three CNAME records into the DNS settings for that given domain.

When publishing the translated site, it is highly recommended to have the domain provider/registrar’s control panel already open, and the DNS settings loaded up. In the Publish Website menu, after selecting the language to be published, and entering the desired serving domain, the key-value pairs in the table below the inputs will change accordingly. These values need to be entered into the DNS settings for the domain, after which propagation may take up to 24 hours, depending on the domain provider’s configuration. Once the new records have propagated (after a recommended wait of 24 hours), pressing the “Verify” button will query the appropriate addresses and check the returned DNS records. If they match the generated values, Easyling sets the appropriate flag on the project, publishing it instantly.

Collaboration
-------------

Easyling offers a multiuser environment for editing your translations. Thanks to Google’s infrastructure, any number of users can work on a single project simultaneously. These users can be assigned specific roles, and with these roles, certain powers that limit their access to Easyling.

The translation workflow in Easyling is split into a maximum of four steps: Translation (marked by a T and the color yellow), two steps of Proofreading (first and second marked by a P and Q, and the colors cyan and violet, respectively), and Client approval (marked by the letter C and the color aqua). Any user may be assigned any combination of these steps, useful for restricting access to entries in the Workbench.

Every project has an owner, who has unlimited powers over the project: the owner may add or remove anyone on the project, edit any entry in any language, including adding new languages, and change any setting, including the advanced ones. There can only be one owner on a project, but owners may renounce ownership, designating another user and setting their own privileges.

*Linguists* are designated using the *Simplified Dashboard* feature: this limits the user’s access to the dashboard and the Content menu, only permitting segment editing, and only in their designated language and phase. Linguists can also receive notification emails on project updates, and may be given the power to import/export XLIFF files.

*Contributors* are the default users, capable of editing any entry in their selected language and workflow step, but are prevented from doing anything else on the project. They may receive notification emails and project update emails, but they may not edit their features, nor invite anyone else, nor access any of the advanced settings.

*Customers* are a special user class, who are given the ability to manage source segments. By default, Easyling marks all newly discovered segments as “Approved” (as opposed to “Pending” or “Excluded”), which means they are available for translation right away. The setting can be changed under the Advanced Settings menu so newly discovered segments are marked differently, and are not available for translation right away. These pending segments can be managed by the *Customer* role to be approved or excluded entirely, deciding whether or not they are to be translated. Note that the *Customer* needs access to at least one target language and a workflow step to be able to enter the Workbench to select and modify the pending segments!

*Project Managers* are designated by their power to invite others onto the project. Other features and roles can be added as well, but care must be exercised not to include other, conflicting roles, which could re-restrict their access.

*Advanced Project Managers* are designated by the eponymous feature. They are given the power to edit languages, as well as any entry in the project, and editing most setting, up to, and including, the URL inclusion-exclusion rules. However, they cannot change segmentation settings, publishing settings, and certain advanced settings.

*Admins* are designated by their *Backup Owner* role. Their powers equal that of project owners, being able to change any setting and entry, adding or removing users, and modifying the language settings.

Translation Memories
--------------------

Easyling can use translation memories to aid in the pre-translation of the site. Memories can be imported from standards-compliant TMX files, or can be populated from the project itself. Once a memory has been created, it will remain accessible to the user across projects, to be used for pre-translation. Memories can also be exported in the same TMX format they are imported in.

During pre-translation, confidence level thresholds can be set for using the memory contents, as well as for automatically confirming these entries. Several memories can be assigned to a given project, and pre-translation will use all of them at once to draw translations from, however, only the default memory can be written to on the project.

Caching
-------

*Target Cache*: the Target cache option is used to achieve great boosts in page serving speed by enabling the proxy to skip processing the page instantly if the remote server’s response matches the response that was used to generate the cache during building. By not having to insert the translations separately, page serving can be accelerated by several milliseconds, which can add up to a noticeable speedup in the case of larger pages with lots of translated content.

The Target cache is built or overwritten every time a page is loaded through the proxy, with a few notable exceptions. The cache is not overwritten if the content served matches the content received (i.e. no processing was done on it), nor are entities larger than the hard-coded maximum entity size (960kb) saved. Furthermore, if a site changes its contents too fast (there are too many cache misses, i.e. the cached content differs from the actual), the Proxy will stop caching the given entity to prevent overusing the database. Should this happen, caches must be cleared manually to restore normal operation and reset the cache miss limit.

*Keep Cache*: the Keep cache is actually a serving mode of the Target cache, used mainly to prevent the *source language bleed-through effect*, or *Bleeding Effect* in short. It operates by checking the cached content’s translation ration against the remote server’s response. If the cached content is found to have a more complete translation (i.e. its translation ratio is higher), the remote response is discarded and the cached content is served instead. This does not mean an increase in page load speed, but by preventing yet-untranslated elements from appearing in the served page, the *Bleeding Effect* is eliminated entirely. As new translations are entered into the database, either manually or via XLIFF imports, the difference between the cached response and the actual response decreases, and the newly-translated elements are displayed automatically. Additionally, this check is run every time the source content is found.

*Source Cache*: the Source cache option records the entire response from the remote server, and forwards it to the client if the path prefixes entered in the text field match (an empty field means that the cached content is served regardless of path), and the page is not externalized. Since this only caches the remote server’s response, it is only capable of providing a smaller increase in serving speed (since processing still needs to be done on the response to create the translated page), it can be used to speed up loading of sites served from overloaded or outdated servers, and can also be used to mask changes on the remote server by supplying the cached response to the Proxy.

Unlike the Target cache, this cache is only built during crawling, and ***only*** if the appropriate options are selected (Build source cache checkbox in the Scan dialog or the Add Pages dialog). Furthermore, pages in question must not be excluded from the crawl to download and cache them, and content from third-party servers (such as content Delivery Networks (CDNs)) are not retained in the cache. Lastly, the same hard-coded limitation of 960kb applies here as well.

On the other hand, selecting the “Preserve & use existing cache” option in the Scan dialog instructs the Proxy to re-use the existing Source cache instead of renewing and overwriting it. When this option is checked, it becomes possible to use the Source cache as a version of the staging server, by continuously supplying the same remote server response to mask any changes done to the original site before a cache is rebuilt.

The cache information for each page can be queried individually by clicking the Cache button on the page’s row. This displays a dialog detailing the currently active caches, when they were generated, and allows the project owner to clear each cache separately for each page (useful for hunting down issues when the translated page doesn’t display a change recently made on the original).

With the 2015 December rollout of the Multicache feature, Easyling has gained the ability to use different caches in different proxy modes. There exists a default cache for both the Target and the Source cache, and the project owner can create up to five named caches for each mode. These caches can be renamed at will, and their contents purged, but cannot be deleted.

Advanced capabilities
---------------------

Easyling offers an ever-expanding host of advanced features with far-reaching impacts.

*Increased Usage Alarm*: Easyling can be configured to send out an email alert if increased resource usage is detected on a project. Alert thresholds can be configured on a per-project basis, with respect to pageviews per second, added source words per second, or translated words per second, or any combination of these. Notification emails come with a cooldown timer: after an alert condition is triggered, no new alerts are sent for the specified time (defaults to 60 minutes, can be configured by the project owners, minimum of 15 minutes).

*Pattern Matching*: Easyling can be given a regular expression to handle automatically generated text. Once the regular expression is entered and saved, all text matching the designated capture group will be considered translation invariant (i.e. the translation is exactly the same as the source). While existing source segments are not deleted, no new segments matching the capture groups will be added.

*Freeze*: Easylingcan be instructed to freeze the project pagelist or translation memory. If the pagelist is frozen, Easyling will not add any more pages when crawling the site (although individual pages can still be forced into the database using the Add Pages dialog from the list); while freezing the translation memory will cause Easyling to stop adding any new source segments, even if the page content changes between recrawls. Since the new segments will be left without translations, they will be allowed to bleed through into the translated site.

Note that attempting to activate translation memory freezing without activating pagelist freezing would result in an error, therefore it is not permitted: upon such an action, Easyling will take corrective steps automatically, and enable pagelist freezing or disable translation memory freezing as needed to maintain consistency.

If desired, after freezing the page list, Easyling can be configured to treat any further pages as “Excluded” by activating the “Handle unknown pages as externalized” option. This will cause Easyling to bypass translation for any page that is not in the current pagelist, just as if it was manually excluded. Be aware that on a live site, this may result in an SEO penalty (due to duplicate content being detected by the crawler)!

*Group pages*: Easyling can group automatically generated pages together, preventing new pages from being added, but not removing already added pages, and making the grouped pages share a single dictionary, necessitating translation of only one. The pages will be grouped according to the path rules specified in the textbox, one path per line, with a “\*” as the wildcard character. This does not decrease the volume of pages that will be crawled, but it makes project maintenance easier.

*JavaScript Translation*: this field, available only on newly created projects, contains the capture group definitions used to extract attribute-value pairs from JavaScript files selected for translation/localization. After entering the capture parameters and re-crawling the site, Easyling will display the selected JavaScript files as translatable pages in the pagelist, from where they can be selected for translation in the List View like regular pages, and any values for the selected attributes will be made available as translatable entries, which are treated identical to regular entries. Entering “ html” (N. B. The switch is separated by a space!) after the path specification will result in Easyling applying its HTML parser to the match instead of a plaintext parser, stripping out HTML markup and only offering the actual content for translation (otherwise, should the match contain markup, the translator must take care not to alter it, or risk breaking the translated site).

If a field of the JSON being parsed contains further JSON data in a stringified form ("key": "{\\"key\\":{\\"key\\":\\"value value value\\"}}"), the path can be passed to a recursive JSON translator by appending “ json” to the path, then extending the path on the next line by adding “.json.”.

*XPath Translation*: Easyling is able to translate XML (eXtensible Markup Language) files sent by the remote server, according to the XPath standard of specifying elements of the XML structure. Similar to JavaScript translation, entering the “ html” switch will result in the HTML parser being applied, while no switch will parse the match as plaintext.

*Mark multiple resources as translatable*: using URL prefixes (N.B. this requires fully qualified URL prefixes, including protocol, host, and possibly path structures!), Easyling can enforce dictionaries over multiple resources in a single rule. This is especially useful if the site under translation contains an API (especially CREST APIs) whose responses also require translation, and each endpoint is served on a different path; in this case, entering the root of the API here will automatically capture all responses from that path without having to individually mark them as translatable from the Resources menu.

*Additional remote request headers*: if the remote server requires certain headers to be present to serve legal responses, it will not be crawlable by default, as the crawler will not supply these. Entering the required headers here will result in them being appended to every request sent by Easyling, including the crawler requests, letting you crawl the site as required.

*JavaScript Rewriter*: this automated tool will rewrite JavaScript files passing through the proxy, changing fully qualified URLs (beginning with “http://”, containing a top-level domain, followed by a “/”, and optionally any further URIs) to refer to the proxied domain instead of the original domain, thus preserving the integrity of the translation.

*Ignored* *classes*: if a certain class of elements are not ought to be translated, they can be entered here. Elements with these classes will be treated as if .they had the &lt;translate=no&gt; attribute, and will be treated as translation-invariant.

*Ignored IDs*: similar to the “Ignored classes” option, this allows the treating of specific elements as translation-invariant, this time through HTML IDs.

*Custom HTML attributes*: some CMS-es may employ non-standard HTML attributes on elements to style the page or otherwise affect certain aspects of their operation. If some of these attributes contain translatable text, you can enter them into the “As text” field to instruct Easyling to extract them. If they contain URLs that need to be mapped to the translated domain, you can use the “As link” field to instruct Easyling to map those non-standard link elements as well.

On request, it is also possible to activate an HTML parser for certain attributes, should they contain HTML formatting in their values.

### Tweaks

These features are small alterations to the by-and-large operation of Easyling. Generally, activating them is not necessary for translation, but in some cases, strange server behavior or page structure may necessitate their use. They can be triggered on and off at will.

*Retaining original* DOCTYPE*-s*: by default, Easyling generates an HTML5 standards-compliant file to send to the client. If, for some reason, this causes problems due to the site relying on HTML4 standards for operation, some of which may be deprecated by HTML5, enabling this option will cause Easyling to retain the original DOCTYPE declaration of the source page.

*Determine document type by* GET *instead of* HEAD: some servers may return different responses to the HEAD request we use to determine document type than the GET request used to download content. Enabling this option forces Easyling to use GET requests for all operations, getting the correct content type from the server (as far as server-side configurations will allow).

*Detect JavaScript content type*: JavaScript may not be explicitly declared as such on the server, being sent to the client with misleading content types. This causes Easyling to mis-identify such streams and not offer operations reserved for JS files. Enabling this option will force a deep check on each file sent to the client, to determine if they are indeed JavaScript code, regardless of their declared content type.

*Download images through the proxy*: this will instruct Easyling to attempt to map all &lt;img src&gt; attributes to the proxied domain. This is especially useful if the images are served only after authentication.

*Attempt to place tags according to punctuation when using TM-based pre-translation*: if using a TM-based pre-translation, Easyling may encounter segments where it cannot replace the XLIFF tags automatically, due to overly large differences between the contexts (possibly because of a changed site). If this option is enabled, the translator will try to replace the XLIFF tags according to their positions relative to punctuation marks in the segment. If successful, the TM entry’s confidence score will be increased by 0.1.

*Translate excluded pages when viewing them in Preview mode (but still not in live serving mode)*: at times, it may be necessary to view excluded pages as if they were translated, in order to assess their layout, without actually making them available on the live site. Enabling this option allows just that, by propagating translations to the excluded pages if viewed in Preview mode, but keeping them untranslated in Live serving mode.

*Translate* javascript: *attribute*: Easyling is capable of extracting and translating code from the onclick attribute of elements. This feature may be used when a site uses this attribute to store translatable content inlined into the attribute and requires this content to be translated. Currently we only process the onclick event’s contents, all other events in the javascript attribute will be ignored.

*Detect and handle JSON-in-string responses, like* "{\\"ResponseCode\\":\\"BadRequest\\"}*"*: string-escaped JSON-format responses can be handled by activating this tweak. If active, Easyling will first attempt to string-unescape the response before passing it to the JSON parser, in order to recreate its base form.

*Make content in* &lt;script type="text/html"&gt;&lt;/script&gt; *translatable as a whole (don't try to parse it as HTML)*: script blocks may contain template data requiring translation, which is often signified by the text/html content type (instead of the more usual application major type). In such cases, HTML parsing can be undesirable, and can be bypassed by activating this option.

*Send a canonical link http header pointing to the original page on externalized pages*: Easyling can insert a Link header into externalized pages, in order to avoid the SEO penalty associated with duplicate content. This header will point to the original address, and have rel=Canonical added, to designate the relationship.

### Trigger classes

Easyling has a number of special classes, in addition to the user-specified *Ignore class*es. These must be added to the source content by the client, and triggers special behavior in the proxy either when the content is extracted or during the actual proxying process.

  -------------------------------------------------------------------------------------------------------------------------------------------------
  Class                 Applicable to      Effect
  --------------------- ------------------ --------------------------------------------------------------------------------------------------------
  “\_\_ptNoRemap”       &lt;a href&gt;     Affected links are left untouched by the proxy, their destinations are not remapped into relative URLs

  “EL\_swap”            Any HTML element   Affected elements are made available as raw HTML on the Workbench, making the source code editable.

  “\_\_ptNoTranslate”                      Affected elements are hidden from the Workbench, making them untranslatable.
                                           
  “EL\_hide”                               
  -------------------------------------------------------------------------------------------------------------------------------------------------

### Manual Publishing

*Manual Publishing* is advanced project control feature that gives project owners the ability to hold back the translations from being published on the live page (but not the preview, as it will always display the latest translation available!) until further notice.

The feature can be activated from the Advanced Settings page. Once activated, it will affect all translations going forward, but already-existing ones will not be “unpublished”.

Once activated, a new item will appear in the Bulk Actions menu, “Publish”. Selecting this action will cause all selected segments to be synchronized with their displayed translations, and once the action finishes, the markers in the status bar on the right of the entries will change to reflect this. If the action encounters an error, the server will attempt to rectify this by publishing the entire entry, after confirmation from the user. If the error is not recoverable, it will list the segments in error.

### Default segment state

By default, Easyling will add new segments during a crawl as “Approved”, making them available for translation immediately after. However, if the user/client desires, this behavior can be changed to adding new segments in one of two states, “Pending” or “Excluded”. If the default setting is changed, the project owner, backup owners, or users with the Customer [role][Sharing Settings] can alter segment states.

“*Pending*” segments are those that are awaiting a decision on translation. They will not be included into exports unless the relevant option is selected at export-time, and will not appear for translation unless filtered for specifically. Users able to alter segment states may move these into either one of the other two states, by approving them for translation, or excluding them entirely.

“*Excluded*” segments are those that have been deemed as not requiring translation at all. Unless the relevant option is selected, they are not included in exports and will not appear for translation unless filtered for specifically. Users able to alter segment states may approve them for translation, making them available.

[^1]: This file is used primarily by search engines to simplify the crawling of the site in question and discover additional information to aid in result ranking during searches.

  [Table of Contents 1]: #_Toc428711598
  [Changelog 2]: #_Toc428711599
  [Project generation 3]: #_Toc428711600
  [Site discovery 3]: #_Toc428711601
  [Content scanning 4]: #_Toc428711602
  [URL List manipulation 5]: #_Toc428711603
  [The Workbench 7]: #_Toc428711604
  [The List View 7]: #_Toc428711605
  [The Highlight View 9]: #_Toc428711606
  [Resources 10]: #_Toc428711607
  [Page modifiers 11]: #_Toc428711608
  [Publishing 12]: #_Toc428711609
  [Collaboration 12]: #_Toc428711610
  [Translation Memories 14]: #_Toc428711611
  [Caching 15]: #_Toc428711612
  [Advanced capabilities 17]: #_Toc428711613
  [Tweaks 21]: #_Toc428711614
  [Trigger classes 23]: #_Toc428711615
  [Manual Publishing 23]: #_Toc428711616
  [Default segment state 24]: #_Toc428711617
  [freezing]: #Freeze
  [Source cache]: #sourceCache
  [Sharing Settings]: #Collaboration
