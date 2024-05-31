yiffparty!
===========

*simple code for fetching yiff images from yiff-party.com*
----------------------------------------------------------

by `Icy\_\_Flames <https://www.reddit.com/user/Icy__Flames>`__

(Works better on Windows, on Linux it is unreliable)

Features
--------

-  Return random yiff image
-  Return newest yiff images in any category
   (gay/straight/animated/anthro/feral/main)
-  Iterate over submissions live as they are uploaded (new images are
   currently uploaded roughly every five minutes)

Usage 
=====

*pip install yiffparty*

.. code:: python

    from yiffparty import horni


    horni.help() # prints a brief overview like this


    print(horni.randomIMG())
    # result will be a random image url


    print(horni.newest("gay"))
    # result will be the newsest image url in the 'gay' category.

    #You can input any of the six categories or 'main' for the main page which includes all categories
    #(gay/lesbian/straight/animated/anthro/feral/main)


    for image in horni.yiff(50,"anthro"):
      print(image)

    #>this will return 50 images in the anthro category


    for image in horni.stream("main"):
      print(image)

    #>This loop will run forever, printing out the images urls as they are uploaded to the site.
