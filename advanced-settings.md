# Advanced capabilities

The Translation Proxy offers an ever-expanding host of advanced features with far-reaching impacts.

*Increased Usage Alarm*: the Proxy Application can be configured to send out an email alert if increased resource usage is detected on a project. Alert thresholds can be configured on a per-project basis, with respect to pageviews per second, added source words per second, or translated words per second, or any combination of these. Notification emails come with a cooldown timer: after an alert condition is triggered, no new alerts are sent for the specified time (defaults to 60 minutes, can be configured by the project owners, minimum of 15 minutes).

*Pattern Matching*: the Proxy Application can be given a regular expression to handle automatically generated text. Once the regular expression is entered and saved, all text matching the designated capture group will be considered translation invariant (i.e. the translation is exactly the same as the source). While existing source segments are not deleted, no new segments matching the capture groups will be added.

*Freeze*: the Proxy Application can be instructed to freeze the project pagelist or translation memory. If the pagelist is frozen, the Proxy Application will not add any more pages when crawling the site (although individual pages can still be forced into the database using the Add Pages dialog from the list); while freezing the translation memory will cause the Proxy Application to stop adding any new source segments, even if the page content changes between recrawls. Since the new segments will be left without translations, they will be allowed to bleed through into the translated site.

Note that attempting to activate translation memory freezing without activating pagelist freezing would result in an error, therefore it is not permitted: upon such an action, the Proxy Application will take corrective steps automatically, and enable pagelist freezing or disable translation memory freezing as needed to maintain consistency.

If desired, after freezing the page list, the Proxy Application can be configured to treat any further pages as “Excluded” by activating the “Handle unknown pages as externalized” option. This will cause the Proxy Application to bypass translation for any page that is not in the current pagelist, just as if it was manually excluded. Be aware that on a live site, this may result in an SEO penalty (due to duplicate content being detected by the crawler)!

*Group pages*: the Proxy Application can group automatically generated pages together, preventing new pages from being added, but not removing already added pages, and making the grouped pages share a single dictionary, necessitating translation of only one. The pages will be grouped according to the path rules specified in the textbox, one path per line, with a “`\*`” as the wildcard character. This does not decrease the volume of pages that will be crawled, but it makes project maintenance easier.

*JavaScript Translation*: this field, available only on newly created projects, contains the capture group definitions used to extract attribute-value pairs from JavaScript files selected for translation/localization. After entering the capture parameters and re-crawling the site, the Proxy Application will display the selected JavaScript files as translatable pages in the pagelist, from where they can be selected for translation in the List View like regular pages, and any values for the selected attributes will be made available as translatable entries, which are treated identical to regular entries. Entering “` html`” (N. B. The switch is separated by a space!) after the path specification will result in the Proxy Application applying its HTML parser to the match instead of a plaintext parser, stripping out HTML markup and only offering the actual content for translation (otherwise, should the match contain markup, the translator must take care not to alter it, or risk breaking the translated site).

If a field of the JSON being parsed contains further JSON data in a stringified form `("key": "{\\"key\\":{\\"key\\":\\"value value value\\"}}")`, the path can be passed to a recursive JSON translator by appending “` json`” to the path, then extending the path on the next line by adding “`.json.`”.

*XPath Translation*: the Proxy Application is able to translate XML (eXtensible Markup Language) files sent by the remote server, according to the XPath standard of specifying elements of the XML structure. Similar to JavaScript translation, entering the “` html`” switch will result in the HTML parser being applied, while no switch will parse the match as plaintext.

*Mark multiple resources as translatable*: using URL prefixes (N.B. this requires fully qualified URL prefixes, including protocol, host, and possibly path structures!), the Proxy Application can enforce dictionaries over multiple resources in a single rule. This is especially useful if the site under translation contains an API (especially CREST APIs) whose responses also require translation, and each endpoint is served on a different path; in this case, entering the root of the API here will automatically capture all responses from that path without having to individually mark them as translatable from the Resources menu.

*Additional remote request headers*: if the remote server requires certain headers to be present to serve legal responses, it will not be crawlable by default, as the crawler will not supply these. Entering the required headers here will result in them being appended to every request sent by the Proxy Application, including the crawler requests, letting you crawl the site as required.

