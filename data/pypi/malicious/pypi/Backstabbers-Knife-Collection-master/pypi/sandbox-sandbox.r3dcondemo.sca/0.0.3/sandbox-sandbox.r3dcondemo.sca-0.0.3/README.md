# Educational Package

This package demonstrates a supply-chain attack. 
Please be careful of installing Python dependencies in the future from trusted sources.
This package will be deleted shortly after demonstration purposes.

* Build the package: `python3 -m build`
    - This demo only works on `.tar.gz` build distributions and not `.whl`
* Upload the package to testpypi: `twine upload --repository testpypi dist/r3dc0n.demo-0.0.5.tar.gz`
* Upload the package to pypi: `twine upload dist/r3dc0n.demo-0.0.1.tar.gz`
* Upload to artifactory: `python3 -m twine upload -r prod dist/sandbox-sandbox.r3dcondemo.sca-0.0.1.tar.gz --verbose`
