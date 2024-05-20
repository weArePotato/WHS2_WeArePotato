# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bullcode',
 'bullcode.core.manage',
 'bullcode.editor.macos.Bull-code.app.Contents.Resources',
 'bullcode.versions.v0_0_0',
 'bullcode.versions.v1_0_0',
 'bullcode.versions.v1_0_0.packages']

package_data = \
{'': ['*'],
 'bullcode': ['core/*',
              'editor/*',
              'editor/macos/*',
              'editor/macos/Bull-code.app/Contents/*',
              'editor/macos/Bull-code.app/Contents/Frameworks/*',
              'editor/macos/Bull-code.app/Contents/Frameworks/Python.framework/*',
              'editor/macos/Bull-code.app/Contents/Frameworks/Python.framework/Versions/3.11/*',
              'editor/macos/Bull-code.app/Contents/Frameworks/Python.framework/Versions/3.11/Resources/*',
              'editor/macos/Bull-code.app/Contents/Frameworks/Python.framework/Versions/3.11/_CodeSignature/*',
              'editor/macos/Bull-code.app/Contents/Frameworks/Python.framework/Versions/3.11/include/python3.11/*',
              'editor/macos/Bull-code.app/Contents/Frameworks/Python.framework/Versions/3.11/lib/python3.11/config-3.11-darwin/*',
              'editor/macos/Bull-code.app/Contents/MacOS/*',
              'editor/macos/Bull-code.app/Contents/_CodeSignature/*',
              'versions/*'],
 'bullcode.editor.macos.Bull-code.app.Contents.Resources': ['include/python3.11/*',
                                                            'lib/*',
                                                            'lib/python3.11/*',
                                                            'lib/python3.11/config-3.11-darwin/*',
                                                            'lib/python3.11/lib-dynload/*',
                                                            'lib/tcl8.6/*',
                                                            'lib/tcl8.6/encoding/*',
                                                            'lib/tcl8.6/http1.0/*',
                                                            'lib/tcl8.6/msgs/*',
                                                            'lib/tcl8.6/opt0.4/*',
                                                            'lib/tcl8/8.4/*',
                                                            'lib/tcl8/8.4/platform/*',
                                                            'lib/tcl8/8.5/*',
                                                            'lib/tcl8/8.6/*',
                                                            'lib/tcl8/8.6/tdbc/*',
                                                            'lib/tk8.6/*',
                                                            'lib/tk8.6/demos/*',
                                                            'lib/tk8.6/demos/images/*',
                                                            'lib/tk8.6/images/*',
                                                            'lib/tk8.6/msgs/*',
                                                            'lib/tk8.6/ttk/*']}

setup_kwargs = {
    'name': 'bullcode',
    'version': '0.5.0',
    'description': '',
    'long_description': 'None',
    'author': 'GlebChubchikdeveloper',
    'author_email': '111385682+GlebChubchikdeveloper@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
