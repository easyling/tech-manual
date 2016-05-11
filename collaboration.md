# Collaboration

The Translation Proxy offers a multiuser environment for editing your translations. Thanks to Google’s infrastructure, any number of users can work on a single project simultaneously. These users can be assigned specific roles, and with these roles, certain powers that limit their access to the Proxy Application.

The translation workflow in the Proxy Application is split into a maximum of four steps:
- Translation: marked by a `T` and the color yellow
- Proofreading: marked by a `P` and the color cyan
- Second Proofreading: marked by a `Q` and the color violet
- Client approval: marked by the letter `C` and the color aqua

Any user may be assigned any combination of these steps, useful for restricting access to entries in the Workbench.

Every project has an owner, who has unlimited powers over the project: the owner may add or remove anyone on the project, edit any entry in any language, including adding new languages, and change any setting, including the advanced ones. There can only be one owner on a project, but owners may renounce ownership, designating another user and setting their own privileges.

*Linguists* are designated using the *Simplified Dashboard* feature: this limits the user’s access to the dashboard and the Content menu, only permitting segment editing, and only in their designated language and phase. Linguists can also receive notification emails on project updates, and may be given the power to import/export XLIFF files.

*Contributors* are the default users, capable of editing any entry in their selected language and workflow step, but are prevented from doing anything else on the project. They may receive notification emails and project update emails, but they may not edit their features, nor invite anyone else, nor access any of the advanced settings.

*Customers* are a special user class, who are given the ability to manage source segments. By default, the Proxy Application marks all newly discovered segments as “Approved” (as opposed to “Pending” or “Excluded”), which means they are available for translation right away. The setting can be changed under the Advanced Settings menu so newly discovered segments are marked differently, and are not available for translation right away. These pending segments can be managed by the *Customer* role to be approved or excluded entirely, deciding whether or not they are to be translated. Note that the *Customer* needs access to at least one target language and a workflow step to be able to enter the Workbench to select and modify the pending segments!

*Project Managers* are designated by their power to invite others onto the project. Other features and roles can be added as well, but care must be exercised not to include other, conflicting roles, which could re-restrict their access.

*Advanced Project Managers* are designated by the eponymous feature. They are given the power to edit languages, as well as any entry in the project, and editing most setting, up to, and including, the URL inclusion-exclusion rules. However, they cannot change segmentation settings, publishing settings, and certain advanced settings.

*Admins* are designated by their *Backup Owner* role. Their powers equal that of project owners, being able to change any setting and entry, adding or removing users, and modifying the language settings.
