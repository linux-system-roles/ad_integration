Changelog
=========

[1.6.0] - 2025-07-02
--------------------

### New Features

- feat: search for name of domain/realm in sssd.conf; merge settings if duplicates (#145)

### Other Changes

- ci: Bump sclorg/testing-farm-as-github-action from 3 to 4 (#136)
- ci: bump tox-lsr to 3.8.0; rename qemu/kvm tests (#137)
- ci: Add Fedora 42; use tox-lsr 3.9.0; use lsr-report-errors for qemu tests (#138)
- ci: Update dyndns test for Fedora 42 and RHEL 10 (#139)
- ci: Add support for bootc end-to-end validation tests (#140)
- ci: Use ansible 2.19 for fedora 42 testing; support python 3.13 (#144)

[1.5.0] - 2025-04-28
--------------------

### New Features

- feat: Introduced option to skip package installation (#131)

### Other Changes

- ci: ansible-plugin-scan is disabled for now (#121)
- ci: bump ansible-lint to v25; provide collection requirements for ansible-lint (#124)
- ci: Check spelling with codespell (#126)
- ci: Add test plan that runs CI tests and customize it for each role (#127)
- ci: In test plans, prefix all relate variables with SR_ (#128)
- ci: Fix bug with ARTIFACTS_URL after prefixing with SR_ (#129)
- ci: several changes related to new qemu test, ansible-lint, python versions, ubuntu versions (#130)
- ci: use tox-lsr 3.6.0; improve qemu test logging (#132)
- ci: skip storage scsi, nvme tests in github qemu ci (#133)
- test: test for ad_integration_manage_packages (#134)

[1.4.8] - 2025-01-09
--------------------

### Other Changes

- ci: Use Fedora 41, drop Fedora 39 (#118)
- ci: Use Fedora 41, drop Fedora 39 - part two (#119)

[1.4.7] - 2024-10-30
--------------------

### Other Changes

- ci: Add tft plan and workflow (#104)
- ci: Update fmf plan to add a separate job to prepare managed nodes (#106)
- ci: bump sclorg/testing-farm-as-github-action from 2 to 3 (#107)
- ci: Add workflow for ci_test bad, use remote fmf plan (#108)
- ci: Fix missing slash in ARTIFACTS_URL (#109)
- ci: Add tags to TF workflow, allow more [citest bad] formats (#112)
- ci: ansible-test action now requires ansible-core version (#113)
- ci: add YAML header to github action workflow files (#114)
- refactor: Use vars/RedHat_N.yml symlink for CentOS, Rocky, Alma wherever possible (#116)

[1.4.6] - 2024-07-02
--------------------

### Bug Fixes

- fix: add support for EL10 (#102)

### Other Changes

- tests: Fix invocation of the `microsoft.ad.user` module (#100)
- ci: ansible-lint action now requires absolute directory (#101)

[1.4.5] - 2024-06-11
--------------------

### Other Changes

- ci: use tox-lsr 3.3.0 which uses ansible-test 2.17 (#95)
- ci: tox-lsr 3.4.0 - fix py27 tests; move other checks to py310 (#97)
- ci: Add supported_ansible_also to .ansible-lint (#98)

[1.4.4] - 2024-04-04
--------------------

### Other Changes

- test: Replace deprecated community.windows.win_domain_user and group modules (#91)
- ci: bump mathieudutour/github-tag-action from 6.1 to 6.2 (#92)

[1.4.3] - 2024-03-08
--------------------

### Bug Fixes

- fix: Sets domain name lower case in realmd.conf section header (#88)

### Other Changes

- ci: bump ansible/ansible-lint from 6 to 24 (#86)
- test: test for lower case realm in realmd.conf (#89)

[1.4.2] - 2024-02-14
--------------------

### Bug Fixes

- fix: Add default_ipv4 to required_facts to gather ansible_hostname (#84)

### Other Changes

- ci: fix python unit test - copy pytest config to tests/unit (#83)

[1.4.1] - 2024-01-23
--------------------

### Other Changes

- ci: Add a basic test for ad_integration_preserve_authselect_profile (#81)

[1.4.0] - 2024-01-16
--------------------

### New Features

- feat: Add SSSD parameters support (#76)
- feat: add ad_integration_preserve_authselect_profile (#79)

### Other Changes

- ci: fix ansible-lint 2.16 and ansible-test 2.16 issues (#74)
- ci: Use supported ansible-lint action; run ansible-lint against the collection (#77)

[1.3.1] - 2023-12-08
--------------------

### Other Changes

- ci: bump actions/github-script from 6 to 7 (#71)
- refactor: get_ostree_data.sh use env shebang - remove from .sanity* (#72)

[1.3.0] - 2023-11-29
--------------------

### New Features

- feat: Add sssd custom settings (#64)
- feat: support for ostree systems (#68)

### Other Changes

- refactor: use the ini_file module to test sssd.conf (#67)

[1.2.3] - 2023-11-08
--------------------

### Other Changes

- build(deps): bump actions/checkout from 3 to 4 (#56)
- ci: ensure dependabot git commit message conforms to commitlint (#59)
- ci: use dump_packages.py callback to get packages used by role (#61)
- ci: tox-lsr version 3.1.1 (#63)
- ci: Add full integration test for dyndns (#65)

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
