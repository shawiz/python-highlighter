Python Highlighter Function
===============================

Highlight document snippets that match a query. 
For example, a search for `deep dish pizza` returns documents that match the query as well as highlights that try to show why the document is relevant. 

The Python Highlighter

1. Highlighter all the words in the query;
2. Are not necessarily the full document. They are instead all connected sentences that contain the query;
3. Matched queries are highlighted with `[[HIGHLIGHT]]...[[ENDHIGHLIGHT]]`

Example:

`highlight_doc("I like fish. Little star's deep dish pizza sure is fantastic. Dogs are funny.", "deep dish pizza")`

yields

`"Little star's [[HIGHLIGHT]]deep dish pizza[[ENDHIGHLIGHT]] sure is fantastic."`