*JavaScript Rewriter*: this automated tool will rewrite JavaScript files passing through the proxy, changing fully qualified URLs (beginning with “http://”, containing a top-level domain, followed by a “/”, and optionally any further URIs) to refer to the proxied domain instead of the original domain, thus preserving the integrity of the translation.

*Ignored* *classes*: if a certain class of elements are not ought to be translated, they can be entered here. Elements with these classes will be treated as if they had the `<translate=no>` attribute, and will be treated as translation-invariant.

*Ignored IDs*: similar to the “Ignored classes” option, this allows the treating of specific elements as translation-invariant, this time through HTML IDs.

*Custom HTML attributes*: some CMS-es may employ non-standard HTML attributes on elements to style the page or otherwise affect certain aspects of their operation. If some of these attributes contain translatable text, you can enter them into the “As text” field to instruct the Proxy Application to extract them. If they contain URLs that need to be mapped to the translated domain, you can use the “As link” field to instruct the Proxy Application to map those non-standard link elements as well.

On request, it is also possible to activate an HTML parser for certain attributes, should they contain HTML formatting in their values.

### Tweaks

These features are small alterations to the by-and-large operation of the Proxy Application. Generally, activating them is not necessary for translation, but in some cases, strange server behavior or page structure may necessitate their use. They can be triggered on and off at will.

*Retaining original* `DOCTYPE`s: by default, the Proxy Application generates an HTML5 standards-compliant file to send to the client. If, for some reason, this causes problems due to the site relying on HTML4 standards for operation, some of which may be deprecated by HTML5, enabling this option will cause the Proxy Application to retain the original DOCTYPE declaration of the source page.

*Determine document type by* `GET` *instead of* HEAD: some servers may return different responses to the HEAD request we use to determine document type than the GET request used to download content. Enabling this option forces the Proxy Application to use GET requests for all operations, getting the correct content type from the server (as far as server-side configurations will allow).

*Detect JavaScript content type*: JavaScript may not be explicitly declared as such on the server, being sent to the client with misleading content types. This causes the Proxy Application to mis-identify such streams and not offer operations reserved for JS files. Enabling this option will force a deep check on each file sent to the client, to determine if they are indeed JavaScript code, regardless of their declared content type.

*Download images through the proxy*: this will instruct the Proxy Application to attempt to map all `<img src>` attributes to the proxied domain. This is especially useful if the images are served only after authentication.

*Attempt to place tags according to punctuation when using TM-based pre-translation*: if using a TM-based pre-translation, the Proxy Application may encounter segments where it cannot replace the XLIFF tags automatically, due to overly large differences between the contexts (possibly because of a changed site). If this option is enabled, the translator will try to replace the XLIFF tags according to their positions relative to punctuation marks in the segment. If successful, the TM entry’s confidence score will be increased by 0.1.

*Translate excluded pages when viewing them in Preview mode (but still not in live serving mode)*: at times, it may be necessary to view excluded pages as if they were translated, in order to assess their layout, without actually making them available on the live site. Enabling this option allows just that, by propagating translations to the excluded pages if viewed in Preview mode, but keeping them untranslated in Live serving mode.

*Translate* `javascript:` *attribute*: the Proxy Application is capable of extracting and translating code from the onclick attribute of elements. This feature may be used when a site uses this attribute to store translatable content inlined into the attribute and requires this content to be translated. Currently we only process the onclick event’s contents, all other events in the javascript attribute will be ignored.

*Detect and handle JSON-in-string responses, like* `"{\\"ResponseCode\\":\\"BadRequest\\"}`: string-escaped JSON-format responses can be handled by activating this tweak. If active, the Proxy Application will first attempt to string-unescape the response before passing it to the JSON parser, in order to recreate its base form.

*Make content in* `<script type="text/html"></script>` *translatable as a whole (don't try to parse it as HTML)*: script blocks may contain template data requiring translation, which is often signified by the text/html content type (instead of the more usual application major type). In such cases, HTML parsing can be undesirable, and can be bypassed by activating this option.

*Send a canonical link http header pointing to the original page on externalized pages*: the Proxy Application can insert a Link header into externalized pages, in order to avoid the SEO penalty associated with duplicate content. This header will point to the original address, and have `rel=Canonical` added, to designate the relationship.

### Trigger classes

Translation Proxy has a number of special classes, in addition to the user-specified *Ignore class* es. These must be added to the source content by the client, and triggers special behavior in the proxy either when the content is extracted or during the actual proxying process.

<table>
  <tr>
    <td>Class</td><td>Applicable to</td><td>Effect</td>
  </tr>
  <tr>
    <td><pre>__ptNoRemap</pre></td><td>`a href`</td><td>Affected links are left untouched by the proxy, their destinations are not remapped into relative URLs.</td>
  </tr>
  <tr>
    <td><pre>EL_swap</pre></td><td>Any HTML element</td><td>Affected elements are made available as raw HTML on the Workbench, making the source code editable.</td>
  </tr>
  <tr>
    <td><pre>__ptNoTranslate</pre></td><td>Any HTML element</td><td>Affected elements are hidden from the Workbench, making them untranslatable.</td>
  </tr>
  <tr>
    <td><pre>EL_hide</pre></td><td>Any HTML element</td><td>Affected elements are hidden from the Workbench, making them untranslatable.</td>
  </tr>
</table>

### Manual Publishing

*Manual Publishing* is advanced project control feature that gives project owners the ability to hold back the translations from being published on the live page (but not the preview, as it will always display the latest translation available!) until further notice.

The feature can be activated from the Advanced Settings page. Once activated, it will affect all translations going forward, but already-existing ones will not be “unpublished”.

Once activated, a new item will appear in the Bulk Actions menu, “Publish”. Selecting this action will cause all selected segments to be synchronized with their displayed translations, and once the action finishes, the markers in the status bar on the right of the entries will change to reflect this. If the action encounters an error, the server will attempt to rectify this by publishing the entire entry, after confirmation from the user. If the error is not recoverable, it will list the segments in error.

### Default segment state

By default, the Proxy Application will add new segments during a crawl as “Approved”, making them available for translation immediately after. However, if the user/client desires, this behavior can be changed to adding new segments in one of two states, “Pending” or “Excluded”. If the default setting is changed, the project owner, backup owners, or users with the Customer [role][Sharing Settings] can alter segment states.

“*Pending*” segments are those that are awaiting a decision on translation. They will not be included into exports unless the relevant option is selected at export-time, and will not appear for translation unless filtered for specifically. Users able to alter segment states may move these into either one of the other two states, by approving them for translation, or excluding them entirely.

“*Excluded*” segments are those that have been deemed as not requiring translation at all. Unless the relevant option is selected, they are not included in exports and will not appear for translation unless filtered for specifically. Users able to alter segment states may approve them for translation, making them available.
