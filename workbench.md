# The Workbench

The Workbench is the online editing view of the Proxy Application. It can be used to edit segments, as well as to execute mass operations on large numbers of segments during the proofreading and the publishing phases. The main view of the Workbench is the List View, a simple two-up listing of all the content on the page, the secondary is the Highlight View, which renders the page as-is and allows in-context editing of its contents

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
