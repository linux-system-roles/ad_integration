Changelog
=========

[1.2.2] - 2023-09-08
--------------------

### Other Changes

- ci: Make badges consistent, run markdownlint all .md files (#53)

  - Consistently generate badges for GH workflows in roles' RHELPLAN-146921
  - Run markdownlint on all .md files
  - Rename woke action to Woke for a pretty badge
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

- ci: Remove badges from README.md prior to converting to HTML (#54)

  - Remove thematic break after badges
  - Remove badges from README.md prior to converting to HTML
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>


[1.2.2] - 2023-09-08
--------------------

### Other Changes

- ci: Make badges consistent, run markdownlint all .md files (#53)

  - Consistently generate badges for GH workflows in roles' RHELPLAN-146921
  - Run markdownlint on all .md files
  - Rename woke action to Woke for a pretty badge
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

- ci: Remove badges from README.md prior to converting to HTML (#54)

  - Remove thematic break after badges
  - Remove badges from README.md prior to converting to HTML
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>


[1.2.1] - 2023-08-21
--------------------

### Bug Fixes

- fix: use command stdin for password, and do not log password (#51)

### Other Changes

- ci: Add markdownlint, test_html_build, and build_docs workflows (#49)

[1.2.0] - 2023-08-11
--------------------

### New Features

- feat: Enable AD dynamic DNS updates (#48)

[1.1.3] - 2023-07-19
--------------------

### Bug Fixes

- fix: facts being gathered unnecessarily (#46)

### Other Changes

- ci: Add pull request template and run commitlint on PR title only (#43)
- ci: Rename commitlint to PR title Lint, echo PR titles from env var (#44)
- ci: ansible-lint - ignore var-naming[no-role-prefix] (#45)

[1.1.2] - 2023-06-06
--------------------

### Other Changes

- tests: Add a test for force rejoin option (#41)

[1.1.1] - 2023-05-26
--------------------

### Other Changes

- docs: Consistent contributing.md for all roles - allow role specific contributing.md section
- docs: remove Dependencies section from README.md

[1.1.0] - 2023-04-27
--------------------

### New Features

- Add 'ad_integration_force_rejoin' role variable (#29)

### Other Changes

- test: check generated files for ansible_managed, fingerprint
- test: ensure the test works with ANSIBLE_GATHERING=explicit
- ci: Add commitlint GitHub action to ensure conventional commits with feedback

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
