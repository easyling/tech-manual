# Client-Side Translator

## Operations

### Overview

The _Client-Side Translator_, codenamed _Crest_, is an alternative publishing mode. Instead of operating in proxy mode, the system generates a JavaScript stub that needs to be referenced in the site, and it will translate the page in real time using a dictionary downloaded from the cloud service. Language choice is persisted in the browser's _Local Storage_, enabling automatic translation of any page in the site instantly on landing.

### Setup

Content is collected and translated the same way as normal. Once publishing is needed, content is exported by selecting the _Client-side translation_ file format, then publishing the latest export (or the one selected for production) from the _Previous Exports_ screen and clicking the context menu.

The translation loader script can be inserted with a one-liner script element, which is available from the _Global Settings_ screen of the _Publish_ section in the sidebar. The website owner needs to insert this script element into pages requiring translation.

![Copy from the Dashboard and paste into the head](./img/crest.png)

Once complete, the translations can be requested by adding a query parameter to the URL, with the name `__ptLanguage` and the chosen locale as the value (for example `https://example.com/path/to/page?__ptLanguage=ja-JP`).

## Integrators' Guide

### Elements

_Crest_ is controlled by the loader script, inserted into every page requiring translation. The script element should be inserted as high in the `head` as possible in order to begin translation at the earliest possible point.  
The loader script has a number of query parameters that may be used to manipulate its operation. Any number of these can be combined to customize the loader's behaviour from the default settings (existence of said defaults also means _none_ of these parameters are mandatory to supply).

- `languageParameter`: This parameter can be used to change the language selector key from its default of `__ptLanguage`.
- `storageParameter`: This parameter can be used to change the LocalStorage key used to store a previous selection from its default of `ptLanguage`.
- `noXDefault`: if set to `true`, suppress placing an `x-default` link element in the `head` if a translated language is loaded. This may have SEO implications!
- `rewriteUrl`: if set to `true`, use `history.replaceState` to rewrite the URL shown to the user so that it always displays the selected language.
- `scriptUrlIsBase`: if set to `true`, the loader will search for the translator script based on its own URL. **CAUTION: This is not supported under Internet Explorer!**
- `disableSelector`: if set to `true`, the stub will not inject its own language selector in the sidebar. In this case, it is up to the website to provide links to the various language versions.

Language selection is possible via the sidebar inserted on the right by default, or custom `a` elements that manipulate the value of the `__ptLanguage` query parameter. Note that once a language is selected, the choice is persisted into the browser _Local Storage_, so further links need not be annotated with the query to maintain translation.

On selecting a language, the loader script will insert a new script element referencing the exported dictionary. It downloads the translations necessary for display and the translator algorithm that processes the available DOM to replace content with the available translations.  
The translator will also attach a `MutationObserver` to the document being displayed that allows it to react to DOM manipulation or newly-appearing elements in real time.

### Interop

#### Events

In order to provide a seamless user experience, _Crest_ exposes a number of events at key points in the process that allow the containing page to react to the translation process and take action to enhance the experience. The following events are dispatched at various points:

- `crestDictionaryLoadingStart`: Dispatched when a language is selected and download of the corresponding dictionary begins. As the dictionary can be sizeable, this event can be used to display a notification to the visitor advising them that the language is about to change.
- `crestDictionaryLoadingEnd`: Dispatched on completion of the dictionary download. Firing this event means translations are available, and they will be applied to the DOM momentarily. If a notification was displayed on download start, it should be removed on this event.
- `crestDocumentTranslationStart`: Dispatched when the initial translation of the document begins. Firing this event means translations are currently being applied to the entire page, and the displayed language is about to change. In case translation takes significant time, the user may benefit from an overlay or other message notifying them of the process and that the displayed language will change soon.
- `crestDocumentTranslationEnd`: Dispatched when the initial translation of the DOM is complete, and all available content has been replaced. At this point, the page is translated to the best of _Crest_'s abilities, and if an overlay or notification was displayed, it should be removed.
- `crestMutationTranslationStart`: Dispatched when a mutation of the DOM is detected by the attached observer and translation of the new/changed elements begins. This event is unique in that it includes a payload, an array of the `MutationRecord`s that are being processed. These include information about the element name, DOM path, and other data that may be used by the page to react to changes.
- `crestMutationTranslationEnd`: Dispatched when the mutation observer completes its run and designates all mutated elements translated. If a notification was displayed on the preceding event, it should be removed now.

In addition, the `crestStub` event can be used to detect changes in the loader configuration in real-time.

##### Example

```html
<script type="application/javascript">
    document.addEventListener("crestDocumentTranslationStart", () => console.log("Document translation started"));
    document.addEventListener("crestDocumentTranslationEnd", () => console.log("Document translation ended"));
    // e.detail.targets contains the array of MutationRecord objects that are being processed in the current run. For more information, see https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord
    document.addEventListener("crestMutationTranslationStart", (e) => console.log(`Mutation translation started. Mutated records: ${e.detail.targets}`));
    document.addEventListener("crestMutationTranslationEnd", () => console.log("Mutation translation ended"));
    document.addEventListener("crestDictionaryLoadingStart", () => console.log("Dictionary download started"));
    document.addEventListener("crestDictionaryLoadingEnd", () => console.log("Dictionary download ended"));

    document.addEventListener("crestStub", (event) => {
        let changes = event.detail.changes; // List of changes in the state.
        let selectedLanguage = event.detail.state.selectedLanguage; // The currently selected language.
    });

    
    console.log("Event listeners ready...");
</script>
```

## Language selector

Language selectors are crucial for localised websites to ensure that the translations are prominently featured on the website. Crest is compatible with two types of language selector - a dropdown or a sidebar.

### Sidebar

The sidebar language selector is the easiest to integrate. It is part of the loader script, `stub.js`, so no further set-up is needed. It'll insert the flag of available languages to the side for users to click. This option offers minimal configuration. The following options are available:

- The flags of each language.
- The name of the language(s) as displayed when hovered.
- The side the selector should show up.

### Dropdown

For websites where more customisation options are required, the dropdown language selector is available. Setup is slightly more involved:

1. Create and empty `span` or `div` with the class `el-dropdown` (or the one configured on the Dashboard).
2. Add the translator stub with the `?disableSelector` query set to `true` or edit the selector to include this query. While technically not _required_, this step ensures that you do not have two selectors on the website. Without the query, the stub will insert the sidebar language selector too.
3. On the Dashboard, under _Language selector_, select JavaScript publishing and Dropdown. Make sure to save the settings.  
Alternatively, you can copy the embed code available under _Language selector_ on the Dashboard and insert it just like you inserted the stub. It looks something like this:

```html
<script type="text/javascript" src="https://whitelabel.example.com/js/webtranslate/languageDropdown.js?code=r2d4ct3d&v=2"></script>
```

This selector has two main versions. You can select the one you prefer on the Dashboard. V1 shows the currently selected language and the rest of them are available through a drop-down selector. V2 on the other hand is more compact by default. It shows a globe icon (🌐), then the language choice is available via a more modern dropdown design.

V1 offers the following options:

- The flags of each language.
- The name of the language(s) as displayed when hovered.

additionally with V2, you can specify whether the design should incorporate the flags of the languages.
