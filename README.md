# collective.js - Plone integration for the List.js library

 + Rigel Di Scala <zedr@ipnext.it>
 + IPnext srl - http://www.ipnext.it


## Introduction

List.js is a lightweight JavaScript library that enhances HTML lists, by 
making them searchable, sortable, orderable, and filterable.

 + http://listjs.com/

*collective.listjs* integrates List.js in Plone 4 by providing the library as a 
resource, together with a set of views that are usable out-of-the-box.


## Installation

In your buildout.cfg, add the following:

    [instance]
    
    eggs =
        ...
        collective.listjs
        
    zcml =
        ...
        collective.listjs

Rerun the Buildout script to download and make available the egg as a new product.

Then, access your Plone instance and install it.


## Usage

A set of views for folderish content are made available once the product is installed.

To enable these views, go to the ZMI/portal_types sections and add the following to
the available_views field of your chosen Folderish types (such as Folder and Topic):

 + listjs_folder_simple_view
 + listjs_folder_tabular_view
    
To use List.js in your products on content, check the docs at http://listjs.com/
