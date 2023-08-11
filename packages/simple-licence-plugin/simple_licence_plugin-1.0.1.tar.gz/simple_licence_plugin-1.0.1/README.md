# simple-licence-plugin
[![PyPI version](https://badge.fury.io/py/simple-licence-plugin.svg)](https://badge.fury.io/py/simple-licence-plugin)
[![Build Status](https://dev.azure.com/CSIROMineralResources/Discovery%20Program/_apis/build/status/simple-licence-plugin?branchName=master)](https://dev.azure.com/CSIROMineralResources/Discovery%20Program/_build/latest?definitionId=1&branchName=master)

## Version: 1.0.1

`simple-licence-plugin` provides a plugin for use with `pyarmor` to allow python code to be commercially distributed in a simple manor. `pyarmor` allows you to obfuscate your code, call plugins, and implement a simple licensing scheme. This plugin provides additional features when using `pyarmor`'s licensing option:
  - Extract data embedded in the licence file (license.lic)
  - Controlling which features are unlocked
  - Calling home via a web service for auditing product usage
  - Ensuring the licence file is for the product
