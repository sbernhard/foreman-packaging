%global npm_name babel-plugin-transform-object-rest-spread
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 6.26.0
Release: 1%{?dist}
Summary: Compile object rest and spread to ES5
License: MIT
Group: Development/Libraries
URL: https://www.npmjs.com/package/babel-plugin-transform-object-rest-spread
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(babel-plugin-syntax-object-rest-spread) >= 6.8.0
Requires: npm(babel-plugin-syntax-object-rest-spread) < 7.0.0
Requires: npm(babel-runtime) >= 6.26.0
Requires: npm(babel-runtime) < 7.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.26.0-1
- Update to 6.26.0

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 6.16.0-1
- new package built with tito

