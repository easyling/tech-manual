Page modifiers
--------------

Due to the way Easyling operates, it becomes fairly easy to modify the pages as they are being served. Because the datastream must pass through the proxy to have the translation embedded, Easyling can insert JavaScript modifiers, modify style sheets, and even embed whole new pages. These features can be found under the Page Modifiers menu.

CSS Editor: Easyling can be used to insert locale-specific CSS rules into the site being served. The most common use of this feature is to alter the writing direction for non-Latin scripts, such as Arabic.

JavaScript Editor: the JavaScript edited here is inserted into the &lt;head&gt; element of every page being served through Easyling. By default, it does not replace any previously present &lt;script&gt; elements, being inserted as its own element, but can be used to modify the page behavior in many ways.

Page Replacement: Easyling can create a “virtual” page in the site or override an existing one with custom code. The new code can be entered in a fully featured HTML editor. After saving, the new page will appear in the Pages list, ready for translation, with the corresponding translation memory entries already created.

