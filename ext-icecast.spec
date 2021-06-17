%global app                     icecast
%global release_prefix          100

Name:                           ext-icecast
Version:                        1.0.1
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure Icecast
License:                        MIT

Source10:                       %{app}.local.xml

Requires:                       icecast

%description
META-package for install and configure Icecast.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{_sysconfdir}/%{app}.local.xml


%files
%config %{_sysconfdir}/%{app}.local.xml


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- UPD: Move to GitHub.
- UPD: License.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-104
- UPD: Configs.

* Tue Jul 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-103
- UPD: SPEC-file.

* Sun Mar 31 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-102
- UPD: "icecast.local.xml".

* Sat Mar 30 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-101
- NEW: 1.0.0-101.

* Fri Feb 15 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-100
- Initial build.
