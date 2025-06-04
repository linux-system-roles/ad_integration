# Direct AD Integration role

[![ansible-lint.yml](https://github.com/linux-system-roles/ad_integration/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/linux-system-roles/ad_integration/actions/workflows/ansible-lint.yml) [![ansible-test.yml](https://github.com/linux-system-roles/ad_integration/actions/workflows/ansible-test.yml/badge.svg)](https://github.com/linux-system-roles/ad_integration/actions/workflows/ansible-test.yml) [![codespell.yml](https://github.com/linux-system-roles/ad_integration/actions/workflows/codespell.yml/badge.svg)](https://github.com/linux-system-roles/ad_integration/actions/workflows/codespell.yml) [![markdownlint.yml](https://github.com/linux-system-roles/ad_integration/actions/workflows/markdownlint.yml/badge.svg)](https://github.com/linux-system-roles/ad_integration/actions/workflows/markdownlint.yml) [![qemu-kvm-integration-tests.yml](https://github.com/linux-system-roles/ad_integration/actions/workflows/qemu-kvm-integration-tests.yml/badge.svg)](https://github.com/linux-system-roles/ad_integration/actions/workflows/qemu-kvm-integration-tests.yml) [![tft.yml](https://github.com/linux-system-roles/ad_integration/actions/workflows/tft.yml/badge.svg)](https://github.com/linux-system-roles/ad_integration/actions/workflows/tft.yml) [![tft_citest_bad.yml](https://github.com/linux-system-roles/ad_integration/actions/workflows/tft_citest_bad.yml/badge.svg)](https://github.com/linux-system-roles/ad_integration/actions/workflows/tft_citest_bad.yml) [![woke.yml](https://github.com/linux-system-roles/ad_integration/actions/workflows/woke.yml/badge.svg)](https://github.com/linux-system-roles/ad_integration/actions/workflows/woke.yml)

An ansible role which configures direct Active Directory integration.

## Supported Distributions

* RHEL7+, CentOS7+
* Fedora

## Requirements

In order to join to the domain, you must use an Active Directory user
which has sufficient join permissions.  It is not recommended to use the
Administrator user as the security footprint of this user is too large.

See [Delegated Permissions](https://www.mankier.com/8/adcli#Delegated_Permissions)
for the explicit permissions a user must have.

Time must be in sync with Active Directory servers. The ad_integration role will use the timesync system role for this if the user specifies [ad_integration_manage_timesync](#ad_integration_manage_timesync) to true and provides a value for [ad_integration_timesync_source](#ad_integration_timesync_source) to use as a timesource.

RHEL8 (and newer) and Fedora no longer support RC4 encryption out of the box, it is recommended to enable AES in Active Directory, if not possible then the AD-SUPPORT crypto policy must be enabled.  The integration role will use the crypto_policies system role for this if the user sets the [ad_integration_manage_crypto_policies](ad_integration_manage_crypto_policies) and [ad_integration_allow_rc4_crypto](#ad_integration_allow_rc4_crypto) parameters to true.

The Linux system must be able to resolve default AD DNS SRV records.

The following firewall ports must be opened on the AD server side, reachable from the Linux client.

| Source Port | Destination | Protocol    | Service                                                   |
|-------------|-------------|-------------|-----------------------------------------------------------|
| 1024:65535  | 53          | TCP and UDP | DNS                                                       |
| 1024:65535  | 389         | TCP and UDP | LDAP                                                      |
| 1024:65535  | 636         | TCP         | LDAPS                                                     |
| 1024:65535  | 88          | TCP and UDP | Kerberos                                                  |
| 1024:65535  | 464         | TCP and UDP | Kerberos change/set password (kadmin)                     |
| 1024:65535  | 3268        | TCP         | LDAP Global Catalog                                       |
| 1024:65535  | 3269        | TCP         | LDAP Global Catalog SSL                                   |
| 1024:65535  | 123         | UDP         | NTP/Chrony(Optional)                                      |
| 1024:65535  | 323         | UDP         | NTP/Chrony (Optional)                                     |

### Collection requirements

This role requires additional modules from external collections.  Please use the
following command to install them:

```bash
ansible-galaxy collection install -vv -r meta/collection-requirements.yml
```

## Role Variables

### Required variables

#### ad_integration_realm

Active Directory realm, or domain name to join

*NOTE* If using this role to manage realm/domain specific settings in SSSD using
([ad_dyndns_update](#ad_dyndns_update) or
[ad_integration_sssd_custom_settings](#ad_integration_sssd_custom_settings),
older versions of the role would make the realm name lower case in the domain
section name.  For example, if you had specified `ad_integration_realm:
EXAMPLE.COM`, then the sssd.conf section would have been `[domain/example.com]`.
The role now will instead use a case-insensitive match to look for an existing
section in sssd.conf, which should already exist.

The result of this is that you may have multiple sections for the domain in your
sssd.conf. If you want to consolidate these sections into one, use
[`ad_integration_sssd_merge_duplicate_sections:
true`](#ad_integration_sssd_merge_duplicate_sections).  See below for more
information about
[ad_integration_sssd_merge_duplicate_sections(#ad_integration_sssd_merge_duplicate_sections).

#### ad_integration_password

The password of the user used to authenticate with when joining the machine to the realm.  Do not use cleartext - use Ansible Vault to encrypt the value.

### Optional variables

#### ad_integration_user

The user name to be used to authenticate with when joining the machine to the realm.

Default: Administrator

#### ad_integration_join_to_dc

an Active Directory domain controller's hostname (do not use IP address) may be specified to join via that domain controller directly.

Default: Not set

#### ad_integration_force_rejoin

Leave existing domain prior to performing join. This might be needed if the keytab is unable to authenticate with the machine account to the AD domain.

Default: false

#### ad_integration_auto_id_mapping

perform automatic UID/GID mapping for users and groups, set to `false` to rely on POSIX attributes already present in Active Directory.

Default: true

#### ad_integration_client_software

Only join realms for which we can use the given client software. Possible values include sssd or winbind. Not all values are supported for all realms.

Default: Automatic selection

#### ad_integration_membership_software

The software to use when joining to the realm. Possible values include samba or adcli. Not all values are supported for all realms.

Default: Automatic selection

#### ad_integration_computer_ou

The distinguished name of an organizational unit to create the computer account. It can be relative to the Root DSE, or a complete LDAP DN.

Default: Default AD computer container

#### ad_integration_manage_timesync

If true, the ad_integration role will use fedora.linux_system_roles.timesync. Requires providing a value for [ad_integration_timesync_source](#ad_integration_timesync_source) to use as a time source.

Default: false

#### ad_integration_timesync_source

Hostname or IP address of time source to synchronize the system clock with. Providing this variable automatically sets [ad_integration_manage_timesync](#ad_integration_manage_timesync) to true.

#### ad_integration_manage_crypto_policies

If true, the ad_integration role will use fedora.linux_system_roles.crypto_policies as needed

Default: false

#### ad_integration_allow_rc4_crypto

If true, the ad_integration role will set the crypto policy allowing RC4 encryption. Providing this variable automatically sets [ad_integration_manage_crypto_policies](#ad_integration_manage_crypto_policies) to true

Default: false

#### ad_integration_manage_dns

If true, the ad_integration role will use fedora.linux_system_roles.network to add the provided dns server (see below) with manual DNS configuration to an existing connection. If true then the following variables are required:

* `ad_integration_dns_server` - DNS server to add
* `ad_integration_dns_connection_name` - Existing network connection name to configure
* `ad_integration_dns_connection_type` - Existing network connection type to configure

#### ad_integration_dns_server

IP address of DNS server to add to existing networking configuration. Only applicable if [ad_integration_manage_dns](#ad_integration_manage_dns) is true

#### ad_integration_dns_connection_name

The name option identifies the connection profile to be configured by the network role. It is not the name of the networking interface for which the profile applies. Only applicable if [ad_integration_manage_dns](#ad_integration_manage_dns) is true

#### ad_integration_dns_connection_type

Network connection type such as ethernet, bridge, bond...etc, the network role contains a list of possible values. Only applicable if [ad_integration_manage_dns](#ad_integration_manage_dns) is true

#### ad_dyndns_update

If true, SSSD is configured to automatically update the AD DNS server with the IP address of the client.

*NOTE*: See the [ad_integration_realm](#ad_integration_realm), and
[ad_integration_sssd_merge_duplicate_sections](#ad_integration_sssd_merge_duplicate_sections)
for information about how the role writes these settings to the sssd.conf file.

Default: false

#### ad_dyndns_ttl

Optional. The TTL, in seconds, to apply to the client's DNS record when updating it. Only applicable if [ad_dyndns_update](#ad_dyndns_update) is true

**Note:** This will override the TTL set by an administrator on the server.

Default: 3600

#### ad_dyndns_iface

Optional. Interface or a list of interfaces whose IP addresses should be used for dynamic DNS updates. Special value "*" implies all IPs from all interfaces should be used. Only applicable if [ad_dyndns_update](#ad_dyndns_update) is true

Default: Use the IP addresses of the interface which is used for AD LDAP connection

#### ad_dyndns_refresh_interval

Optional. How often should, in seconds, periodic DNS updates be performed in addition to when the back end goes online. Only applicable if [ad_dyndns_update](#ad_dyndns_update) is true

**Note:** lowest possible value is 60 seconds. If value less than 60 is specified sssd will assume lowest value only.

Default: 86400

#### ad_dyndns_update_ptr

Optional. If true, the PTR record should also be explicitly updated. Only applicable if [ad_dyndns_update](#ad_dyndns_update) is true

Default: true

#### ad_dyndns_force_tcp

Optional. If true, the nsupdate utility should default to using TCP for communicating with the DNS server. Only applicable if [ad_dyndns_update](#ad_dyndns_update) is true

Default: false

#### ad_dyndns_auth

Optional. If true, GSS-TSIG authentication will be used for secure updates with the DNS server when updating A and AAAA records. Only applicable if [ad_dyndns_update](#ad_dyndns_update) is true

Default: true

#### ad_dyndns_server

Optional. DNS server to use when performing a DNS update when autodetection settings fail. Only applicable if [ad_dyndns_update](#ad_dyndns_update) is true

Default: None (let nsupdate choose the server)

#### ad_integration_join_parameters

Additional parameters (as a string) supplied directly to the realm join command.
Useful if some specific configuration like `--user-principal=host/name@REALM` or `--use-ldaps` is needed.
See man realm for details.
Example: `ad_integration_join_parameters: "--user-principal host/client007@EXAMPLE.COM"`

#### ad_integration_sssd_settings

A list of setting to be included into the `[sssd]` section
of the sssd.conf file. See sssd.conf man pages for details.
Example:

```yaml
ad_integration_sssd_settings:
  - key: "configuration_name"
    value: "configuration_value"
```

#### ad_integration_sssd_custom_settings

A list of custom setting to be included into the `[domain/$REALM]` section
of the sssd.conf file. See sssd.conf man pages for details.
Example:

```yaml
ad_integration_sssd_custom_settings:
  - key: "configuration_name"
    value: "configuration_value"
```

*NOTE*: See the [ad_integration_realm](#ad_integration_realm) and
[ad_integration_sssd_merge_duplicate_sections](#ad_integration_sssd_merge_duplicate_sections) for information about how the
role writes these settings to the sssd.conf file.

#### ad_integration_preserve_authselect_profile

This is a boolean, default is `false`.  If `true`, configure realmd.conf to
remove the `authselect` command from `sssd-enable-logins` to avoid overwriting
previous PAM/nsswitch changes, until
[RHEL-5101](https://issues.redhat.com/browse/RHEL-5101) is addressed.

#### ad_integration_manage_packages

By default, the role installs OS‐level packages needed for Active Directory integration. If `false`, the role assumes that all prerequisites are already in place and skips package installation.

Default: true

#### ad_integration_sssd_merge_duplicate_sections

*NOTE WELL*: This will do a [force rejoin](#ad_integration_force_rejoin) as this
is the only way to clean up sssd.conf and ensure all of the settings are applied
correctly after merging.

This is a boolean, default is `false`.  Because the domain/realm section in
sssd.conf is case insensitive, and you have previously used the role to manage
domain/realm settings in sssd.conf, there may be multiple sections matching the
domain/realm.  If you want to consolidate these sections into one, use
`ad_integration_sssd_merge_duplicate_sections: true`.  For example, if you have
a sssd.conf with both `[domain/example.com]` and `[domain/EXAMPLE.COM]`, and you
want to use only the latter, then use:

```yaml
ad_integration_realm: EXAMPLE.COM
ad_integration_sssd_merge_duplicate_sections: true
ad_integration_sssd_custom_settings: somesettings
```

All of the settings from `[domain/example.com]` will be moved to
`[domain/EXAMPLE.COM]`, and the section `[domain/example.com]` will be removed
from sssd.conf.

## Example Playbook

The following is an example playbook to setup direct Active Directory integration with AD domain `domain.example.com`, the join will be performed with user Administrator using the vault stored password. Prior to the join, the crypto policy for AD SUPPORT with RC4 encryption allowed will be set.

```yaml
- hosts: all
  vars:
    ad_integration_realm: "domain.example.com"
    ad_integration_password: !vault | …vault encrypted password…
    ad_integration_manage_crypto_policies: true
    ad_integration_allow_rc4_crypto: true
  roles:
    - linux-system-roles.ad_integration
```

## rpm-ostree

See README-ostree.md

## License

MIT.

## Author Information

Justin Stephenson (<jstephen@redhat.com>)
