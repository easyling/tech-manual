# Client-Side Translator
## Operations
### Overview
The _Client-Side Translator_, codenamed _CREST_, is an alternative publishing mode. Instead of operating in proxy mode, the system generates a Javascript stub that needs to be referenced in the site, and it will translate the page in real time using a dictionary downloaded from the cloud service. Language choice is persisted in the browser's _Local Storage_, enabling automatic translation of any page in the site instantly on landing.

### Setup
Content is collected and translated the same way as normal. Once publishing is needed, content is exported by selecting the _Client side translation_ file format, then publishing the latest export (or the one selected for production) from the _Previous Exports_ screen and clicking the context menu.

The translation loader script can be inserted with a one-liner script element, which is available from the _Global Settings_ screen of the _Publish_ section in the sidebar. The website owner needs to insert this script element into pages requiring translation.  
Once complete, the translations can be requested by adding a query parameter to the URL, with the name `__ptLanguage` and the chosen locale as the value (for example `https://example.com/path/to/page?__ptLanguage=ja-JP`).

## Integrators' Guide
### Elements
_CREST_ is controlled by the loader script, inserted into every page requiring translation. The script element should be inserted as high in the `head` as possible in order to begin translation at the earliest possible point.

Language selection is possible via the sidebar inserted on the right by default, or custom `a` elements that manipulate the value of the `__ptLanguage` query parameter. Note that once a language is selected, the choice is persisted into the browser _Local Storage_, so further links need not be annotated with the query to maintain translation.

On selecting a language, the loader script will insert a new script element referencing the exported dictionary. This download the translations necessary for display and the translator algorithm that processes the available DOM to replace content with the available translations.  
The translator will also attach a `MutationObserver` to the document being displayed that allows it to react to DOM manipulation or newly-appearing elements in real time.

###Interop
In order to provide a seamless user experience, _CREST_ exposes a number of events at key points in the process that allow the containing page to react to the translation process and take action to enhance the experience. The following events are dispatched at various points:

- `crestDictionaryLoadingStart`: Dispatched when a language is selected and download of the corresponding dictionary begins. As the dictionary can be sizeable, this event can be used to display a notification to the visitor advising them that the language is about to change.
- `crestDictionaryLoadingEnd`: Dispatched on completion of the dictionary download. Firing this event means translations are available, and they will be applied to the DOM momentarily. If a notification was displayed on download start, it should be removed on this event.
- `crestDocumentTranslationStart`: Dispatched when the initial translation of the document begins. Firing this event means translations are currently being applied to the entire page, and the displayed language is about to change. In case translation takes significant time, the user may benefit from an overlay or other message notifying them of the process and that the displayed language will change soon.
- `crestDocumentTranslationEnd`: Dispatched when the initial translation of the DOM is complete, and all available content has been replaced. At this point, the page is translated to the best of _CREST_'s abilities, and if an overlay or notification was displayed, it should be removed.
- `crestMutationTranslationStart`: Dispatched when a mutation of the DOM is detected by the attached observer and translation of the new/changed elements begins. This event is unique in that it includes a payload, an array of the `MutationRecord`s that are being processed. These include information about the element name, DOM path, and other data that may be used by the page to react to changes.
- `crestMutationTranslationEnd`: Dispatched when the mutation observer completes its run and designates all mutated elements translated. If a notification was displayed on the preceding event, it should be removed now.

#### Example

```html
<script type="application/javascript">
        document.addEventListener("crestDocumentTranslationStart", () => console.log("Document translation started"));
        document.addEventListener("crestDocumentTranslationEnd", () => console.log("Document translation ended"));
        document.addEventListener("crestMutationTranslationStart", (e) => console.log(`Mutation translation started. Mutated records: ${e.detail.targets}`)); // e.detail.targets contains the array of MutationRecord objects that are being processed in the current run. For more information, see https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord
        document.addEventListener("crestMutationTranslationEnd", () => console.log("Mutation translation ended"));
        document.addEventListener("crestDictionaryLoadingStart", () => console.log("Dictionary download started"));
        document.addEventListener("crestDictionaryLoadingEnd", () => console.log("Dictionary download ended"));

        console.log("Event listeners ready...");
    </script>
```
