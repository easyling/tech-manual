Content scanning
----------------

Scanning extracts content from the pages in the allowed range by attempting to read it into the database, using up the pageWrite quota for legacy accounts, and deducting €2 from the balance of credit-based accounts for every thousand source words. The scanning crawler obeys the same inclusion-exclusion rules as the discovery crawler, but will attempt to copy the page’s content into Google’s Datastore. If the page can be copied successfully, the Proxy Application will process the content once all selected pages have been extracted.

If a link serves content that is not textual (usually HTML), it will be added to the Resources menu instead. This enables the localization of various other types of content, including, but not limited to, inline images, CSS files, and downloadables.

Once all the selected pages have been extracted, the Proxy Application analyzes the extracted content, mapping out the textual structure and searching for repetitions source segments. These repetitions are factored into the final word count. Repetitions of the same source segment are then linked, so that modification of one is replicated across all the other instances of the same segment.

Scanning may be limited to assessing only resources (non-HTML entities) or pages using the checkboxes in the dialog. Additionally, if page or dictionary [freezing] is enabled, the appropriate warning will be displayed by the dialog before crawling is started.

Additionally, Scanning may be used to build up the [Source cache] by ticking the option in the dialog, or can be instructed to use the source cache’s contents (if it exists) instead of the server’s actual response.

Once a project is scanned, there may be suspicions of content inserted by JavaScript (i.e. untranslated content appears that is not available on the Workbench for translation). In such cases, it is advisable to run the Proxy Application’s *JavaScript-generated content check*. This opens each page in turn, checking for JavaScript-inserted content, which may take a long time. Once the scan runs its course, an email is sent to the initiator, with the JS-generated content, as well as the source file (that needs to be added from the Resources list to translate) and suggestions for the search paths that need to be entered into the JavaScript search on the Advanced Settings menu to capture the content for translation.

