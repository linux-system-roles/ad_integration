Changelog
=========

[1.0.3] - 2023-04-06
--------------------

### Other Changes

- Fix typo in README for timesync variable (#23)
- Improve recommendation for AD join user account (#24)
- Add README-ansible.md to refer Ansible intro page on linux-system-roles.github.io (#26)
- Fingerprint RHEL System Role managed config files (#27)

[1.0.2] - 2023-02-15
--------------------

### New Features

- none

### Bug Fixes

- Add `state: up` for the network role to activate the connection (#20)

### Other Changes

- none

[1.0.1] - 2023-01-20
--------------------

### New Features

- none

### Bug Fixes

- ansible-lint 6.x fixes (#11)

### Other Changes

- Add check for non-inclusive language (#10)

[1.0.0] - 2022-12-06
--------------------

### New Features

- initial versioned release

### Bug Fixes

- none

### Other Changes

- Add integration tests for the role. (#4)

[0.0.1] - 2022-11-01
--------------------

### New Features

- New role to manage integrating linux hosts with an Active Directory
  (AD) domain

Implementation uses `realmd` and `adcli`

### Bug Fixes

- none

### Other Changes

- none
