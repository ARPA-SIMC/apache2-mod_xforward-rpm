%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%define gitname   apache2-mod_xforward
%define gitcommit 8c7ab1b91d219d88f7ded3d817a41b86b2d217a7
%define releaseno 2

Summary:        Apache module to do internal redirect
Name:           mod_xforward
Version:        0.6
Release:        %{releaseno}%{?dist}
Group:          System Environment/Daemons
License:        Apache License, Version 2.0
URL:            https://github.com/openSUSE/apache2-mod_xforward
Source0:        https://github.com/openSUSE/apache2-mod_xforward/archive/%{gitcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/ARPA-SIMC/apache2-mod_xforward-rpm/v%{version}-%{releaseno}/PACKAGE-LICENSING
BuildRequires:  gcc
BuildRequires:  httpd-devel
Requires:       httpd-mmn = %{_httpd_mmn}

%description
Apache module to do internal redirect

Whenever an X-FORWARD header occures in the response headers drop
the body and do an internal redirect to the specified URL via mod_proxy
module.

There is no need to configure a proxy in apache config, we always
trust our backend to send valid redirections.

Method inspired by lighttpd <http://lighttpd.net/>
Code inspired by mod_headers, mod_rewrite and such


%prep
%setup -q -n %{gitname}-%{gitcommit}


%build
%{_httpd_apxs} -c %{name}.c


%install
rm -rf $%{buildroot}
mkdir -p %{buildroot}/%{_httpd_moddir}
%{_httpd_apxs} -i -S LIBEXECDIR=%{buildroot}/%{_httpd_moddir} -n %{name} %{name}.la

cp %{SOURCE1} .


%clean
rm -rf %{buildroot}


%files
%license PACKAGE-LICENSING
%{_httpd_moddir}/%{name}.so


%changelog
* Tue Nov 26 2019 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.6.2
- Add gcc BuildRequire
* Mon Apr 04 2016 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.6-1
- First release
