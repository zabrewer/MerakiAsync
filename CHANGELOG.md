# Change Log
All notable changes to this project will be documented in this file.

## [1.0.01] - 2024-02-14

Minor Updates

### Added
- For any class that accepts perPage and total_pages (for Meraki API endpoints that support pagination), total_pages now defaults to 'all' so that all pages are always returned.  
    
The default can be overridden by passing a different value to the total_pages parameter when calling a specific class method (e.g. AsyncGetOrganizationNetworks).
 
### Changed
- Docstrings were re-worded to make it more clear that optional parameters are passed directly to the class method as opposed to required parameters that should be keys/values in one or more dictionaries nested in a list.

e.g. AsyncGetOrganizationNetworks(networks=[{organizationId: '1234'}], configTemplateId='X_5678')
 
### Fixed
- None

## [1.0.0] - 2024-02-9

Initial release

### Added
   
### Changed
 
### Fixed
