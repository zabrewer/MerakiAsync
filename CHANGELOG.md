# Change Log
All notable changes to this project will be documented in this file.

## [1.0.02] - 2024-02-19

Minor Updates

### Added

When async_debug flag is set to True, we check for the location of the .py file using the merakiasync library.

MerakiAsync then creates a new directory (merakiasync_logs) in the same directory as the .py file and places all log files in that directory.

example:

If the session is initated from /Users/me/merakiasync_testing/async.py and async.py contains the following snippet of code:
```
async_session = merakiasync.AsyncDashboard(apikey=my_apikey, async_debug=True)
```

1) MerakiAsync checks to see if /Users/me/merakiasync_testing/merakiasync_logs directory exists
2) If it does not, the directory is created
3) All log files while async_debug = True are placed in **/Users/me/merakiasync_testing/merakiasync_logs**

Note that this occurs regardless of how the MerakiAsync library was installed (virtual environment) or where the library exists on the file system (install path).  The **merakiasync_logs** directory is always created in the same folder as the .py file that is using the library.
 
### Changed

MerakiAsync was updated to support version 1.43.0 of the Meraki Dashboard API.  The Meraki Dashboard API Changelog can be found here: https://developer.cisco.com/meraki/whats-new/v1-43-0/

### Fixed

None


## [1.0.01] - 2024-02-14

Minor Updates

### Added

For any class that accepts perPage and total_pages (for Meraki API endpoints that support pagination), total_pages now defaults to 'all' so that all pages are always returned.  
    
The default can be overridden by passing a different value to the total_pages parameter when calling a specific class method (e.g. AsyncGetOrganizationNetworks).
 
### Changed

Docstrings were re-worded to make it more clear that optional parameters are passed directly to the class method as opposed to required parameters that should be keys/values in one or more dictionaries nested in a list.

e.g.
```
AsyncGetOrganizationNetworks(networks=[{organizationId: '1234'}], configTemplateId='X_5678')
```

### Fixed

None

## [1.0.0] - 2024-02-9

Initial release

### Added
   
### Changed
 
### Fixed
