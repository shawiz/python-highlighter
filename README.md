Python Highlighter Function
===============================

A python function that highlight document snippets that match a query. 
For example, a search for `deep dish pizza` returns documents that match the query as well as highlights that try to show why the document is relevant. 

The Python Highlighter

1. Highlighter all the words in the query;
2. Are not necessarily the full document (they are instead only a relevant snippet);
3. The given text is highlighted with [[HIGHLIGHT]]…[[ENDHIGHLIGHT]]

Example:

`highlight_doc("I like fish. Little star's deep dish pizza sure is fantastic. Dogs are funny.", "deep dish pizza") -> "Little star's [[HIGHLIGHT]]deep dish pizza[[ENDHIGHLIGHT]] sure is fantastic."`
