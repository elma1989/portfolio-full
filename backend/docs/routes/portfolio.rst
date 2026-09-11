Portfolio
^^^^^^^^^^^^

.. toctree::

.. http:get:: /

    Opens main portfolio page.

    :statuscode 200: Main page successfully loaded.
    :statuscode 404: Main page not found.

.. http:get:: /docs/

    Loads this documentation.

    :statuscode 200: Documentation successfully loaded.
    :statuscode 404: Documentation not found.

.. http:post:: /contact

    Sends contact data to backend.

    :<json string name: Name of reqeuster.
    :<json string email: E-Mail of requester.
    :<json string question: Question of requester.

    :statuscode 200: Data successfully submited.
    :statuscode 400: Minimum one of params doesn't exist.